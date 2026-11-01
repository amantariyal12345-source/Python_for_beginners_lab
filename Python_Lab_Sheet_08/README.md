# Python Programming Lab Sheet 8 — Database Management

This folder contains one `.py` file for each of the 30 questions in the uploaded Lab Sheet-08 PDF.

## Database choice
These solutions use SQLite (`sqlite3`), which is included with Python 3. The database file `student_db.db` is created automatically in this folder when a program connects.

## How to run
1. Install Python 3.
2. Extract this folder.
3. Open a terminal/command prompt in this folder.
4. Run `python 03_create_students_table.py` to create the main table.
5. Run a program, for example: `python 08_insert_single_student.py`.

## Recommended order
- Start with `01_connect_database.py`, `02_create_database.py`, and `03_create_students_table.py`.
- Use `09_insert_multiple_students.py` to add sample student records.
- Run `21_create_courses_and_insert.py` before the JOIN examples.
- For CSV import, create `students_import.csv` with columns `name,age,marks` and run `27_import_csv_to_database.py`.
- Each program is independent; some create, update, or delete records.

## Notes
- SQLite has no `TRUNCATE TABLE` statement. Question 20 uses `DELETE FROM students`, which empties the table while preserving its structure.
- SQLite `CREATE DATABASE` is handled by connecting to a new database filename, so Question 2 creates/opens `student_db.db`.
- The course table links to students through `student_id` for the INNER JOIN and LEFT JOIN examples.
- All SQL values supplied by the user use parameterized queries.
