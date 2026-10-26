cart = []
total = 0

while True:
    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))

        if price > 0:
            cart.append([name, price])
            print("Product added!")
        else:
            print("Invalid price")

    elif choice == "2":
        total = 0

        for item in cart:
            print(item[0], "-", item[1])
            total += item[1]

        print("Total Price:", total)

    elif choice == "3":
        total = 0

        for item in cart:
            total += item[1]

        print("Final Bill:", total)
        print("Thank you for shopping!")

    elif choice == "4":
        break