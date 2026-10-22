"""Question 29: Find the difference between two lists (items in the first list that are not in the second)."""

first = input("Enter the first list items separated by spaces: ").split()
second = input("Enter the second list items separated by spaces: ").split()
difference = []

for item in first:
    if item not in second and item not in difference:
        difference.append(item)

print("Difference (first list minus second list):", difference)
