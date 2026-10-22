"""Question 30: Separate even and odd numbers from a list."""

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)
