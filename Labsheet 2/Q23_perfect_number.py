# Q23: Check if a number is perfect
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Enter a positive integer.")
else:
    divisor_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        print("Perfect number")
    else:
        print("Not a perfect number")
