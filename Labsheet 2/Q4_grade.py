# Q4: Display grade based on marks
marks = float(input("Enter marks (0-100): "))

if 90 <= marks <= 100:
    grade = "A"
elif 75 <= marks < 90:
    grade = "B"
elif 50 <= marks < 75:
    grade = "C"
elif 0 <= marks < 50:
    grade = "F"
else:
    grade = "Invalid marks"

print("Grade =", grade)
