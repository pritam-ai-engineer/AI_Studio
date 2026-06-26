import sqlite3
from pathlib import Path

DB = Path("database/studio.db")


class CharacterController:

    def __init__(self):

        self.conn = sqlite3.connect(DB)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS characters(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        """)

        self.conn.commit()

    def get_all(self):

        self.cursor.execute("""
            SELECT name
            FROM characters
            ORDER BY name
        """)

        return self.cursor.fetchall()

    def add(self, name):

        self.cursor.execute("""
            INSERT OR IGNORE
            INTO characters(name)
            VALUES(?)
        """, (name,))

        self.conn.commit()

    def delete(self, name):

        self.cursor.execute("""
            DELETE
            FROM characters
            WHERE name=?
        """, (name,))

        self.conn.commit()