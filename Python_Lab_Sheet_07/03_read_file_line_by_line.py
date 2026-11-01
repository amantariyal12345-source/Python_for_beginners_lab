# Question 3: Write a program to read a file line by line.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.rstrip()}")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
