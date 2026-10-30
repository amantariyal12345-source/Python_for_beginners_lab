"""Write a program to add a single element to a set."""

# Q3. Add a single element to a set

my_set = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to add: ")

my_set.add(element)
print("Set after adding the element:", my_set)
