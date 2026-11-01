# Question 17: Update the name of a student.
import sqlite3
try:
    student_id = int(input("Student ID: "))
    new_name = input("New name: ").strip()
    with sqlite3.connect("student_db.db") as connection:
        cursor = connection.execute(
            "UPDATE students SET name=? WHERE id=?", (new_name, student_id)
        )
    print("Student name updated." if cursor.rowcount else "No student found with that ID.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
