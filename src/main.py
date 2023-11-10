from src.car import create_car
from src.calculator import calculate_total_monthly_cost

def prompt_for_float(message):
    """
    Prompt the user for a float number input. 
    
    This function repeatly prompts the user to enter a value until they provide a valid float number.
    If a non-numeric input is given, it catches the ValueError and prompts the user again.

    :param message: A string that is displayed to the user as a prompt.
    :returns: A float number representing the user's input/
       """
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")

def prompt_for_int(message):
    """
    Prompt the user for an integer input.

    This function continuously prompts the user to enter a value until a valid integer is provided. 
    It handles the case where the user enters non-integer values by catching a ValueError and 
    requesting the user to input the data again.

    :param message: A string to be displayed to the user, prompting for input.
    :return: An integer representing the user's input.
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid integer.")

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
    
    print("\nEnter details for the second car:")
    car2 = get_car_details()
    purchase_price2 = float(input("Purchase price: "))
    down_payment2 = float(input("Down payment: "))
    interest_rate2 = float(input("Annual interest rate (in %): "))
    loan_term2 = int(input("Loan term (in years): "))
    maintenance_cost2 = float(input("Annual maintenance cost: "))

    # Calculate total monthly cost for the first car
    total_monthly_cost1 = calculate_total_monthly_cost(
        car1, purchase_price1, down_payment1, interest_rate1, loan_term1, maintenance_cost1, gas_price)

    # Calculate total monthly cost for the second car
    total_monthly_cost2 = calculate_total_monthly_cost(
        car2, purchase_price2, down_payment2, interest_rate2, loan_term2, maintenance_cost2, gas_price)


    # Output results
    print(f"\nMonthly cost for the first car: ${total_monthly_cost1:.2f}")
    print(f"\nMonthly cost for the second car: ${total_monthly_cost2:.2f}")
   
if __name__ == "__main__":
    main()
