def calculate_gas_cost(car, gas_price):
    """
    Calculate the monthly gas cost for a car.

    :param car: Dictionary containing car specifications.
    :param gas_price: Float representing the current price of gas per gallon.
    :return: Float representing the monthly gas cost for the car.
    """
    monthly_miles = car['weekly_miles_weekdays'] * 5 + car['weekly_miles_weekends'] * 2
    monthly_gas_cost = (monthly_miles / car['mpg']) * gas_price
    return monthly_gas_cost

def calculate_loan_payment(purchase_price, down_payment, annual_interest_rate, loan_term):
    """
    Calculate the monthly loan payment for a car.

    :param purchase_price: Float representing the purchase price of the car.
    :param down_payment: Float representing the down payment made on the car.
    :param annual_interest_rate: Float representing the annual interest rate of the loan.
    :param loan_term: Integer representing the loan term in years.
    :return: Float representing the monthly loan payment.
    """
    monthly_interest_rate = annual_interest_rate / 12 / 100
    loan_amount = purchase_price - down_payment
    monthly_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_term * 12)))
    return monthly_payment

def calculate_total_monthly_cost(car, purchase_price, down_payment, annual_interest_rate, loan_term, maintenance_cost, gas_price):
    """
    Calculate the total monthly cost of owning a car including loan payment, gas, and maintenance.

    :param car: Dictionary containing car specifications.
    :param purchase_price: Float representing the purchase price of the car.
    :param down_payment: Float representing the down payment on the car.
    :param annual_interest_rate: Float representing the annual interest rate of the loan.
    :param loan_term: Integer representing the loan term in years.
    :param maintenance_cost: Float representing the annual maintenance cost of the car.
    :param gas_price: Float representing the current price of gas per gallon.
    :return: Float representing the total monthly cost of the car.
    """
    loan_payment = calculate_loan_payment(purchase_price, down_payment, annual_interest_rate, loan_term)
    gas_cost = calculate_gas_cost(car, gas_price)
    monthly_maintenance_cost = maintenance_cost / 12
    total_cost = loan_payment + gas_cost + monthly_maintenance_cost
    return total_cost
