# Question 29: Use functions to insert and fetch data (modular approach).
import sqlite3

def insert_student(name, age, marks):
    """Insert one student using a parameterized query."""
    with sqlite3.connect("student_db.db") as connection:
        connection.execute(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
            (name, age, marks)
        )

def fetch_students():
    """Return all student records."""
    with sqlite3.connect("student_db.db") as connection:
        return connection.execute("SELECT * FROM students").fetchall()

try:
    insert_student("Sample Student", 20, 88.5)
    print("Inserted a sample student.")
    for student in fetch_students():
        print(student)
except sqlite3.Error as error:
    print("Database error:", error)
