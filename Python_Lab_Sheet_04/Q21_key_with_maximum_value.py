"""Question 21: Find the key with the maximum value in a dictionary."""

data = {}
count = int(input("How many numeric key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = float(input("Enter numeric value: "))
    data[key] = value

if not data:
    print("The dictionary is empty.")
else:
    keys = list(data.keys())
    maximum_key = keys[0]

    for key in keys:
        if data[key] > data[maximum_key]:
            maximum_key = key

    print("Key with maximum value:", maximum_key)
    print("Maximum value:", data[maximum_key])
