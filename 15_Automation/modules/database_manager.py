import sqlite3
from pathlib import Path

DATABASE = Path("D:/AI_Studio/15_Automation/database/studio.db")


def connect():
    return sqlite3.connect(DATABASE)


def initialize_database():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS characters(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS episodes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        episode_number INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database initialized.")