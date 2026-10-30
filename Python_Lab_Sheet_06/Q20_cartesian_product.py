"""Write a program to find the Cartesian product of two sets."""

# Q20. Find the Cartesian product of two sets
# Each pair contains one element from A and one element from B.

set_a = set(input("Enter elements of set A: ").split())
set_b = set(input("Enter elements of set B: ").split())

cartesian_product = {(a, b) for a in set_a for b in set_b}
print("Cartesian product A x B:", cartesian_product)
