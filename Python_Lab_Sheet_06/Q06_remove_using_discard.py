"""Write a program to remove an element from a set using discard()."""

# Q6. Remove an element using discard()
# discard() does not raise an error if the element is absent.

my_set = set(input("Enter set elements separated by spaces: ").split())
element = input("Enter the element to discard: ")

my_set.discard(element)
print("Set after discard():", my_set)
