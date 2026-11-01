# Question 29: Write a program to search a record in a CSV file based on student name.
import csv

name_to_find = input("Enter the student name to search: ").strip()
try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        matches = [
            row for row in reader
            if row.get("Name", "").casefold() == name_to_find.casefold()
        ]
    if matches:
        for row in matches:
            print(row)
    else:
        print("No matching student record found.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
