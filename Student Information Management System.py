students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        students[roll] = [name, marks]
        print("Student added!")

    elif choice == "2":
        for roll, data in students.items():
            print("Roll:", roll)
            print("Name:", data[0])
            print("Marks:", data[1])

    elif choice == "3":
        break