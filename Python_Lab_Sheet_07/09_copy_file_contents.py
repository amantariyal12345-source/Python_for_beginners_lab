# Question 9: Write a program to copy the contents of one file into another.
source_file = "sample.txt"
destination_file = "copy_of_sample.txt"
try:
    with open(source_file, "r", encoding="utf-8") as source:
        content = source.read()
    with open(destination_file, "w", encoding="utf-8") as destination:
        destination.write(content)
    print(f"Copied {source_file} to {destination_file}.")
except FileNotFoundError:
    print(f"{source_file} was not found. Run 01_create_write_file.py first.")
except OSError as error:
    print(f"File error: {error}")
