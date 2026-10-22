"""Question 28: Find common elements in two lists."""

first = input("Enter the first list items separated by spaces: ").split()
second = input("Enter the second list items separated by spaces: ").split()
common = []

for item in first:
    if item in second and item not in common:
        common.append(item)

print("Common elements:", common)
