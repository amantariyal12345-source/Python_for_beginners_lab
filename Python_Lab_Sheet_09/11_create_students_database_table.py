# Question 11: Connect to a database and create a students table.
import sqlite3
try:
    with sqlite3.connect("student_crud.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)
    print("Connected to student_crud.db and ensured students table exists.")
except sqlite3.Error as error:
    print("Database error:", error)
