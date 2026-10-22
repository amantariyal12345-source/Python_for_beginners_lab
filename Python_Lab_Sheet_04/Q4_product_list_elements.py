"""Question 4: Find the product of all elements in a list."""

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

product = 1
for number in numbers:
    product *= number

if numbers:
    print("Product:", product)
else:
    print("The list is empty; product is not calculated.")
