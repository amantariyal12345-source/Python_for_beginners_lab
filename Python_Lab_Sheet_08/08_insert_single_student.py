# Question 8: Insert a single record into the students table.
import sqlite3
try:
    student = (
        input("Name: ").strip(),
        int(input("Age: ")),
        float(input("Marks: "))
    )
    with sqlite3.connect("student_db.db") as connection:
        connection.execute(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", student
        )
    print("Student inserted successfully.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
