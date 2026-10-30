"""Write a program to count distinct elements from a list using a set."""

# Q21. Count distinct elements in a list using a set

items = input("Enter list elements separated by spaces: ").split()
distinct_items = set(items)

print("Distinct elements:", distinct_items)
print("Count of distinct elements:", len(distinct_items))
