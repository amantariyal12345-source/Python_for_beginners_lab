# Question 9: Save student data into a text file and read it back.
students = [
    {"roll_no": 101, "name": "Aarav", "age": 20, "marks": 85},
    {"roll_no": 102, "name": "Diya", "age": 19, "marks": 92},
]
try:
    with open("students.txt", "w", encoding="utf-8") as file:
        for student in students:
            file.write(
                f'{student["roll_no"]},{student["name"]},{student["age"]},{student["marks"]}\n'
            )
    print("Student data saved to students.txt.")

    with open("students.txt", "r", encoding="utf-8") as file:
        print("Reading student data:")
        for line in file:
            print(line.rstrip())
except OSError as error:
    print("File error:", error)
