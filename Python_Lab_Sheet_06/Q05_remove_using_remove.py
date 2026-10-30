"""Write a program to remove an element from a set using remove()."""

# Q5. Remove an element using remove()
# remove() raises KeyError if the element is not present.

my_set = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to remove: ")

try:
    my_set.remove(element)
    print("Set after removal:", my_set)
except KeyError:
    print("Element was not found in the set.")
