"""Write a program to check if an element exists in a set."""

# Q8. Check whether an element exists in a set

my_set = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to search for: ")

if element in my_set:
    print(element, "exists in the set.")
else:
    print(element, "does not exist in the set.")
