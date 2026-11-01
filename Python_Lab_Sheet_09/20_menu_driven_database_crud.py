# Question 20: Menu-driven application to perform all CRUD operations using a database.
import sqlite3

DB_NAME = "student_crud.db"

def add_student():
    roll_no = int(input("Roll number: "))
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (roll_no, name, age, marks)
        )
    print("Student added.")

def view_students():
    with sqlite3.connect(DB_NAME) as connection:
        rows = connection.execute("SELECT * FROM students ORDER BY id").fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("No student records found.")

def update_student():
    roll_no = int(input("Roll number to update: "))
    marks = float(input("New marks: "))
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("UPDATE students SET marks=? WHERE id=?", (marks, roll_no))
    print("Student updated." if cursor.rowcount else "Student not found.")

def delete_student():
    roll_no = int(input("Roll number to delete: "))
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (roll_no,))
    print("Student deleted." if cursor.rowcount else "Student not found.")

def main():
    # Ensure the database table exists before using the menu.
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)
    while True:
        print("\n1. Add\n2. View\n3. Update Marks\n4. Delete\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting.")
                break
            else:
                print("Invalid choice.")
        except (sqlite3.Error, ValueError) as error:
            print("Operation failed:", error)

if __name__ == "__main__":
    try:
        main()
    except sqlite3.Error as error:
        print("Database error:", error)
