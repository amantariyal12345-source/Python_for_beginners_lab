# Question 6: Drop (delete) a table from the database.
import sqlite3
table_name = input("Enter table name to drop (students/courses): ").strip()
allowed_tables = {"students", "courses"}
if table_name not in allowed_tables:
    print("Invalid table name.")
else:
    try:
        with sqlite3.connect("student_db.db") as connection:
            connection.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"{table_name} table dropped if it existed.")
    except sqlite3.Error as error:
        print("Database error:", error)
