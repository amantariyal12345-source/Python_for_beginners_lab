"""Question 13: Convert vowels to uppercase and consonants to lowercase."""

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char.isalpha():
        if char in vowels:
            result += char.upper()
        else:
            result += char.lower()
    else:
        result += char

print("Converted string:", result)
