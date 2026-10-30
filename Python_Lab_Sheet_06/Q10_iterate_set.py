"""Write a program to iterate through a set and print its elements."""

# Q10. Iterate through a set and print its elements
# Set elements are unordered, so their display order may vary.

my_set = set(input("Enter set elements separated by spaces: ").split())

print("Elements of the set:")
for element in my_set:
    print(element)
