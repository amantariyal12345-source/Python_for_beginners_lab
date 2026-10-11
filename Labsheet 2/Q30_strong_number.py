# Q30: Check if a number is strong
# A strong number equals the sum of factorials of its digits.
number = int(input("Enter a positive integer: "))

if number < 0:
    print("Enter a positive integer.")
else:
    original = number
    total = 0

    if number == 0:
        total = 1
    else:
        while number > 0:
            digit = number % 10

            factorial = 1
            for value in range(1, digit + 1):
                factorial *= value

            total += factorial
            number //= 10

    if total == original:
        print("Strong number")
    else:
        print("Not a strong number")
