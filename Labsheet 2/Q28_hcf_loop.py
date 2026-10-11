# Q28: Find HCF of two numbers using a loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

if a == 0 and b == 0:
    print("HCF is undefined for both numbers being zero.")
else:
    smaller = a if a < b else b
    hcf = 1

    for divisor in range(1, smaller + 1):
        if a % divisor == 0 and b % divisor == 0:
            hcf = divisor

    print("HCF =", hcf)
