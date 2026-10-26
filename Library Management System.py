books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")

        books.append([name, "Available"])
        print("Book added successfully!")

    elif choice == "2":
        for book in books:
            print("Book:", book[0], "| Status:", book[1])

    elif choice == "3":
        name = input("Enter book name to issue: ")
        found = False

        for book in books:
            if book[0].lower() == name.lower():
                found = True

                if book[1] == "Available":
                    book[1] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")

                break

        if not found:
            print("Book not found!")

    elif choice == "4":
        name = input("Enter book name to return: ")
        found = False

        for book in books:
            if book[0].lower() == name.lower():
                found = True

                if book[1] == "Issued":
                    book[1] = "Available"
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")

                break

        if not found:
            print("Book not found!")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")