import sqlite3

class SessionStore:
    def __init__(self, db_path="session.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS context (key TEXT, value TEXT)")
        self.conn.commit()

    def save(self, key, value):
        self.cursor.execute("INSERT INTO context VALUES (?, ?)", (key, value))
        self.conn.commit()

    def load(self, key):
        self.cursor.execute("SELECT value FROM context WHERE key=?", (key,))
        result = self.cursor.fetchone()
        return result[0] if result else None
