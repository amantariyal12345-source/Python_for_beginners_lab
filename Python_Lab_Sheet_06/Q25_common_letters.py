"""Write a program to find common letters in two strings using sets."""

# Q25. Find common letters in two strings using sets
# Spaces are excluded and comparison is case-insensitive.

string_a = input("Enter the first string: ").lower().replace(" ", "")
string_b = input("Enter the second string: ").lower().replace(" ", "")

common_letters = set(string_a) & set(string_b)
print("Common letters:", common_letters)
