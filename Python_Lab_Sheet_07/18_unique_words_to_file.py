# Question 18: Write a program to read a file and store only unique words into another file.
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        words = file.read().split()
    # Keep the first occurrence of each word, ignoring case for uniqueness.
    unique_words = []
    seen = set()
    for word in words:
        key = word.casefold()
        if key not in seen:
            seen.add(key)
            unique_words.append(word)
    with open("unique_words.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(unique_words))
        if unique_words:
            file.write("\n")
    print("Unique words saved to unique_words.txt.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
