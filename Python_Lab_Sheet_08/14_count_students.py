# Question 14: Count the total number of records in the students table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    print("Total student records:", count)
except sqlite3.Error as error:
    print("Database error:", error)
