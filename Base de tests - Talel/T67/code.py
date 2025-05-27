def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    # Convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    # Convert meters to feet
    return meters * 3.28084

def feet_to_meters(feet):
    """Convert length from feet to meters.

    Args:
        feet (float): Length in feet.

    Returns:
        float: Length in meters.
    """
    # Convert feet to meters
    return feet / 3.28084

def kg_to_pounds(kg):
    # Convert kilograms to pounds
    return kg * 2.20462

def pounds_to_kg(pounds):
    # Convert pounds to kilograms
    return pounds / 2.20462

def km_to_miles(km):
    """Convert distance from kilometers to miles.

    Args:
        km (float): Distance in kilometers.

    Returns:
        float: Distance in miles.
    """
    # Convert kilometers to miles
    return km * 0.621371

def miles_to_km(miles):
    # Convert miles to kilometers
    return miles / 0.621371

def liters_to_gallons(liters):
    # Convert liters to gallons
    return liters * 0.264172

def gallons_to_liters(gallons):
    """Convert volume from gallons to liters.

    Args:
        gallons (float): Volume in gallons.

    Returns:
        float: Volume in liters.
    """
    # Convert gallons to liters
    return gallons / 0.264172