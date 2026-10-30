"""Write a program to remove all elements of one set from another set."""

# Q18. Remove all elements of set B from set A
# difference_update() modifies set A in place.

set_a = set(input("Enter elements of set A: ").split())
set_b = set(input("Enter elements of set B to remove: ").split())

set_a.difference_update(set_b)
print("Set A after removing elements of set B:", set_a)
