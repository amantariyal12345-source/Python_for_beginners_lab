# Question 1: Connect to a SQLite database and display a success message.
import sqlite3
try:
    connection = sqlite3.connect("student_db.db")
    print("Connected to student_db.db successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
