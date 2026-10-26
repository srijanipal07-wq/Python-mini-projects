print("1. Kilometer to Meter")
print("2. Meter to Kilometer")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Enter choice: ")
value = float(input("Enter value: "))

if choice == "1":
    print("Result:", value * 1000, "meters")

elif choice == "2":
    print("Result:", value / 1000, "kilometers")

elif choice == "3":
    print("Result:", (value * 9 / 5) + 32, "Fahrenheit")

elif choice == "4":
    print("Result:", (value - 32) * 5 / 9, "Celsius")

else:
    print("Invalid choice")