"""Question 3: Replace all spaces in a string with underscores."""

text = input("Enter a string: ")
result = ""

for char in text:
    if char == " ":
        result += "_"
    else:
        result += char

print("Updated string:", result)
