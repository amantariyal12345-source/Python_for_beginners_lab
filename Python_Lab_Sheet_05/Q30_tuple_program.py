"""
Question 30: Find the element-wise sum of two tuples.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Add elements at matching positions
tuple1 = (10, 20, 30, 40)
tuple2 = (1, 2, 3, 4)
if len(tuple1) == len(tuple2):
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    print("Element-wise sum:", result)
else:
    print("Both tuples must have the same length.")
