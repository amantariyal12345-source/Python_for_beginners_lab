# Question 27: Write a program to display specific columns (like Name and Marks) from a CSV file.
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "Name" not in reader.fieldnames or "Marks" not in reader.fieldnames:
            print('CSV must contain "Name" and "Marks" column headings.')
        else:
            print("Name | Marks")
            for row in reader:
                print(f'{row["Name"]} | {row["Marks"]}')
except FileNotFoundError:
    print("students.csv was not found. Run 21_create_write_csv.py first.")
except OSError as error:
    print(f"File error: {error}")
