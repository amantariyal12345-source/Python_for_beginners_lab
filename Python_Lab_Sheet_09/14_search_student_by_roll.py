# Question 14: Search for a specific student by roll number.
import sqlite3
try:
    roll_no = int(input("Enter roll number to search: "))
    with sqlite3.connect("student_crud.db") as connection:
        record = connection.execute("SELECT * FROM students WHERE id=?", (roll_no,)).fetchone()
    print(record if record else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
