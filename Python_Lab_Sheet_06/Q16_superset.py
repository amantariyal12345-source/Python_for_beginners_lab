"""Write a program to check if a set is a superset of another set."""

# Q16. Check whether the first set is a superset of the second set

set_a = set(input("Enter elements of the first set: ").split())
set_b = set(input("Enter elements of the second set: ").split())

if set_a.issuperset(set_b):
    print("The first set is a superset of the second set.")
else:
    print("The first set is not a superset of the second set.")
