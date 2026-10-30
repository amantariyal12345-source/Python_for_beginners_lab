"""Write a program to check if two strings are anagrams using sets."""

# Q27. Check whether two strings are anagrams
# Sets first check that both strings contain the same distinct characters.
# Frequency dictionaries then ensure repeated letters occur equally often.
# This is necessary because sets alone do not preserve character counts.

string_a = input("Enter the first string: ").lower().replace(" ", "")
string_b = input("Enter the second string: ").lower().replace(" ", "")

if set(string_a) != set(string_b):
    print("The strings are not anagrams.")
else:
    count_a = {}
    count_b = {}

    for char in string_a:
        count_a[char] = count_a.get(char, 0) + 1

    for char in string_b:
        count_b[char] = count_b.get(char, 0) + 1

    if count_a == count_b:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
