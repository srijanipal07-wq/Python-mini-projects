while True:
    name = input("\nEnter employee name: ")

    basic_salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))
    deduction = float(input("Enter deduction: "))

    net_salary = basic_salary + bonus - deduction

    print("\n--- Salary Details ---")
    print("Employee Name:", name)
    print("Basic Salary:", basic_salary)
    print("Bonus:", bonus)
    print("Deduction:", deduction)
    print("Net Salary:", net_salary)

    choice = input("\nContinue? (yes/no): ")

    if choice.lower() == "no":
        break