# Question 2: Create a new database.
# SQLite creates the database file automatically when connect() is called.
import sqlite3
try:
    connection = sqlite3.connect("student_db.db")
    print("Database student_db.db created/opened successfully.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if "connection" in locals():
        connection.close()
