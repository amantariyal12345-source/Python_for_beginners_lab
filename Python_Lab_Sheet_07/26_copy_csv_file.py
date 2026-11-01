# Question 26: Write a program to copy data from one CSV file to another.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as source:
        rows = list(csv.reader(source))
    with open("students_copy.csv", "w", newline="", encoding="utf-8") as destination:
        writer = csv.writer(destination)
        writer.writerows(rows)
    print("Copied students.csv to students_copy.csv.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
