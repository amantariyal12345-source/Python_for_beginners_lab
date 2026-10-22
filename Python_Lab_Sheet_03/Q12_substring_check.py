"""Question 12: Check if a substring exists in a given string."""

text = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
