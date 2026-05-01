def seconds_to_minutes(seconds):
    """Calculate the square of a number.

    Args:
        seconds (int): Input number.

    Returns:
        int: The squared value.
    """
    # Convert seconds to minutes
    return seconds / 60

def minutes_to_hours(minutes):
    # Convert minutes to hours
    return minutes / 60

def hours_to_days(hours):
    # Convert hours to days
    return hours / 24

def add_time_hours(time_hours, hours):
    """Check if a string is a palindrome.

    Args:
        time_hours (float): Current time in hours.
        hours (float): Hours to add.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Add hours to time
    return time_hours + hours

def is_leap_year(year):
    # Check if year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    # Return number of days in a given month
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def seconds_to_hms(seconds):
    """Reverse a list.

    Args:
        seconds (int): Input list.

    Returns:
        list: Reversed list.
    """
    # Convert seconds to hours, minutes, seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return hours, minutes, secs

def time_difference_hours(t1, t2):
    # Calculate absolute time difference in hours
    return abs(t1 - t2)

def is_valid_hour(hour):
    # Check if hour is valid (0-23)
    return 0 <= hour <= 23

def format_time_24h(hours, minutes):
    # Format time in 24-hour format
    return f"{hours:02d}:{minutes:02d}"