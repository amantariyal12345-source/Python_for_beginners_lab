# Question 4: Update a student's marks in the list (Update operation).
students = [
    {"roll_no": 101, "name": "Aarav", "age": 20, "marks": 85},
    {"roll_no": 102, "name": "Diya", "age": 19, "marks": 92},
]
try:
    roll_no = int(input("Enter roll number: "))
    new_marks = float(input("Enter new marks: "))
    for student in students:
        if student["roll_no"] == roll_no:
            student["marks"] = new_marks
            print("Marks updated:", student)
            break
    else:
        print("Student not found.")
except ValueError:
    print("Please enter a valid roll number and marks.")
