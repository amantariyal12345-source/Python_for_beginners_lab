"""Write a program to find the union of two sets."""

# Q11. Find the union of two sets

set_a = set(input("Enter elements of the first set: ").split())
set_b = set(input("Enter elements of the second set: ").split())

print("Union:", set_a.union(set_b))
