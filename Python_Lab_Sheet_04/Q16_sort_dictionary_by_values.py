"""Question 16: Sort a dictionary by values."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    data[key] = value

items = list(data.items())
for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j][1] > items[j + 1][1]:
            items[j], items[j + 1] = items[j + 1], items[j]

sorted_data = {}
for key, value in items:
    sorted_data[key] = value

print("Dictionary sorted by values:", sorted_data)
