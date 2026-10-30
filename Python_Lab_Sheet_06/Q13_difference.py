"""Write a program to find the difference of two sets."""

# Q13. Find the difference of two sets (A - B)

set_a = set(input("Enter elements of the first set: ").split())
set_b = set(input("Enter elements of the second set: ").split())

print("Difference (A - B):", set_a.difference(set_b))
