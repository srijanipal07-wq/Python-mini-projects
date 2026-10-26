import math

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")

    elif choice == "5":
        a = float(input("Enter number: "))

        if a >= 0:
            print("Square Root:", math.sqrt(a))
        else:
            print("Enter a non-negative number")

    elif choice == "6":
        break