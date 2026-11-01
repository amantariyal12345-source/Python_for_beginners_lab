# Question 25: Write a program to append a new record to an existing CSV file.
import csv
import os

try:
    file_exists = os.path.exists("students.csv") and os.path.getsize("students.csv") > 0
    with open("students.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Marks", "Age"])
        name = input("Enter student name: ").strip()
        marks = input("Enter marks: ").strip()
        age = input("Enter age: ").strip()
        writer.writerow([name, marks, age])
    print("Student record appended to students.csv.")
except OSError as error:
    print(f"File error: {error}")
