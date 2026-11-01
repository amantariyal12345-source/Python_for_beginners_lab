# Question 10: Read and display all records from the students table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("SELECT * FROM students").fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
