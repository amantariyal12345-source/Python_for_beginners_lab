"""Write a program to perform all basic set operations (union, intersection, difference, symmetric difference) in one program."""

# Q30. Perform basic set operations on two sets

set_a = set(input("Enter elements of set A: ").split())
set_b = set(input("Enter elements of set B: ").split())

print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric difference (A ^ B):", set_a ^ set_b)
