"""Question 5: Create a list of squares of numbers from 1 to n."""

n = int(input("Enter a positive integer n: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    squares = []
    for number in range(1, n + 1):
        squares.append(number * number)
    print("Squares from 1 to", n, ":", squares)
