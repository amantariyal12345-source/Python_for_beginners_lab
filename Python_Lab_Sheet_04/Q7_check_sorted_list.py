"""Question 7: Check if a list is sorted or not."""

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
is_sorted = True

for index in range(len(numbers) - 1):
    if numbers[index] > numbers[index + 1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")
