patients = []

while True:
    print("\n1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        disease = input("Enter disease: ")

        patient = [name, age, disease]
        patients.append(patient)

        print("Patient added successfully!")

    elif choice == "2":
        for p in patients:
            print("Name:", p[0])
            print("Age:", p[1])
            print("Disease:", p[2])

    elif choice == "3":
        break

    else:
        print("Invalid choice")