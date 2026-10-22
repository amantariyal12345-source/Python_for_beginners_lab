"""Question 25: Count word frequency in a paragraph using a dictionary."""

import string

paragraph = input("Enter a paragraph: ").lower()
cleaned = ""

for char in paragraph:
    if char not in string.punctuation:
        cleaned += char

words = cleaned.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)
