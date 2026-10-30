"""
Question 19: Remove duplicate elements from a tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Remove duplicates while preserving their original order
items = (10, 20, 10, 30, 20, 40, 30)
unique_items = tuple(dict.fromkeys(items))
print("Original tuple:", items)
print("Tuple without duplicates:", unique_items)
