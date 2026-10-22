"""Question 1: Check if a string is a palindrome."""

text = input("Enter a string: ")

# Compare the string with its reverse.
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

if text.lower() == reversed_text.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
