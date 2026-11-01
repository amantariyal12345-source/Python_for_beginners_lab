# Question 13: Retrieve data sorted by marks in descending order.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute(
            "SELECT * FROM students ORDER BY marks DESC"
        ).fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as error:
    print("Database error:", error)
