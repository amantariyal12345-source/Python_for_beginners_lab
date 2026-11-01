# Question 18: Display all records sorted by student name.
import sqlite3
try:
    with sqlite3.connect("student_crud.db") as connection:
        records = connection.execute("SELECT * FROM students ORDER BY name ASC").fetchall()
    for record in records:
        print(record)
except sqlite3.Error as error:
    print("Database error:", error)
