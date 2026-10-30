"""Write a program to remove duplicates from a list using a set."""

# Q23. Remove duplicates from a list using a set
# Converting back to a list does not preserve the original order.

items = input("Enter list elements separated by spaces: ").split()
unique_items = list(set(items))

print("List after removing duplicates:", unique_items)
