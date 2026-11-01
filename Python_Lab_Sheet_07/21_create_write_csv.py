# Question 21: Write a Python program to create and write data into a CSV file.
import csv

rows = [
    ["Name", "Marks", "Age"],
    ["Aarav", 85, 20],
    ["Diya", 92, 19],
    ["Kabir", 78, 21],
]
try:
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Data written to students.csv.")
except OSError as error:
    print(f"File error: {error}")
