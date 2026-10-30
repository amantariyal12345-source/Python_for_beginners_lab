"""Write a program to find maximum and minimum values in a set."""

# Q29. Find maximum and minimum values in a set
# Input values are converted to integers for numeric comparison.

try:
    numbers = {int(value) for value in input("Enter integers separated by spaces: ").split()}

    if numbers:
        print("Set:", numbers)
        print("Maximum value:", max(numbers))
        print("Minimum value:", min(numbers))
    else:
        print("The set is empty.")
except ValueError:
    print("Please enter valid integers only.")
