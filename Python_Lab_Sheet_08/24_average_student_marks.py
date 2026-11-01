# Question 24: Find the average marks of all students.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        average = connection.execute("SELECT AVG(marks) FROM students").fetchone()[0]
    print("Average marks:", average if average is not None else "No marks available")
except sqlite3.Error as error:
    print("Database error:", error)
