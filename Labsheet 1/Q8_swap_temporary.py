# Q8: Swap two variables using a temporary variable
a = input("Enter first value: ")
b = input("Enter second value: ")

temp = a
a = b
b = temp

print("After swapping:")
print("First value =", a)
print("Second value =", b)
