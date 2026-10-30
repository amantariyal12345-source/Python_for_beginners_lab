"""Write a program to create a frozen set and demonstrate its properties."""

# Q28. Create a frozenset and demonstrate its properties
# A frozenset is an immutable set, so its elements cannot be added or removed.

items = input("Enter elements separated by spaces: ").split()
frozen = frozenset(items)

print("Frozenset:", frozen)
print("Number of elements:", len(frozen))
print("Is 'Python' present?", "Python" in frozen)

# Frozensets support set operations.
other = frozenset(input("Enter another group of elements: ").split())
print("Union:", frozen | other)
print("Intersection:", frozen & other)
