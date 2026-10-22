"""Question 22: Sort a list of integers in ascending and descending order."""

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
ascending = numbers.copy()

# Bubble sort in ascending order.
for i in range(len(ascending)):
    for j in range(0, len(ascending) - i - 1):
        if ascending[j] > ascending[j + 1]:
            ascending[j], ascending[j + 1] = ascending[j + 1], ascending[j]

descending = ascending[::-1]
print("Ascending order:", ascending)
print("Descending order:", descending)
