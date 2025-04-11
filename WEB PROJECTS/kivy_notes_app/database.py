import sqlite3

class NotesDatabase:
    def __init__(self, db_name="data/notes.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_note(self, title, content):
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    def delete_note(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
