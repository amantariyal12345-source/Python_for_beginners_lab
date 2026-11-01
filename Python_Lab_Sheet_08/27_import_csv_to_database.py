# Question 27: Import data from a CSV file into the students table.
# CSV should have columns: name, age, marks (with or without a header row).
import csv
import sqlite3
try:
    with open("students_import.csv", "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    if rows and [item.strip().casefold() for item in rows[0][:3]] == ["name", "age", "marks"]:
        rows = rows[1:]
    records = [(row[0], int(row[1]), float(row[2])) for row in rows if len(row) >= 3]
    with sqlite3.connect("student_db.db") as connection:
        connection.executemany(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", records
        )
    print(f"Imported {len(records)} records from students_import.csv.")
except FileNotFoundError:
    print("students_import.csv not found. Create it with name, age, marks columns.")
except (sqlite3.Error, OSError, ValueError, IndexError) as error:
    print("Error:", error)
