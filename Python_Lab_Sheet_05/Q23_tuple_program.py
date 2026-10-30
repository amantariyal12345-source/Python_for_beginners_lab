"""
Question 23: Swap two tuples.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Swap two tuple variables
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
print("Before swapping:", tuple1, tuple2)
tuple1, tuple2 = tuple2, tuple1
print("After swapping:", tuple1, tuple2)
