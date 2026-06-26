import sqlite3
from pathlib import Path

DB = Path("database/studio.db")


class PromptController:

    def __init__(self):

        self.conn = sqlite3.connect(DB)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS prompts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            category TEXT,

            prompt TEXT
        )
        """)

        self.conn.commit()

    def get_all(self):

        self.cursor.execute("""
        SELECT title,category
        FROM prompts
        ORDER BY title
        """)

        return self.cursor.fetchall()

    def add(self,title,category,prompt):

        self.cursor.execute("""

        INSERT INTO prompts(title,category,prompt)

        VALUES(?,?,?)

        """,(title,category,prompt))

        self.conn.commit()

    def delete(self,title):

        self.cursor.execute("""

        DELETE FROM prompts

        WHERE title=?

        """,(title,))

        self.conn.commit()