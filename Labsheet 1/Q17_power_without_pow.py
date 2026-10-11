# Q17: Calculate power without using pow()
base = float(input("Enter base: "))
exponent = int(input("Enter non-negative integer exponent: "))

if exponent >= 0:
    result = 1
    for _ in range(exponent):
        result *= base
    print("Result =", result)
else:
    print("Please enter a non-negative exponent.")
