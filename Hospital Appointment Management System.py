appointments = []

while True:
    print("\n1. Book Appointment")
    print("2. View Appointments")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        patient = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter appointment date: ")

        appointments.append([patient, doctor, date])
        print("Appointment booked!")

    elif choice == "2":
        for a in appointments:
            print("Patient:", a[0])
            print("Doctor:", a[1])
            print("Date:", a[2])

    elif choice == "3":
        break