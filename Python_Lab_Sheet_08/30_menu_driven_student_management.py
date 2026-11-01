# Question 30: Menu-driven student management application (Add, View, Update, Delete).
import sqlite3

DB_NAME = "student_db.db"

def add_student():
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
            (name, age, marks)
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
    student_id = int(input("Student ID to update: "))
    marks = float(input("New marks: "))
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute(
            "UPDATE students SET marks=? WHERE id=?", (marks, student_id)
        )
    print("Student updated." if cursor.rowcount else "Student ID not found.")

def delete_student():
    student_id = int(input("Student ID to delete: "))
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (student_id,))
    print("Student deleted." if cursor.rowcount else "Student ID not found.")

def main():
    # Ensure the table exists before showing the menu.
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
        print("\n1. Add Student\n2. View Students\n3. Update Marks\n4. Delete Student\n5. Exit")
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
                print("Exiting student management.")
                break
            else:
                print("Invalid choice. Select 1-5.")
        except (sqlite3.Error, ValueError) as error:
            print("Operation failed:", error)

if __name__ == "__main__":
    try:
        main()
    except sqlite3.Error as error:
        print("Database error:", error)
