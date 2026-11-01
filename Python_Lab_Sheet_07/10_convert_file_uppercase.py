# Question 10: Write a program to read a file and convert its content to uppercase.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content.upper())
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
