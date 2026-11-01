# Question 15: Update the marks of a student using roll number (Update operation).
import sqlite3
try:
    roll_no = int(input("Roll number: "))
    marks = float(input("New marks: "))
    with sqlite3.connect("student_crud.db") as connection:
        cursor = connection.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll_no))
    print("Marks updated." if cursor.rowcount else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
