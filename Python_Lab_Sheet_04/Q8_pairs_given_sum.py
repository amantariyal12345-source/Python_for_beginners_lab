"""Question 8: Find pairs of numbers in a list whose sum is equal to a given number."""

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))
found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)
            found = True

if not found:
    print("No pairs found.")
