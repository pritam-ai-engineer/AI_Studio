import sqlite3
from pathlib import Path


class DatabaseService:

    def __init__(self):

        self.db = Path("database/studio.db")

        self.conn = sqlite3.connect(self.db)

        self.cursor = self.conn.cursor()

    def count_characters(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM characters"
        )

        return self.cursor.fetchone()[0]

    def count_prompts(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM prompts"
        )

        return self.cursor.fetchone()[0]

    def close(self):

        self.conn.close()