# Q9: Swap two variables without a temporary variable
a = input("Enter first value: ")
b = input("Enter second value: ")

a, b = b, a

print("After swapping:")
print("First value =", a)
print("Second value =", b)
