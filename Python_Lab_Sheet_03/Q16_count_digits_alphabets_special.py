"""Question 16: Count digits, alphabets, and special characters in a string."""

text = input("Enter a string: ")
digits = 0
alphabets = 0
special = 0

for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special)
