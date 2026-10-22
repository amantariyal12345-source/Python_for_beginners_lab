"""Question 19: Check if a key exists in a dictionary."""

data = {}
count = int(input("How many key-value pairs? "))

for index in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

search_key = input("Enter the key to search for: ")
if search_key in data:
    print("Key exists. Value:", data[search_key])
else:
    print("Key does not exist.")
