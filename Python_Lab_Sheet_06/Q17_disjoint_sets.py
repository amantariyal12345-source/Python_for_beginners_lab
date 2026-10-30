"""Write a program to check if two sets are disjoint."""

# Q17. Check whether two sets are disjoint
# Disjoint sets have no common elements.

set_a = set(input("Enter elements of the first set: ").split())
set_b = set(input("Enter elements of the second set: ").split())

if set_a.isdisjoint(set_b):
    print("The two sets are disjoint.")
else:
    print("The two sets are not disjoint.")
