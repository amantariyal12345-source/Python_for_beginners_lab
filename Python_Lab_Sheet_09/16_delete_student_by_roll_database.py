# Question 16: Delete a student record using roll number (Delete operation).
import sqlite3
try:
    roll_no = int(input("Roll number to delete: "))
    with sqlite3.connect("student_crud.db") as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (roll_no,))
    print("Student deleted." if cursor.rowcount else "Student not found.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
