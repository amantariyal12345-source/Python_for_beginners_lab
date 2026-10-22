"""Question 27: Find the second largest number in a list."""

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("At least two distinct numbers are required.")
else:
    largest = unique_numbers[0]
    second_largest = None

    for number in unique_numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number

    print("Second largest number:", second_largest)
