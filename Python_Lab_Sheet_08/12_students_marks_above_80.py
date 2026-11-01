# Question 12: Retrieve records where marks are greater than 80.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students WHERE marks > ?", (80,)
        ).fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No students scored above 80.")
except sqlite3.Error as error:
    print("Database error:", error)
