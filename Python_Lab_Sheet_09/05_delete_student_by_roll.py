# Question 5: Delete a student record by roll number (Delete operation).
students = [
    {"roll_no": 101, "name": "Aarav", "age": 20, "marks": 85},
    {"roll_no": 102, "name": "Diya", "age": 19, "marks": 92},
]
try:
    roll_no = int(input("Enter roll number to delete: "))
    original_count = len(students)
    students = [student for student in students if student["roll_no"] != roll_no]
    print("Student deleted." if len(students) < original_count else "Student not found.")
    print("Remaining records:", students)
except ValueError:
    print("Please enter a valid roll number.")
