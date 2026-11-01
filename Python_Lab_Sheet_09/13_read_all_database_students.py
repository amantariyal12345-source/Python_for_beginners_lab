# Question 13: Read and display all records from the students table.
import sqlite3
try:
    with sqlite3.connect("student_crud.db") as connection:
        records = connection.execute("SELECT * FROM students").fetchall()
    for record in records:
        print(record)
    if not records:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
