"""Question 3: Remove all negative numbers from a list."""

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
non_negative = []

for number in numbers:
    if number >= 0:
        non_negative.append(number)

print("List without negative numbers:", non_negative)
