# Banking Management System
balance = 0

while True:
    print("\n--- BANKING MANAGEMENT SYSTEM ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Money deposited successfully!")
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount!")
        elif amount <= balance:
            balance = balance - amount
            print("Money withdrawn successfully!")
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice!")