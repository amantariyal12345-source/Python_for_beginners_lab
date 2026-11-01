# Question 11: Display only the name and marks columns.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("SELECT name, marks FROM students").fetchall()
    for row in rows:
        print(f"Name: {row[0]}, Marks: {row[1]}")
except sqlite3.Error as error:
    print("Database error:", error)
