# Question 6: Implement CRUD operations on a dictionary of employee data.
employees = {}

def add_employee():
    employee_id = input("Employee ID: ").strip()
    if employee_id in employees:
        print("Employee ID already exists.")
        return
    employees[employee_id] = {
        "name": input("Employee name: ").strip(),
        "department": input("Department: ").strip(),
        "salary": input("Salary: ").strip(),
    }
    print("Employee added.")

def view_employees():
    if not employees:
        print("No employee records.")
    for employee_id, details in employees.items():
        print(employee_id, details)

def update_employee():
    employee_id = input("Employee ID to update: ").strip()
    if employee_id not in employees:
        print("Employee not found.")
        return
    employees[employee_id]["name"] = input("New name: ").strip()
    employees[employee_id]["department"] = input("New department: ").strip()
    employees[employee_id]["salary"] = input("New salary: ").strip()
    print("Employee updated.")

def delete_employee():
    employee_id = input("Employee ID to delete: ").strip()
    if employees.pop(employee_id, None) is None:
        print("Employee not found.")
    else:
        print("Employee deleted.")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
    except (ValueError, KeyError) as error:
        print("Operation failed:", error)
