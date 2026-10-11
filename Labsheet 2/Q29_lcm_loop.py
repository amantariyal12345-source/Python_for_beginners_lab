# Q29: Find LCM of two numbers using a loop
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

if a == 0 or b == 0:
    print("LCM =", 0)
else:
    greater = a if a > b else b
    lcm = greater

    while lcm % a != 0 or lcm % b != 0:
        lcm += greater

    print("LCM =", lcm)
