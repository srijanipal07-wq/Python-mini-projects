# Inventory Management System
# Using Dictionary and CRUD Operations

inventory = {}

while True:
    print("\n----- INVENTORY MANAGEMENT SYSTEM -----")
    print("1. Create / Add Product")
    print("2. Read / View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # CREATE
    if choice == "1":
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Quantity: "))

        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully!")

    # READ
    elif choice == "2":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("\n----- PRODUCT LIST -----")

            for product_id, product in inventory.items():
                print("Product ID:", product_id)
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
                print("-----------------------")

    # UPDATE
    elif choice == "3":
        product_id = input("Enter Product ID to update: ")

        if product_id in inventory:
            price = float(input("Enter New Price: "))
            quantity = int(input("Enter New Quantity: "))

            inventory[product_id]["price"] = price
            inventory[product_id]["quantity"] = quantity

            print("Product updated successfully!")
        else:
            print("Product not found.")

    # DELETE
    elif choice == "4":
        product_id = input("Enter Product ID to delete: ")

        if product_id in inventory:
            del inventory[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    # EXIT
    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")