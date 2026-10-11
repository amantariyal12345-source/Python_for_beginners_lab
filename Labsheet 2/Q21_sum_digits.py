# Q21: Find the sum of digits of a number
number = int(input("Enter a number: "))

number = abs(number)
total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of digits =", total)
