def create_car(make, model, mpg, weekly_miles_weekdays, weekly_miles_weekends):
    """Create and return a car dictionary with the provided parameters.
    
    Args:
        make (str): String representing the make of the car.
        model (str): String representing the model of the car.
        mpg (float): Float representing the miles per gallon of the car.
        weekly_miles_weekdays (float): Float representing the miles driven on weekdays.
        weekly_miles_weekends (float): Float representing the miles driven on weekends.
        return: Dictionary representing the car.
    """
    return {
        'make': make,
        'model': model,
        'mpg': mpg,
        'weekly_miles_weekdays': weekly_miles_weekdays,
        'weekly_miles_weekends': weekly_miles_weekends
    }