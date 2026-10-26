rooms = {}

while True:
    print("\n1. Book Room")
    print("2. View Bookings")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        room = input("Enter room number: ")

        if room not in rooms:
            name = input("Enter guest name: ")
            rooms[room] = name
            print("Room booked successfully!")
        else:
            print("Room already booked!")

    elif choice == "2":
        for room, name in rooms.items():
            print("Room:", room, "Guest:", name)

    elif choice == "3":
        break