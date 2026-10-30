"""
Question 8: Find the index of an element in a tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Find the first index of an element
items = ("apple", "banana", "cherry", "banana")
element = input("Enter a fruit to find: ")
if element in items:
    print("Index:", items.index(element))
else:
    print("Element not found in the tuple.")
