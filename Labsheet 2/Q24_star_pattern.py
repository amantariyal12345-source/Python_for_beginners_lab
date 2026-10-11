# Q24: Print the given star pattern
rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for column in range(row):
        print("*", end="")
    print()
