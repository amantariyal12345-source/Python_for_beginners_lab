"""Question 7: Reverse a string without using slicing."""

text = input("Enter a string: ")
result = ""

for char in text:
    result = char + result

print("Reversed string:", result)
