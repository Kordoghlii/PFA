def simple_interest(principal, rate, time):
    """Calculate the square of a number.

    Args:
        principal (float): The principal amount.
        rate (float): Annual interest rate (as a decimal).
        time (float): Time in years.

    Returns:
        float: The squared value.
    """
    # Calculate simple interest
    return principal * rate * time

def compound_interest(principal, rate, time, compounds_per_year):
    """Check if a string is a palindrome.

    Args:
        principal (float): The principal amount.
        rate (float): Annual interest rate (as a decimal).
        time (float): Time in years.
        compounds_per_year (int): Number of times interest is compounded per year.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)

def future_value(present_value, rate, time):
    """Reverse a list.

    Args:
        present_value (float): Present value.
        rate (float): Annual interest rate (as a decimal).
        time (float): Time in years.

    Returns:
        list: Reversed list.
    """
    return present_value * (1 + rate) ** time

def present_value(future_value, rate, time):
    """Count vowels in a string.

    Args:
        future_value (float): Future value.
        rate (float): Annual discount rate (as a decimal).
        time (float): Time in years.

    Returns:
        int: Number of vowels.
    """
    return future_value / (1 + rate) ** time

def loan_payment(principal, rate, time):
    """Find maximum in a list.

    Args:
        principal (float): Loan amount.
        rate (float): Monthly interest rate (as a decimal).
        time (float): Loan term in months.

    Returns:
        float: Maximum value.
    """
    # Calculate monthly loan payment
    if rate == 0:
        return principal / time
    return principal * rate / (1 - (1 + rate) ** -time)

def annual_percentage_yield(nominal_rate, compounds_per_year):
    """Convert string to uppercase.

    Args:
        nominal_rate (float): Nominal interest rate (as a decimal).
        compounds_per_year (int): Number of compounding periods per year.

    Returns:
        str: Uppercase string.
    """
    return (1 + nominal_rate / compounds_per_year) ** compounds_per_year - 1

def net_present_value(cash_flows, rate):
    """Calculate factorial of a number.

    Args:
        cash_flows (list): List of cash flows.
        rate (float): Discount rate (as a decimal).

    Returns:
        int: Factorial result.
    """
    # Calculate net present value
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))

def return_on_investment(initial, final):
    """Split a string into words.

    Args:
        initial (float): Initial investment.
        final (float): Final value.

    Returns:
        list: List of words.
    """
    return (final - initial) / initial if initial != 0 else 0

def amortize_payment(principal, rate, periods):
    """Check if a number is prime.

    Args:
        principal (float): Loan amount.
        rate (float): Monthly interest rate (as a decimal).
        periods (int): Number of payment periods.

    Returns:
        bool: True if prime, False otherwise.
    """
    # Calculate fixed amortization payment
    if rate == 0:
        return principal / periods
    return principal * rate * (1 + rate) ** periods / ((1 + rate) ** periods - 1)

def savings_goal(principal, target, rate, time):
    """Calculate the sum of a list.

    Args:
        principal (float): Initial amount.
        target (float): Target amount.
        rate (float): Annual interest rate (as a decimal).
        time (float): Time in years.

    Returns:
        float: Sum of the list.
    """
    # Calculate savings goal achievement
    return target <= principal * (1 + rate) ** time