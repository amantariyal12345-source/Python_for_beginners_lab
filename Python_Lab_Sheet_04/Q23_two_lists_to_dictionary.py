"""Question 23: Convert two lists into a dictionary."""

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()

if len(keys) != len(values):
    print("Error: both lists must have the same number of items.")
else:
    result = {}
    for index in range(len(keys)):
        result[keys[index]] = values[index]
    print("Dictionary:", result)
