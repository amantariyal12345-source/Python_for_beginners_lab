# Question 28: Display database errors using exception handling.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        # This deliberately uses a nonexistent table to demonstrate error handling.
        connection.execute("SELECT * FROM table_that_does_not_exist").fetchall()
except sqlite3.Error as error:
    print("Database error caught:", error)
