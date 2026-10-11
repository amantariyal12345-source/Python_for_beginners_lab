# Q16: Find remainder when one number is divided by another
number = int(input("Enter number: "))
divisor = int(input("Enter divisor: "))

if divisor != 0:
    remainder = number % divisor
    print("Remainder =", remainder)
else:
    print("Division by zero is not allowed.")
