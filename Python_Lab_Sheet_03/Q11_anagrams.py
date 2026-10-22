"""Question 11: Check if two strings are anagrams of each other."""

first = input("Enter the first string: ").lower().replace(" ", "")
second = input("Enter the second string: ").lower().replace(" ", "")

if len(first) != len(second):
    print("The strings are not anagrams.")
else:
    remaining = list(second)
    is_anagram = True

    for char in first:
        if char in remaining:
            remaining.remove(char)
        else:
            is_anagram = False
            break

    if is_anagram:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
