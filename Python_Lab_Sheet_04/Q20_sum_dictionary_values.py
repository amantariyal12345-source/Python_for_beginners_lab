"""Question 20: Find the sum of all values in a dictionary."""

data = {}
count = int(input("How many numeric key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    data[key] = value

total = 0
for value in data.values():
    total += value

print("Sum of dictionary values:", total)
