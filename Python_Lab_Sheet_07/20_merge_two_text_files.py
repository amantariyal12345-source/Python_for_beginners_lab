# Question 20: Write a program to merge two text files into a third file.
# This program expects first.txt and second.txt in the same folder.
try:
    with open("first.txt", "r", encoding="utf-8") as first:
        first_content = first.read()
    with open("second.txt", "r", encoding="utf-8") as second:
        second_content = second.read()
    with open("merged.txt", "w", encoding="utf-8") as merged:
        merged.write(first_content)
        if first_content and not first_content.endswith("\n"):
            merged.write("\n")
        merged.write(second_content)
    print("Merged first.txt and second.txt into merged.txt.")
except FileNotFoundError as error:
    print(f"Required input file not found: {error.filename}")
except OSError as error:
    print(f"File error: {error}")
