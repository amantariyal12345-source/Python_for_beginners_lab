"""Question 4: Extract all uppercase characters from a string."""

text = input("Enter a string: ")
uppercase_chars = ""

for char in text:
    if char.isupper():
        uppercase_chars += char

print("Uppercase characters:", uppercase_chars)
