# Q30: Check whether a number is prime
number = int(input("Enter an integer: "))

if number < 2:
    print("Not a prime number")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
