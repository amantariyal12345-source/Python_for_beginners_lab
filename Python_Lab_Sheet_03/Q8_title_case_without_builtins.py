"""Question 8: Convert a string into title case without using built-in title-case functions."""

text = input("Enter a string: ")
result = ""
make_upper = True

for char in text:
    if char == " ":
        result += char
        make_upper = True
    elif make_upper:
        result += char.upper()
        make_upper = False
    else:
        result += char.lower()

print("Title case:", result)
