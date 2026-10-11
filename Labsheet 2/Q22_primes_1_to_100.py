# Q22: Print all prime numbers between 1 and 100
for number in range(2, 101):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()
