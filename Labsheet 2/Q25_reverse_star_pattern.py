# Q25: Print the reverse star pattern
rows = int(input("Enter number of rows: "))

for row in range(rows, 0, -1):
    for column in range(row):
        print("*", end="")
    print()
