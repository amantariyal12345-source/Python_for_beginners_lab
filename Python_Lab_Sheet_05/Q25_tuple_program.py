"""
Question 25: Find the difference between two tuples.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Find elements present in the first tuple but not in the second
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 6)
difference = tuple(item for item in tuple1 if item not in tuple2)
print("Difference (tuple1 - tuple2):", tuple(dict.fromkeys(difference)))
