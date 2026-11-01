# Question 19: Find the student with the highest marks from the database.
import sqlite3
try:
    with sqlite3.connect("student_crud.db") as connection:
        record = connection.execute(
            "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
        ).fetchone()
    print("Highest-scoring student:", record if record else "No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
