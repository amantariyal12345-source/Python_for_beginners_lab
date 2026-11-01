# Question 23: Write a program to read a CSV file and calculate the average of numeric columns.
# Uses students.csv with column headings such as Name, Marks, Age.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        totals = {}
        counts = {}
        for row in reader:
            for column, value in row.items():
                try:
                    number = float(value)
                except (TypeError, ValueError):
                    continue
                totals[column] = totals.get(column, 0) + number
                counts[column] = counts.get(column, 0) + 1
    if not totals:
        print("No numeric columns found.")
    else:
        for column in totals:
            print(f"Average of {column}: {totals[column] / counts[column]:.2f}")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
