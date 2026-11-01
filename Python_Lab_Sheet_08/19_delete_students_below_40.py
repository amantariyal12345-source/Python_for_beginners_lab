# Question 19: Delete all students with marks below 40.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("DELETE FROM students WHERE marks < ?", (40,))
    print("Records deleted:", cursor.rowcount)
except sqlite3.Error as error:
    print("Database error:", error)
