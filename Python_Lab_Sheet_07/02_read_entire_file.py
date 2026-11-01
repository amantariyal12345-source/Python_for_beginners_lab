# Question 2: Write a program to read the entire content of a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
