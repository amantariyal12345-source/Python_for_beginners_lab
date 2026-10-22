"""Question 18: Sort the characters of a string alphabetically."""

text = input("Enter a string: ")
characters = list(text)

# Use bubble sort to avoid using sorted().
for i in range(len(characters)):
    for j in range(0, len(characters) - i - 1):
        if characters[j].lower() > characters[j + 1].lower():
            characters[j], characters[j + 1] = characters[j + 1], characters[j]

print("Sorted characters:", "".join(characters))
