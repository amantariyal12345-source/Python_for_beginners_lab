# Q19: Reverse a number using a loop
number = int(input("Enter a number: "))

sign = -1 if number < 0 else 1
number = abs(number)
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reversed number =", sign * reverse)
