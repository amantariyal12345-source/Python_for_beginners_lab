"""Question 23: Remove duplicate elements from a list."""

items = input("Enter list items separated by spaces: ").split()
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("List without duplicates:", unique_items)
