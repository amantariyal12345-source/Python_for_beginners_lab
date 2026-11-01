# Question 28: Write a program to find and display the highest marks from a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        students = list(csv.DictReader(file))
    marked_students = []
    for student in students:
        try:
            marked_students.append((float(student["Marks"]), student["Name"]))
        except (KeyError, ValueError):
            continue
    if marked_students:
        highest_marks = max(marked_students, key=lambda item: item[0])[0]
        print("Highest marks:", highest_marks)
        print("Student(s):", ", ".join(name for marks, name in marked_students if marks == highest_marks))
    else:
        print("No valid marks found in students.csv.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
