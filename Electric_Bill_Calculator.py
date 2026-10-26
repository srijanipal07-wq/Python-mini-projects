def calculate_electricity_bill(units):
    """Calculates electricity bill based on consumed units and slab rates."""
    service_charge = 500
    bill_amount = 0

    # Slab 1: 0 to 100 units
    if units <= 100:
        bill_amount = units * 1.0
    # Slab 2: 101 to 200 units
    elif units <= 200:
        bill_amount = (100 * 1.0) + ((units - 100) * 1.4)
    # Slab 3: 201 to 300 units
    elif units <= 300:
        bill_amount = (100 * 1.0) + (100 * 1.4) + ((units - 200) * 2.0)
    # Slab 4: Above 300 units
    else:
        bill_amount = (100 * 1.0) + (100 * 1.4) + (100 * 2.0) + ((units - 300) * 3.0)

    # Total bill including the mandatory service charge
    total_bill = bill_amount + service_charge
    return total_bill

def main():
    print("===== Electricity Bill Calculator =====")
    try:
         # Prompt for customer details first
        customer_name = input("Enter customer name: ")
        
         # Prompt for energy consumption
        units = int(input("Enter the number of consumed units: "))
        
        # Validation to prevent negative numbers
        if units < 0:
            print("Error! Consumed units cannot be a negative value.")
            return

        # Calculate final amount using your exact logic
        final_bill = calculate_electricity_bill(units)
        
        # Display the formatted receipt
        print("\n===== Electricity Bill Receipt =====")
        print(f"Customer Name: {customer_name}")
        print(f"Units Consumed: {units}")
        print(f"Total Amount Due (including service charge): Rs. {final_bill:.2f}")
    
    except ValueError:
        # Validation to prevent crashing on text inputs
        print("Error! Invalid input. Please enter a valid number.")

if __name__ == "__main__":
 main()

