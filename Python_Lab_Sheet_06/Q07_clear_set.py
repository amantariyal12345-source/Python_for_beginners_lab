"""Write a program to clear all elements from a set."""

# Q7. Clear all elements from a set

my_set = set(input("Enter set elements separated by spaces: ").split())
print("Original set:", my_set)

my_set.clear()
print("Set after clear():", my_set)
