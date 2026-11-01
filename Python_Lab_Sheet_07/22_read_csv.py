# Question 22: Write a program to read data from a CSV file and display it.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
