"""Question 1: Find the sum and average of elements in a list."""

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

if not numbers:
    print("The list is empty.")
else:
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)
