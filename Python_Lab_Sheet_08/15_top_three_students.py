# Question 15: Display the top 3 highest-scoring students.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students ORDER BY marks DESC LIMIT 3"
        ).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
