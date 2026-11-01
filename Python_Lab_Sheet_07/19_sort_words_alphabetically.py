# Question 19: Write a program to sort all words in a file alphabetically and save to a new file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().split()
    sorted_words = sorted(words, key=str.casefold)
    with open("sorted_words.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(sorted_words))
        if sorted_words:
            file.write("\n")
    print("Alphabetically sorted words saved to sorted_words.txt.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
