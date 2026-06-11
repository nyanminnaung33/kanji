from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.environ.get("DATABASE_URL")
USE_PG = bool(DATABASE_URL)

if USE_PG:
    import psycopg2
    import psycopg2.extras
    _PK = "id SERIAL PRIMARY KEY"
    _STRIP_EXAMPLE_SQL = """
        CASE
          WHEN strpos(meaning, chr(10) || 'Example:') > 0
            THEN substr(meaning, 1, strpos(meaning, chr(10) || 'Example:') - 1)
          ELSE meaning
        END"""
else:
    import sqlite3
    DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(__file__), "kanji.db"))
    _PK = "id INTEGER PRIMARY KEY AUTOINCREMENT"
    _STRIP_EXAMPLE_SQL = """
        CASE
          WHEN instr(meaning, char(10) || 'Example:') > 0
            THEN substr(meaning, 1, instr(meaning, char(10) || 'Example:') - 1)
          ELSE meaning
        END"""


def get_db():
    if USE_PG:
        return psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _p(sql):
    return sql.replace("?", "%s") if USE_PG else sql


def run(conn, sql, params=()):
    if USE_PG:
        cur = conn.cursor()
        cur.execute(_p(sql), params or None)
        return cur
    return conn.execute(sql, params)


def runmany(conn, sql, params_list):
    if USE_PG:
        cur = conn.cursor()
        cur.executemany(_p(sql), params_list)
        return cur
    return conn.executemany(sql, params_list)


def getall(conn, sql, params=()):
    return [dict(r) for r in run(conn, sql, params).fetchall()]


def getone(conn, sql, params=()):
    r = run(conn, sql, params).fetchone()
    return dict(r) if r else None


def insert_id(conn, sql, params):
    if USE_PG:
        cur = conn.cursor()
        cur.execute(_p(sql) + " RETURNING id", params)
        return cur.fetchone()["id"]
    return conn.execute(sql, params).lastrowid


def init_jlpt_table():
    from jlpt_seed import JLPT_WORDS
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS jlpt_cards (
            {_PK},
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL
        )
    """)
    run(conn, "DELETE FROM jlpt_cards")
    runmany(conn, "INSERT INTO jlpt_cards (word, reading, meaning) VALUES (?,?,?)", JLPT_WORDS)
    conn.commit()
    conn.close()


def init_db():
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS cards (
            {_PK},
            kanji TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL,
            example_word TEXT,
            example_reading TEXT,
            example_meaning TEXT
        )
    """)
    conn.commit()

    from add_words import NEW_WORDS
    seed_data = [
        ("職", "しょく", "job, work, occupation, duty / role", None, None, None),
        ("職業", "しょくぎょう", "occupation / profession", "職業を選ぶ", "しょくぎょうをえらぶ", "to choose an occupation"),
        ("無職", "むしょく", "unemployed", "無職の状態", "むしょくのじょうたい", "state of being unemployed"),
        ("職場", "しょくば", "workplace", "職場の仲間", "しょくばのなかま", "workplace colleagues"),
        ("退職", "たいしょく", "resignation (leaving a job)", "退職を決める", "たいしょくをきめる", "to decide to resign"),
        ("就職", "しゅうしょく", "getting a job", "就職活動", "しゅうしょくかつどう", "job hunting"),
        ("職務", "しょくむ", "job duties", "職務を果たす", "しょくむをはたす", "to fulfill one's duties"),
        ("公職", "こうしょく", "public office", "公職に就く", "こうしょくにつく", "to take public office"),
    ]
    all_seed = seed_data + list(NEW_WORDS)
    run(conn, "DELETE FROM cards")
    runmany(
        conn,
        "INSERT INTO cards (kanji, reading, meaning, example_word, example_reading, example_meaning) VALUES (?,?,?,?,?,?)",
        all_seed,
    )
    conn.commit()
    conn.close()


@app.route("/api/cards", methods=["GET"])
def get_cards():
    conn = get_db()
    result = getall(conn, "SELECT * FROM cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/cards/<int:card_id>", methods=["GET"])
def get_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(card)


@app.route("/api/cards", methods=["POST"])
def create_card():
    data = request.get_json()
    required = ["kanji", "reading", "meaning"]
    if not all(k in data for k in required):
        return jsonify({"error": "kanji, reading, and meaning are required"}), 400
    conn = get_db()
    new_id = insert_id(
        conn,
        "INSERT INTO cards (kanji, reading, meaning, example_word, example_reading, example_meaning) VALUES (?,?,?,?,?,?)",
        (data["kanji"], data["reading"], data["meaning"],
         data.get("example_word"), data.get("example_reading"), data.get("example_meaning")),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM cards WHERE id = ?", (new_id,))
    conn.close()
    return jsonify(card), 201


@app.route("/api/cards/<int:card_id>", methods=["PUT"])
def update_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    run(conn,
        "UPDATE cards SET kanji=?, reading=?, meaning=?, example_word=?, example_reading=?, example_meaning=? WHERE id=?",
        (data.get("kanji", card["kanji"]),
         data.get("reading", card["reading"]),
         data.get("meaning", card["meaning"]),
         data.get("example_word", card["example_word"]),
         data.get("example_reading", card["example_reading"]),
         data.get("example_meaning", card["example_meaning"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/cards/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    run(conn, "DELETE FROM cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Card deleted"})


@app.route("/api/jlpt", methods=["GET"])
def get_jlpt():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        result = getall(conn, f"""
            SELECT * FROM jlpt_cards
            WHERE word LIKE ?
               OR reading LIKE ?
               OR ({_STRIP_EXAMPLE_SQL}) LIKE ?
            ORDER BY id
            """, (like, like, like))
    else:
        result = getall(conn, "SELECT * FROM jlpt_cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/jlpt/<int:card_id>", methods=["GET"])
def get_jlpt_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM jlpt_cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(card)


@app.route("/api/jlpt/<int:card_id>", methods=["PUT"])
def update_jlpt_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM jlpt_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn,
        "UPDATE jlpt_cards SET word=?, reading=?, meaning=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("meaning", card["meaning"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM jlpt_cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/jlpt/<int:card_id>", methods=["DELETE"])
def delete_jlpt_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM jlpt_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn, "DELETE FROM jlpt_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


def init_favourites():
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS favourites (
            {_PK},
            card_type TEXT NOT NULL,
            card_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL,
            UNIQUE(card_type, card_id)
        )
    """)
    conn.commit()
    conn.close()


def reconcile_favourites():
    """After reseeding, fix card_id references using word+reading as the stable key."""
    conn = get_db()
    favs = getall(conn, "SELECT * FROM favourites")
    for fav in favs:
        if fav["card_type"] == "jlpt":
            current = getone(conn, "SELECT id FROM jlpt_cards WHERE word=? AND reading=?",
                             (fav["word"], fav["reading"]))
        elif fav["card_type"] == "n3":
            current = getone(conn, "SELECT id FROM n3_cards WHERE word=? AND reading=?",
                             (fav["word"], fav["reading"]))
        elif fav["card_type"] == "n4":
            current = getone(conn, "SELECT id FROM n4_cards WHERE word=? AND reading=?",
                             (fav["word"], fav["reading"]))
        elif fav["card_type"] == "marugoto":
            current = getone(conn, "SELECT id FROM marugoto_cards WHERE word=? AND reading=?",
                             (fav["word"], fav["reading"]))
        elif fav["card_type"] == "exam_key":
            current = getone(conn, "SELECT id FROM exam_key_cards WHERE word=? AND reading=?",
                             (fav["word"], fav["reading"]))
        else:
            current = getone(conn, "SELECT id FROM cards WHERE kanji=? AND reading=?",
                             (fav["word"], fav["reading"]))

        if current is None:
            run(conn, "DELETE FROM favourites WHERE id=?", (fav["id"],))
        elif current["id"] != fav["card_id"]:
            try:
                run(conn, "UPDATE favourites SET card_id=? WHERE id=?", (current["id"], fav["id"]))
            except Exception:
                if USE_PG:
                    conn.rollback()
                run(conn, "DELETE FROM favourites WHERE id=?", (fav["id"],))
    conn.commit()
    conn.close()


@app.route("/api/favourites", methods=["GET"])
def get_favourites():
    conn = get_db()
    result = getall(conn, "SELECT * FROM favourites ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/favourites", methods=["POST"])
def add_favourite():
    data = request.get_json()
    required = ["card_type", "card_id", "word", "reading", "meaning"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400
    conn = get_db()
    try:
        new_id = insert_id(
            conn,
            "INSERT INTO favourites (card_type, card_id, word, reading, meaning) VALUES (?,?,?,?,?)",
            (data["card_type"], data["card_id"], data["word"], data["reading"], data["meaning"]),
        )
        conn.commit()
        fav = getone(conn, "SELECT * FROM favourites WHERE id = ?", (new_id,))
        conn.close()
        return jsonify(fav), 201
    except Exception:
        conn.close()
        return jsonify({"error": "Already favourited"}), 409


@app.route("/api/favourites/<string:card_type>/<int:card_id>", methods=["DELETE"])
def remove_favourite(card_type, card_id):
    conn = get_db()
    run(conn, "DELETE FROM favourites WHERE card_type=? AND card_id=?", (card_type, card_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Removed"})


def init_passages():
    from passages import PASSAGES
    conn = get_db()
    run(conn, "DROP TABLE IF EXISTS passages")
    run(conn, f"""
        CREATE TABLE passages (
            {_PK},
            title TEXT NOT NULL,
            level TEXT NOT NULL,
            text TEXT NOT NULL,
            translation TEXT NOT NULL DEFAULT ''
        )
    """)
    runmany(
        conn,
        "INSERT INTO passages (title, level, text, translation) VALUES (?,?,?,?)",
        [(p["title"], p["level"], p["text"], p.get("translation", "")) for p in PASSAGES],
    )
    conn.commit()
    conn.close()


@app.route("/api/passages", methods=["GET"])
def get_passages():
    conn = get_db()
    result = getall(
        conn,
        "SELECT id, title, level, substr(text, 1, 60) AS preview FROM passages ORDER BY id",
    )
    conn.close()
    return jsonify(result)


@app.route("/api/passages/<int:passage_id>", methods=["GET"])
def get_passage(passage_id):
    from passages import PASSAGES
    conn = get_db()
    passage = getone(conn, "SELECT * FROM passages WHERE id = ?", (passage_id,))
    if passage is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404

    text = passage["text"]
    cards = getall(conn, "SELECT kanji AS word, reading, meaning FROM cards")
    jlpt = getall(conn, "SELECT word, reading, meaning FROM jlpt_cards")
    conn.close()

    seen = set()
    words = []
    for w in cards + jlpt:
        word = w["word"]
        if word and word in text and word not in seen:
            seen.add(word)
            words.append({"word": word, "reading": w["reading"], "meaning": w["meaning"]})

    vocab_raw = PASSAGES[passage_id - 1].get("vocab", []) if passage_id <= len(PASSAGES) else []
    vocab = [{"word": v[0], "hiragana": v[1], "breakdown": v[2], "meaning": v[3]} for v in vocab_raw]

    return jsonify({**passage, "words": words, "vocab": vocab})


def init_n3_table():
    from n3_seed import N3_WORDS
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS n3_cards (
            {_PK},
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL,
            myanmar_meaning TEXT NOT NULL DEFAULT ''
        )
    """)
    run(conn, "DELETE FROM n3_cards")
    runmany(conn, "INSERT INTO n3_cards (word, reading, meaning, myanmar_meaning) VALUES (?,?,?,?)", N3_WORDS)
    conn.commit()
    conn.close()


@app.route("/api/n3", methods=["GET"])
def get_n3():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        result = getall(conn, """
            SELECT * FROM n3_cards
            WHERE word LIKE ?
               OR reading LIKE ?
               OR meaning LIKE ?
               OR myanmar_meaning LIKE ?
            ORDER BY id
        """, (like, like, like, like))
    else:
        result = getall(conn, "SELECT * FROM n3_cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/n3/<int:card_id>", methods=["GET"])
def get_n3_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM n3_cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(card)


@app.route("/api/n3/<int:card_id>", methods=["PUT"])
def update_n3_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM n3_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn,
        "UPDATE n3_cards SET word=?, reading=?, meaning=?, myanmar_meaning=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("meaning", card["meaning"]),
         data.get("myanmar_meaning", card["myanmar_meaning"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM n3_cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/n3/<int:card_id>", methods=["DELETE"])
def delete_n3_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM n3_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn, "DELETE FROM n3_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


def init_n4_table():
    from n4_seed import N4_WORDS
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS n4_cards (
            {_PK},
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            myanmar_meaning TEXT NOT NULL DEFAULT ''
        )
    """)
    run(conn, "DELETE FROM n4_cards")
    runmany(conn, "INSERT INTO n4_cards (word, reading, myanmar_meaning) VALUES (?,?,?)", N4_WORDS)
    conn.commit()
    conn.close()


@app.route("/api/n4", methods=["GET"])
def get_n4():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        result = getall(conn, """
            SELECT * FROM n4_cards
            WHERE word LIKE ?
               OR reading LIKE ?
               OR myanmar_meaning LIKE ?
            ORDER BY id
        """, (like, like, like))
    else:
        result = getall(conn, "SELECT * FROM n4_cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/n4/<int:card_id>", methods=["GET"])
def get_n4_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM n4_cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(card)


@app.route("/api/n4/<int:card_id>", methods=["PUT"])
def update_n4_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM n4_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn,
        "UPDATE n4_cards SET word=?, reading=?, myanmar_meaning=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("myanmar_meaning", card["myanmar_meaning"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM n4_cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/n4/<int:card_id>", methods=["DELETE"])
def delete_n4_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM n4_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn, "DELETE FROM n4_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


def init_marugoto_table():
    from marugoto_seed import MARUGOTO_WORDS
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS marugoto_cards (
            {_PK},
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            myanmar_meaning TEXT NOT NULL DEFAULT ''
        )
    """)
    run(conn, "DELETE FROM marugoto_cards")
    runmany(conn, "INSERT INTO marugoto_cards (word, reading, myanmar_meaning) VALUES (?,?,?)", MARUGOTO_WORDS)
    conn.commit()
    conn.close()


@app.route("/api/marugoto", methods=["GET"])
def get_marugoto():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        result = getall(conn, """
            SELECT * FROM marugoto_cards
            WHERE word LIKE ?
               OR reading LIKE ?
               OR myanmar_meaning LIKE ?
            ORDER BY id
        """, (like, like, like))
    else:
        result = getall(conn, "SELECT * FROM marugoto_cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/marugoto/<int:card_id>", methods=["GET"])
def get_marugoto_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM marugoto_cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(card)


@app.route("/api/marugoto/<int:card_id>", methods=["PUT"])
def update_marugoto_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM marugoto_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn,
        "UPDATE marugoto_cards SET word=?, reading=?, myanmar_meaning=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("myanmar_meaning", card["myanmar_meaning"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM marugoto_cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/marugoto/<int:card_id>", methods=["DELETE"])
def delete_marugoto_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM marugoto_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn, "DELETE FROM marugoto_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


def init_exam_key_table():
    from exam_key_seed import EXAM_KEY_WORDS
    conn = get_db()
    run(conn, f"""
        CREATE TABLE IF NOT EXISTS exam_key_cards (
            {_PK},
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            myanmar_meaning TEXT NOT NULL DEFAULT '',
            example TEXT NOT NULL DEFAULT ''
        )
    """)
    run(conn, "DELETE FROM exam_key_cards")
    runmany(conn, "INSERT INTO exam_key_cards (word, reading, myanmar_meaning, example) VALUES (?,?,?,?)", EXAM_KEY_WORDS)
    conn.commit()
    conn.close()


@app.route("/api/exam_key", methods=["GET"])
def get_exam_key():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        result = getall(conn, """
            SELECT * FROM exam_key_cards
            WHERE word LIKE ?
               OR reading LIKE ?
               OR myanmar_meaning LIKE ?
               OR example LIKE ?
            ORDER BY id
        """, (like, like, like, like))
    else:
        result = getall(conn, "SELECT * FROM exam_key_cards ORDER BY id")
    conn.close()
    return jsonify(result)


@app.route("/api/exam_key/<int:card_id>", methods=["GET"])
def get_exam_key_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM exam_key_cards WHERE id = ?", (card_id,))
    conn.close()
    if card is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(card)


@app.route("/api/exam_key/<int:card_id>", methods=["PUT"])
def update_exam_key_card(card_id):
    data = request.get_json()
    conn = get_db()
    card = getone(conn, "SELECT * FROM exam_key_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn,
        "UPDATE exam_key_cards SET word=?, reading=?, myanmar_meaning=?, example=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("myanmar_meaning", card["myanmar_meaning"]),
         data.get("example", card["example"]),
         card_id),
    )
    conn.commit()
    card = getone(conn, "SELECT * FROM exam_key_cards WHERE id = ?", (card_id,))
    conn.close()
    return jsonify(card)


@app.route("/api/exam_key/<int:card_id>", methods=["DELETE"])
def delete_exam_key_card(card_id):
    conn = get_db()
    card = getone(conn, "SELECT * FROM exam_key_cards WHERE id = ?", (card_id,))
    if card is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    run(conn, "DELETE FROM exam_key_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


init_db()
init_jlpt_table()
init_n3_table()
init_n4_table()
init_marugoto_table()
init_exam_key_table()
init_favourites()
init_passages()
reconcile_favourites()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
