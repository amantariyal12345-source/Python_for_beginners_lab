"""Question 14: Merge two dictionaries into one."""

first = {}
second = {}

count1 = int(input("Number of entries in first dictionary: "))
for index in range(count1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    first[key] = value

count2 = int(input("Number of entries in second dictionary: "))
for index in range(count2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    second[key] = value

merged = first.copy()
for key, value in second.items():
    merged[key] = value

print("Merged dictionary:", merged)
