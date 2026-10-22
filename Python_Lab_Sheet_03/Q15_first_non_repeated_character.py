"""Question 15: Find the first non-repeated character in a string."""

text = input("Enter a string: ")
found = False

for char in text:
    count = 0
    for item in text:
        if item == char:
            count += 1
    if count == 1:
        print("First non-repeated character:", char)
        found = True
        break

if not found:
    print("There is no non-repeated character.")
