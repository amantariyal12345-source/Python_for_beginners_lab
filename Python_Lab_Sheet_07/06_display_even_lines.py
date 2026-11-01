# Question 6: Write a program to display only even-numbered lines from a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line_number % 2 == 0:
                print(f"Line {line_number}: {line.rstrip()}")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
