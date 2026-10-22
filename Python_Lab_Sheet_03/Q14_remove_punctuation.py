"""Question 14: Remove all punctuation from a string."""

import string

text = input("Enter a string: ")
result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print("String without punctuation:", result)
