# Question 15: Write a program to replace a word in a file with another word.
old_word = input("Enter the word to replace: ")
new_word = input("Enter the replacement word: ")
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()
    # Replace the exact word while keeping the rest of the file unchanged.
    import re
    updated_content = re.sub(rf"\b{re.escape(old_word)}\b", lambda _: new_word, content)
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(updated_content)
    print("Word replacement completed in sample.txt.")
except FileNotFoundError:
    print("sample.txt was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
