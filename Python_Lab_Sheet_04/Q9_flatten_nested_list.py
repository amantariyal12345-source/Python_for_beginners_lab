"""Question 9: Flatten a nested list."""

# Enter a simple nested list, for example: [[1, 2], [3, 4], [5]]
nested = eval(input("Enter a nested list (example [[1, 2], [3, 4]]): "))
flat = []

for sublist in nested:
    if isinstance(sublist, list):
        for item in sublist:
            flat.append(item)
    else:
        flat.append(sublist)

print("Flattened list:", flat)
