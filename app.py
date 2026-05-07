from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), "kanji.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_jlpt_table():
    from jlpt_seed import JLPT_WORDS
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jlpt_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL
        )
    """)
    conn.commit()
    if conn.execute("SELECT COUNT(*) FROM jlpt_cards").fetchone()[0] == 0:
        conn.executemany(
            "INSERT INTO jlpt_cards (word, reading, meaning) VALUES (?,?,?)",
            JLPT_WORDS,
        )
        conn.commit()
    conn.close()


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kanji TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL,
            example_word TEXT,
            example_reading TEXT,
            example_meaning TEXT
        )
    """)
    conn.commit()

    if conn.execute("SELECT COUNT(*) FROM cards").fetchone()[0] == 0:
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
        conn.executemany(
            "INSERT INTO cards (kanji, reading, meaning, example_word, example_reading, example_meaning) VALUES (?,?,?,?,?,?)",
            seed_data,
        )
        conn.commit()
    conn.close()


@app.route("/api/cards", methods=["GET"])
def get_cards():
    conn = get_db()
    rows = conn.execute("SELECT * FROM cards ORDER BY id").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/api/cards/<int:card_id>", methods=["GET"])
def get_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "Card not found"}), 404
    return jsonify(dict(row))


@app.route("/api/cards", methods=["POST"])
def create_card():
    data = request.get_json()
    required = ["kanji", "reading", "meaning"]
    if not all(k in data for k in required):
        return jsonify({"error": "kanji, reading, and meaning are required"}), 400
    conn = get_db()
    cur = conn.execute(
        "INSERT INTO cards (kanji, reading, meaning, example_word, example_reading, example_meaning) VALUES (?,?,?,?,?,?)",
        (data["kanji"], data["reading"], data["meaning"],
         data.get("example_word"), data.get("example_reading"), data.get("example_meaning")),
    )
    conn.commit()
    new_id = cur.lastrowid
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (new_id,)).fetchone()
    conn.close()
    return jsonify(dict(row)), 201


@app.route("/api/cards/<int:card_id>", methods=["PUT"])
def update_card(card_id):
    data = request.get_json()
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    card = dict(row)
    conn.execute(
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
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    return jsonify(dict(row))


@app.route("/api/cards/<int:card_id>", methods=["DELETE"])
def delete_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Card not found"}), 404
    conn.execute("DELETE FROM cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Card deleted"})


@app.route("/api/jlpt", methods=["GET"])
def get_jlpt():
    q = request.args.get("q", "").strip()
    conn = get_db()
    if q:
        like = f"%{q}%"
        rows = conn.execute(
            "SELECT * FROM jlpt_cards WHERE word LIKE ? OR reading LIKE ? OR meaning LIKE ? ORDER BY id",
            (like, like, like),
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM jlpt_cards ORDER BY id").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/api/jlpt/<int:card_id>", methods=["GET"])
def get_jlpt_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM jlpt_cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))


@app.route("/api/jlpt/<int:card_id>", methods=["PUT"])
def update_jlpt_card(card_id):
    data = request.get_json()
    conn = get_db()
    row = conn.execute("SELECT * FROM jlpt_cards WHERE id = ?", (card_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    card = dict(row)
    conn.execute(
        "UPDATE jlpt_cards SET word=?, reading=?, meaning=? WHERE id=?",
        (data.get("word", card["word"]),
         data.get("reading", card["reading"]),
         data.get("meaning", card["meaning"]),
         card_id),
    )
    conn.commit()
    row = conn.execute("SELECT * FROM jlpt_cards WHERE id = ?", (card_id,)).fetchone()
    conn.close()
    return jsonify(dict(row))


@app.route("/api/jlpt/<int:card_id>", methods=["DELETE"])
def delete_jlpt_card(card_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM jlpt_cards WHERE id = ?", (card_id,)).fetchone()
    if row is None:
        conn.close()
        return jsonify({"error": "Not found"}), 404
    conn.execute("DELETE FROM jlpt_cards WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted"})


init_db()
init_jlpt_table()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
