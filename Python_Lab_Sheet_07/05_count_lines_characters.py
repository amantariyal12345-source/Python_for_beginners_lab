# Question 5: Write a program to count the number of lines and characters in a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("Number of lines:", len(content.splitlines()))
    print("Number of characters:", len(content))
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
