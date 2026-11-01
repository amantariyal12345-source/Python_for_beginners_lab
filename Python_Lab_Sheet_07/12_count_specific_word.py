# Question 12: Write a program to count the occurrence of a specific word in a file.
word_to_count = input("Enter the word to count: ").strip()
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().casefold().split()
    count = words.count(word_to_count.casefold()) if word_to_count else 0
    print(f'"{word_to_count}" occurs {count} time(s).')
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
