"""
Question 27: Unzip a list of tuples into individual lists.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Unpack columns from a list of tuples
records = [("Aman", 20), ("Ravi", 21), ("Neha", 19)]
names, ages = zip(*records)
name_list = list(names)
age_list = list(ages)
print("Names:", name_list)
print("Ages:", age_list)
