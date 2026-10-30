"""
Question 6: Check if an element exists in a tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Check membership in a tuple
items = ("red", "green", "blue")
element = input("Enter a colour to search: ")
if element in items:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")
