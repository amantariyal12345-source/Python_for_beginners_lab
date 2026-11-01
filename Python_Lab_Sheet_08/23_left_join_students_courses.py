# Question 23: Perform a LEFT JOIN between students and courses.
import sqlite3
try:
    with sqlite3.connect("student_db.db") as connection:
        rows = connection.execute("""
            SELECT students.name, courses.course_name
            FROM students
            LEFT JOIN courses ON students.id = courses.student_id
        """).fetchall()
    for row in rows:
        print(f"Student: {row[0]}, Course: {row[1]}")
except sqlite3.Error as error:
    print("Database error:", error)
