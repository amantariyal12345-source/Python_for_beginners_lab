"""
Question 28: Find repeated items in a tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Find items that occur more than once
items = (10, 20, 10, 30, 20, 40, 10)
repeated = tuple(item for item in dict.fromkeys(items) if items.count(item) > 1)
print("Repeated items:", repeated)
