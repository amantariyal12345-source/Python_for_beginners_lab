"""Question 22: Create a dictionary with numbers as keys and their squares as values."""

n = int(input("Enter a positive integer n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    squares = {}
    for number in range(1, n + 1):
        squares[number] = number * number
    print("Number-square dictionary:", squares)
