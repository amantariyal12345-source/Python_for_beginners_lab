"""Question 21: Find the largest and smallest elements in a list."""

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

if not numbers:
    print("The list is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    print("Largest element:", largest)
    print("Smallest element:", smallest)
