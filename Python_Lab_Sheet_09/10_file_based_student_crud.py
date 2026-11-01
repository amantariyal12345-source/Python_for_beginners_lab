# Question 10: Perform CRUD operations on a file: add, view, modify, and delete records.
# Each record is stored as roll_no,name,age,marks in students_records.txt.
import csv
import os

FILE_NAME = "students_records.txt"

def read_records():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def write_records(records):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        fields = ["roll_no", "name", "age", "marks"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)

def add_record():
    records = read_records()
    roll_no = input("Roll number: ").strip()
    if any(record["roll_no"] == roll_no for record in records):
        print("Roll number already exists.")
        return
    records.append({
        "roll_no": roll_no,
        "name": input("Name: ").strip(),
        "age": input("Age: ").strip(),
        "marks": input("Marks: ").strip(),
    })
    write_records(records)
    print("Record added.")

def view_records():
    for record in read_records():
        print(record)
    if not read_records():
        print("No records found.")

def update_record():
    records = read_records()
    roll_no = input("Roll number to update: ").strip()
    for record in records:
        if record["roll_no"] == roll_no:
            record["name"] = input("New name: ").strip()
            record["age"] = input("New age: ").strip()
            record["marks"] = input("New marks: ").strip()
            write_records(records)
            print("Record updated.")
            return
    print("Record not found.")

def delete_record():
    records = read_records()
    roll_no = input("Roll number to delete: ").strip()
    updated = [record for record in records if record["roll_no"] != roll_no]
    if len(updated) == len(records):
        print("Record not found.")
    else:
        write_records(updated)
        print("Record deleted.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            update_record()
        elif choice == "4":
            delete_record()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except (OSError, csv.Error) as error:
        print("File operation failed:", error)
