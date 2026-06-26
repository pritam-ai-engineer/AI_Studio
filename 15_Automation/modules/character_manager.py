from pathlib import Path
import sqlite3

from utils.logger import log

DATABASE = Path("D:/AI_Studio/15_Automation/database/studio.db")

FOLDERS = [
    "images",
    "videos",
    "voice",
    "poses",
    "expressions",
    "prompts",
]


def create_character(base_path, character_name):

    character = base_path / character_name

    character.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (character / folder).mkdir(exist_ok=True)

    (character / "character.md").touch(exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO characters(name) VALUES(?)",
        (character_name,),
    )

    conn.commit()

    conn.close()

    log(f"Character {character_name} Created")

    print(f"\n✅ Character '{character_name}' Created\n")