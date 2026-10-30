"""Write a program to find the symmetric difference of two sets."""

# Q14. Find the symmetric difference of two sets
# It contains elements that belong to either set, but not both.

set_a = set(input("Enter elements of the first set: ").split())
set_b = set(input("Enter elements of the second set: ").split())

print("Symmetric difference:", set_a.symmetric_difference(set_b))
