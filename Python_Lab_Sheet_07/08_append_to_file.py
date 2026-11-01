# Question 8: Write a program to append new content to an existing file.
try:
    with open("sample.txt", "a", encoding="utf-8") as file:
        file.write("This line was appended later.\n")
    print("New content appended to sample.txt.")
except OSError as error:
    print(f"File error: {error}")
