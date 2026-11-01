# Question 17: Write a program to remove blank lines from a file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    non_blank_lines = [line for line in lines if line.strip()]
    with open("without_blank_lines.txt", "w", encoding="utf-8") as file:
        file.writelines(non_blank_lines)
    print("Blank lines removed. Result saved to without_blank_lines.txt.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
