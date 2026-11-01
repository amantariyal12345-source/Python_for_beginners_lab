# Question 20: Empty a table while keeping its structure intact.
# SQLite has no TRUNCATE TABLE command; DELETE removes all rows and preserves the table.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        connection.execute("DELETE FROM students")
    print("students table emptied; its structure is unchanged.")
except sqlite3.Error as error:
    print("Database error:", error)
