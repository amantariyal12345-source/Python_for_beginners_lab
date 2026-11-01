# Python Programming Lab Sheet 9 — CRUD Operations

This folder contains separate Python source files for all 20 questions in the uploaded Lab Sheet-09 PDF.

## Requirements
- Python 3
- SQLite support through Python's built-in `sqlite3` module (no extra installation required)

## How to run
1. Extract this folder.
2. Open a terminal in the folder.
3. Run `python 11_create_students_database_table.py` before database exercises 12–20.
4. Run any program, for example: `python 12_insert_student_record.py`.

## Contents
- Questions 1–8: CRUD using lists, dictionaries, books, employees, and products.
- Questions 9–10: Text-file storage and file-based CRUD.
- Questions 11–20: Database CRUD using SQLite and a menu-driven application.

## Notes
- Database exercises use `student_crud.db` and a table named `students(id, name, age, marks)`.
- Each program is separate. List/dictionary data is held in memory and resets when the program exits.
- File-based records are saved in `students_records.txt`.
- Use unique roll numbers for database insert operations because `id` is the primary key.
