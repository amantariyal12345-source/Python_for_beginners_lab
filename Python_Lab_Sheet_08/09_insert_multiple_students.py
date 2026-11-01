# Question 9: Insert multiple records into the students table.
import sqlite3
students = [
    ("Aarav", 20, 85.0),
    ("Diya", 19, 92.0),
    ("Kabir", 21, 78.0),
]
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.executemany(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", students
        )
    print(f"Inserted {len(students)} student records.")
except sqlite3.Error as error:
    print("Database error:", error)
