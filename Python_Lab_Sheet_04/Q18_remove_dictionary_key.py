"""Question 18: Remove a key from a dictionary."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

key_to_remove = input("Enter the key to remove: ")
if key_to_remove in data:
    del data[key_to_remove]
    print("Updated dictionary:", data)
else:
    print("Key not found. Dictionary unchanged:", data)
