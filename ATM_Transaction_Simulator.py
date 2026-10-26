# ATM Transaction Simulator (Basic Version)

# 1. Initial Data Setup (Account Number, PIN, and Balance)
account_number = "12345"
account_pin = "1111"
balance = 5000.0  # Initial account balance is 5000.00

print("=== Welcome to the Python ATM Simulator ===")

# 2. Login System (User Validation)
input_acc = input("Enter your 5-digit Account Number: ")
input_pin = input("Enter your 4-digit PIN: ")

# Check if the entered account number and PIN match our data
if input_acc == account_number and input_pin == account_pin:
    print("\n Login Successful!")
    
    # 3. Main ATM Menu (Runs repeatedly using a loop)
    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            # Logic to check and display balance
            print(f" Your current balance is: ${balance:.2f}")
            
        elif choice == "2":
            # Logic to deposit money
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                balance += amount  # Adds money to the current balance
                print(f" Successfully deposited ${amount:.2f}")
            else:
                print(" Invalid amount! Please enter a valid number.")
                
        elif choice == "3":
            # Logic to withdraw money
            amount = float(input("Enter the amount to withdraw: $"))
            if 0 < amount <= balance:
                balance -= amount  # Subtracts money from the current balance
                print(f" Successfully withdrew ${amount:.2f}")
            elif amount > balance:
                print(" Transaction Failed! Insufficient funds.")
            else:
                print(" Invalid amount! Please enter a valid number.")
                
        elif choice == "4":
            # Logic to break the loop and close the program
            print(" Thank you for using our ATM. Goodbye!")
            break
            
        else:
            print(" Invalid option! Please choose between 1 and 4.")

else:
    print("\n Invalid Account Number or PIN! Please try again.")