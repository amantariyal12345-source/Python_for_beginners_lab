# Q3: Check if a number is an Armstrong number
number = int(input("Enter a number: "))

original = number
digits = 0
temp = number

if temp == 0:
    digits = 1
else:
    while temp > 0:
        digits += 1
        temp //= 10

temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
