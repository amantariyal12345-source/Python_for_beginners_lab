"""
Question 29: Check if all elements in a tuple are the same.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Check whether every element matches the first element
items = (5, 5, 5, 5)
if len(items) > 0 and all(item == items[0] for item in items):
    print("All elements are the same.")
else:
    print("All elements are not the same.")
