while True:
    name = input("Enter employee name: ")

    salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))
    deduction = float(input("Enter deduction: "))

    total = salary + bonus - deduction

    print("Employee:", name)
    print("Basic Salary:", salary)
    print("Net Salary:", total)

    choice = input("Continue? (yes/no): ")

    if choice == "no":
        break