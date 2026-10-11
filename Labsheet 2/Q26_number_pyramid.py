# Q26: Print a pyramid pattern of numbers
rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for space in range(rows - row):
        print(" ", end="")

    for number in range(1, row + 1):
        print(number, end=" ")

    print()
