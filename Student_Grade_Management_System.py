students = {}

while True:
    print("\n1. Add Student")
    print("2. View Student Grades")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")

        marks = float(input("Enter marks out of 100: "))

        if marks < 0 or marks > 100:
            print("Invalid marks!")
            continue

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"

        students[roll] = [name, marks, grade]

        print("Student added successfully!")

    elif choice == "2":
        for roll, data in students.items():
            print("\nRoll Number:", roll)
            print("Name:", data[0])
            print("Marks:", data[1])
            print("Grade:", data[2])

    elif choice == "3":
        roll = input("Enter roll number to search: ")

        if roll in students:
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
            print("Grade:", students[roll][2])
        else:
            print("Student not found!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")