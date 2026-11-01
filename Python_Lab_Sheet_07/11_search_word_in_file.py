# Question 11: Write a program to search for a particular word in a file.
word_to_find = input("Enter the word to search for: ").strip()
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    if word_to_find and word_to_find.casefold() in content.casefold().split():
        print(f'"{word_to_find}" was found in sample.txt.')
    else:
        print(f'"{word_to_find}" was not found as a separate word in sample.txt.')
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
