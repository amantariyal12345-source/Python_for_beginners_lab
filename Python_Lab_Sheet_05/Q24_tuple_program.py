"""
Question 24: Find common elements between two tuples.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Find common elements while preserving order from the first tuple
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
common = tuple(item for item in tuple1 if item in tuple2)
print("Common elements:", tuple(dict.fromkeys(common)))
