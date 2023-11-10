def validate_car_data(mpg, price, interest_rate, loan_term, down_payment):
    """
    Validate the provided car data parameters.

    Checks if the given parameters for a car are within acceptable ranges and raises
    ValueError with an appropriate message if any parameter is invalid.

    :param mpg: A float representing the miles per gallon of the car. Must be greater than zero.
    :param price: A float representing the purchase price of the car. Must be greater than zero.
    :param interest_rate: A float representing the loan interest rate as a fraction (e.g., 0.05 for 5%). Must be between 0 and 1 (exclusive).
    :param loan_term: An integer representing the loan term in years. Must be greater than zero.
    :param down_payment: A float representing the down payment amount on the car. Cannot be negative.
    :raises ValueError: If any of the parameters are out of their valid range.
    """
    if mpg <= 0:
        raise ValueError("MPG must be greater than zero.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    if not (0 < interest_rate < 1):
        raise ValueError("Interest rate must be a percentage between 0 and 1.")
    if loan_term <= 0:
        raise ValueError("Loan term must be greater than zero.")
    if down_payment < 0:
        raise ValueError("Down payment cannot be negative.")

def create_car(make, model, mpg, weekly_miles_weekdays, weekly_miles_weekends):
    """
    Create and return a car dictionary with the provided specifications.

    :param make: String representing the make of the car.
    :param model: String representing the model of the car.
    :param mpg: Float representing the miles per gallon efficiency of the car.
    :param weekly_miles_weekdays: Float representing the miles driven on weekdays.
    :param weekly_miles_weekends: Float representing the miles driven on weekends.
    :return: Dictionary representing the car.
    """
    return {
        'make': make,
        'model': model,
        'mpg': mpg,
        'weekly_miles_weekdays': weekly_miles_weekdays,
        'weekly_miles_weekends': weekly_miles_weekends
    }
