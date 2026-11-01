# Question 24: Write a program to count the number of rows and columns in a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if rows:
        print("Number of rows excluding header:", max(0, len(rows) - 1))
        print("Number of columns:", len(rows[0]))
    else:
        print("The CSV file is empty.")
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
