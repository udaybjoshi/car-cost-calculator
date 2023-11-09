from src.car import create_car
from src.calculator import calculate_total_monthly_cost

def get_car_details():
    """
    Obtain car details from the user input.

    :return: Dictionary representing the car with inputted details.
    """
    make = input("Make: ")
    model = input("Model: ")
    mpg = float(input("Miles per gallon: "))
    weekly_miles_weekdays = float(input("Weekly miles on weekdays: "))
    weekly_miles_weekends = float(input("Weekly miles on weekends: "))
    return create_car(make, model, mpg, weekly_miles_weekdays, weekly_miles_weekends)

def main():
    """
    Main function to run the car cost calculator application.
    """
    print("Welcome to the Car Cost Calculator!")

    gas_price = float(input("Enter the current gas price per gallon: "))

    # Gather details for two cars
    print("\nEnter details for the first car:")
    car1 = get_car_details()
    purchase_price1 = float(input("Purchase price: "))
    down_payment1 = float(input("Down payment: "))
    interest_rate1 = float(input("Annual interest rate (in %): "))
    loan_term1 = int(input("Loan term (in years): "))
    maintenance_cost1 = float(input("Annual maintenance cost: "))

    # Calculate total monthly cost for the first car
    total_monthly_cost1 = calculate_total_monthly_cost(
        car1, purchase_price1, down_payment1, interest_rate1, loan_term1, maintenance_cost1, gas_price)

    # Repeat process for the second car...

    # Output results
    print(f"\nMonthly cost for the first car: ${total_monthly_cost1:.2f}")
    # Repeat output for the second car...

if __name__ == "__main__":
    main()
