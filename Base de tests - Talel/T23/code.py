def is_valid_date(day, month, year):
    """Check if a date is valid.

    Args:
        day (int): Day of the month.
        month (int): Month of the year.
        year (int): Year.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Check if date is valid
    if not (1 <= month <= 12):
        return False
    if year < 1:
        return False
    days_in_month = [31, 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 1 <= day <= days_in_month[month - 1]

def day_of_week(day, month, year):
    # Calculate day of week (0=Sunday, 6=Saturday)
    from datetime import datetime
    return datetime(year, month, day).weekday()

def days_between_dates(day1, month1, year1, day2, month2, year2):
    """Calculate days between two dates.

    Args:
        day1 (int): Day of first date.
        month1 (int): Month of first date.
        year1 (int): Year of first date.
        day2 (int): Day of second date.
        month2 (int): Month of second date.
        year2 (int): Year of second date.

    Returns:
        int: Absolute number of days between dates.
    """
    # Calculate absolute days between two dates
    from datetime import datetime
    d1 = datetime(year1, month1, day1)
    d2 = datetime(year2, month2, day2)
    return abs((d2 - d1).days)

def add_days(day, month, year, days):
    # Add days to a date
    from datetime import datetime, timedelta
    date = datetime(year, month, day) + timedelta(days=days)
    return date.day, date.month, date.year

def is_leap_year(year):
    # Check if year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_year(year):
    # Return number of days in a year
    return 366 if is_leap_year(year) else 365

def next_day(day, month, year):
    """Return the next day's date.

    Args:
        day (int): Current day.
        month (int): Current month.
        year (int): Current year.

    Returns:
        tuple: (day, month, year) of the next day.
    """
    # Calculate next day
    from datetime import datetime, timedelta
    date = datetime(year, month, day) + timedelta(days=1)
    return date.day, date.month, date.year

def is_weekend(day, month, year):
    # Check if date is a weekend
    return day_of_week(day, month, year) in [5, 6]

def month_name(month):
    # Return name of the month
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month - 1] if 1 <= month <= 12 else ""

def days_in_month(month, year):
    # Return number of days in a month
    days = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1] if 1 <= month <= 12 else 0