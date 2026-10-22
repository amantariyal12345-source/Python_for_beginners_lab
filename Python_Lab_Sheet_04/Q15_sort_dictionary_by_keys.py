"""Question 15: Sort a dictionary by keys."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

keys = list(data.keys())
for i in range(len(keys)):
    for j in range(0, len(keys) - i - 1):
        if keys[j] > keys[j + 1]:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

sorted_data = {}
for key in keys:
    sorted_data[key] = data[key]

print("Dictionary sorted by keys:", sorted_data)
