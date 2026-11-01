# Question 5: List all tables available in the connected database.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        tables = connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
    print("Tables:", [row[0] for row in tables])
except sqlite3.Error as error:
    print("Database error:", error)
