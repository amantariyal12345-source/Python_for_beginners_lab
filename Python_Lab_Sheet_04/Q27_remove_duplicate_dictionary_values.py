"""Question 27: Remove duplicate values from a dictionary."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

unique_data = {}
seen_values = []

for key, value in data.items():
    if value not in seen_values:
        unique_data[key] = value
        seen_values.append(value)

print("Dictionary after removing duplicate values:", unique_data)
