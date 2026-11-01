# Question 12: Insert a new record into the students table (Create operation).
import sqlite3
try:
    roll_no = int(input("Roll number: "))
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect("student_crud.db") as connection:
        connection.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (roll_no, name, age, marks)
        )
    print("Student record inserted.")
except (sqlite3.Error, ValueError) as error:
    print("Error:", error)
