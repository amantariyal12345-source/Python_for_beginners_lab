# Question 18: Delete a student record using ID.
import sqlite3
try:
    student_id = int(input("Student ID to delete: "))
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (student_id,))
    print("Student deleted." if cursor.rowcount else "No student found with that ID.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
