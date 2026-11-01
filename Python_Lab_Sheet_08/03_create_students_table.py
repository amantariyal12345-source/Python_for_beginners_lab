# Question 3: Create a students table with id, name, age, and marks.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)
    print("students table created successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
