"""Run once: python jlpt_seed.py — seeds jlpt_cards from jlpt_words_source.md."""
import os
import re
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "kanji.db")
SOURCE_MD_PATH = os.path.join(os.path.dirname(__file__), "jlpt_words_source.md")


def clean_example(text: str) -> str:
    text = text.replace("**", "")
    text = text.replace("။", "。")
    return re.sub(r"\s+", " ", text).strip()


def load_words_from_markdown(path: str):
    """
    Parse 5-column markdown rows into 3-field tuples:
    (word, reading, "Meaning: ...\\nExample: ...")
    Keeps row order exactly as in markdown.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Source markdown not found: {path}")

    words = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line.startswith("|"):
                continue
            if "Number" in line or "Original words" in line or "--------" in line:
                continue

            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) < 5:
                continue

            word = cols[1]
            reading = cols[2]
            myanmar_meaning = cols[3]
            example = cols[4]

            if not word or not reading:
                continue

            # Skip explicit duplicate-note rows like: （上記xxと重複...）
            if "重複" in example:
                continue

            example = clean_example(example)
            meaning = f"Meaning: {myanmar_meaning}\nExample: {example}" if example else f"Meaning: {myanmar_meaning}"
            words.append((word, reading, meaning))

    if not words:
        raise ValueError("No valid JLPT rows found in markdown source.")
    return words


JLPT_WORDS = load_words_from_markdown(SOURCE_MD_PATH)


def main():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}. Start app.py first to create it.")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS jlpt_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            reading TEXT NOT NULL,
            meaning TEXT NOT NULL
        )
        """
    )

    # Full reseed so order matches markdown exactly
    conn.execute("DELETE FROM jlpt_cards")
    conn.execute("DELETE FROM sqlite_sequence WHERE name = 'jlpt_cards'")
    conn.executemany(
        "INSERT INTO jlpt_cards (word, reading, meaning) VALUES (?,?,?)",
        JLPT_WORDS,
    )

    conn.commit()

    count = conn.execute("SELECT COUNT(*) FROM jlpt_cards").fetchone()[0]
    first10 = conn.execute("SELECT id, word, reading FROM jlpt_cards ORDER BY id LIMIT 10").fetchall()
    conn.close()

    print(f"Done. Seeded {count} JLPT cards from markdown source.")
    print("First 10 rows:")
    for row_id, word, reading in first10:
        safe_word = word.encode("unicode_escape").decode("ascii")
        safe_reading = reading.encode("unicode_escape").decode("ascii")
        print(f"  {row_id}. {safe_word} ({safe_reading})")


if __name__ == "__main__":
    main()
