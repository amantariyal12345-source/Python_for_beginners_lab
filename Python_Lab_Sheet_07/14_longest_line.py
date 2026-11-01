# Question 14: Write a program to display the longest line in a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        longest_line = max(lines, key=len)
        print("Longest line:", longest_line.rstrip())
        print("Length:", len(longest_line.rstrip("\n")))
    else:
        print("The file is empty.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
