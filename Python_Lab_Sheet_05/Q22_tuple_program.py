"""
Question 22: Flatten a nested tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Flatten a tuple containing tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
flat_tuple = tuple(item for group in nested_tuple for item in group)
print("Nested tuple:", nested_tuple)
print("Flattened tuple:", flat_tuple)
