"""Question 17: Update the value of a key in a dictionary."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

key_to_update = input("Enter the key to update: ")
if key_to_update in data:
    new_value = input("Enter the new value: ")
    data[key_to_update] = new_value
    print("Updated dictionary:", data)
else:
    print("Key not found. Dictionary unchanged:", data)
