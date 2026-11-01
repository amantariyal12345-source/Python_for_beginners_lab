# Question 16: Update the marks of a student using their ID.
import sqlite3
try:
    student_id = int(input("Student ID: "))
    new_marks = float(input("New marks: "))
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute(
            "UPDATE students SET marks=? WHERE id=?", (new_marks, student_id)
        )
    print("Student marks updated." if cursor.rowcount else "No student found with that ID.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
