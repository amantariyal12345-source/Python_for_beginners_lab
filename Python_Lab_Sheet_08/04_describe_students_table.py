# Question 4: Describe the structure of the students table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("PRAGMA table_info(students)").fetchall()
    if rows:
        for row in rows:
            print(f"Column: {row[1]}, Type: {row[2]}, Not Null: {row[3]}, Primary Key: {row[5]}")
    else:
        print("students table does not exist. Run 03_create_students_table.py first.")
except sqlite3.Error as error:
    print("Database error:", error)
