"""Question 29: Find common keys between two dictionaries."""

def read_dictionary(label):
    data = {}
    count = int(input("How many entries in " + label + "? "))
    for index in range(count):
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
    return data

first = read_dictionary("the first dictionary")
second = read_dictionary("the second dictionary")
common_keys = []

for key in first:
    if key in second:
        common_keys.append(key)

print("Common keys:", common_keys)
