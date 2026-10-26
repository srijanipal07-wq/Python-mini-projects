employees = []

while True:
    print("\n1. Add Employee")
    print("2. Search Employee")
    print("3. View All Employees")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = input("Enter salary: ")

        employees.append([emp_id, name, salary])
        print("Employee added!")

    elif choice == "2":
        emp_id = input("Enter employee ID to search: ")
        found = False

        for e in employees:
            if e[0] == emp_id:
                print("Name:", e[1])
                print("Salary:", e[2])
                found = True

        if not found:
            print("Employee not found")

    elif choice == "3":
        for e in employees:
            print(e)

    elif choice == "4":
        break