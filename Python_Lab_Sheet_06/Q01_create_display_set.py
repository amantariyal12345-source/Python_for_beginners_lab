"""Write a Python program to create and display a set."""

# Q1. Create and display a set
# split() reads space-separated values; set() stores only unique values.

elements = input("Enter elements separated by spaces: ").split()
my_set = set(elements)

print("Created set:", my_set)
