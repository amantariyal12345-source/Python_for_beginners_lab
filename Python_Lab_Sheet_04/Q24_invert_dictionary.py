"""Question 24: Invert a dictionary (keys become values and values become keys)."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter original key: ")
    value = input("Enter value (must be unique to avoid overwriting): ")
    data[key] = value

inverted = {}
for key, value in data.items():
    inverted[value] = key

print("Original dictionary:", data)
print("Inverted dictionary:", inverted)
