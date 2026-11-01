# Question 3: Search for a student by name in the list.
students = [
    {"roll_no": 101, "name": "Aarav", "age": 20, "marks": 85},
    {"roll_no": 102, "name": "Diya", "age": 19, "marks": 92},
]
search_name = input("Enter student name to search: ").strip()
matches = [student for student in students if student["name"].casefold() == search_name.casefold()]
if matches:
    for student in matches:
        print(student)
else:
    print("Student not found.")
