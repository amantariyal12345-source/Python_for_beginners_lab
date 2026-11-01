# Question 1: Write a Python program to create and write text into a file.
# Open the file in write mode; it will be created if it does not exist.
try:
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write("Hello, this is a sample text file.\n")
        file.write("Python file handling is easy to learn.\n")
    print("Text written to sample.txt successfully.")
except OSError as error:
    print(f"File error: {error}")
