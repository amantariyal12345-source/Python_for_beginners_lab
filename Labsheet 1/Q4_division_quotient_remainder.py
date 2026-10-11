# Q4: Display quotient and remainder of two integers
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))

if b != 0:
    quotient = a // b
    remainder = a % b
    print("Quotient =", quotient)
    print("Remainder =", remainder)
else:
    print("Division by zero is not allowed.")
