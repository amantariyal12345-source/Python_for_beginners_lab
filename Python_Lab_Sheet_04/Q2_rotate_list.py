"""Question 2: Rotate a list by n positions."""

items = input("Enter list items separated by spaces: ").split()
n = int(input("Enter number of positions to rotate to the right: "))

if items:
    n = n % len(items)
    rotated = items[-n:] + items[:-n] if n != 0 else items[:]
else:
    rotated = []

print("Rotated list:", rotated)
