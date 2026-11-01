# Question 4: Write a program to count the number of words in a text file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        word_count = len(file.read().split())
    print("Number of words:", word_count)
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
