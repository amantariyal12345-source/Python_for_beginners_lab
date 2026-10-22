"""Question 12: Find the maximum and minimum marks from a dictionary."""

marks = {}
count = int(input("How many students? "))

for index in range(count):
    name = input("Enter student name: ")
    score = float(input("Enter marks: "))
    marks[name] = score

if not marks:
    print("No marks entered.")
else:
    names = list(marks.keys())
    highest_name = names[0]
    lowest_name = names[0]

    for name in names:
        if marks[name] > marks[highest_name]:
            highest_name = name
        if marks[name] < marks[lowest_name]:
            lowest_name = name

    print("Maximum marks:", marks[highest_name], "by", highest_name)
    print("Minimum marks:", marks[lowest_name], "by", lowest_name)
