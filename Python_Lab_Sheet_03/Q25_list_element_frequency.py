"""Question 25: Count the frequency of each element in a list."""

items = input("Enter list items separated by spaces: ").split()
checked = []

for item in items:
    if item not in checked:
        count = 0
        for value in items:
            if value == item:
                count += 1
        print(item + ":", count)
        checked.append(item)
