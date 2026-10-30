"""Write a program to add multiple elements to a set."""

# Q4. Add multiple elements to a set

my_set = set(input("Enter initial set elements separated by spaces: ").split())
new_elements = input("Enter multiple elements to add, separated by spaces: ").split()

my_set.update(new_elements)
print("Set after adding multiple elements:", my_set)
