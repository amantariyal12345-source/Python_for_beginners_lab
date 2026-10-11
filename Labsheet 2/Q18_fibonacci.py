# Q18: Print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))

first = 0
second = 1

if n <= 0:
    print("Enter a positive number of terms.")
else:
    for _ in range(n):
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term
    print()
