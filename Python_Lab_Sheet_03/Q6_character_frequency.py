"""Question 6: Find the frequency of each character in a string."""

text = input("Enter a string: ")
checked = ""

for char in text:
    if char not in checked:
        count = 0
        for item in text:
            if item == char:
                count += 1
        print(repr(char) + ":", count)
        checked += char
