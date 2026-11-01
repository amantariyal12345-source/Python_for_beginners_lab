# Question 21: Create a courses table and insert data into it.
import sqlite3
courses = [
    ("Python Programming", 1),
    ("Database Management", 2),
    ("Computer Networks", 3),
]
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                course_name TEXT NOT NULL,
                student_id INTEGER
            )
        """)
        connection.executemany(
            "INSERT INTO courses (course_name, student_id) VALUES (?, ?)", courses
        )
    print("courses table created and records inserted.")
except sqlite3.Error as error:
    print("Database error:", error)
