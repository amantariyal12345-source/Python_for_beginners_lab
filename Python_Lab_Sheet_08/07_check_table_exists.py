# Question 7: Check whether a specific table exists in the database.
import sqlite3
table_name = input("Enter table name to check: ").strip()
try:
    with sqlite3.connect("student_db.db") as connection:
        result = connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,)
        ).fetchone()
    print("Table exists." if result else "Table does not exist.")
except sqlite3.Error as error:
    print("Database error:", error)
