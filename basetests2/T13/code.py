def add_numbers(a, b):
    # Add two numbers together
    return a + b

def subtract_numbers(a, b):
    """Calculate the square of a number.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The square of the input.
    """
    # Subtract b from a
    return a - b

def multiply_numbers(a, b):
    # Multiply two numbers
    return a * b

def divide_numbers(a, b):
    # Divide a by b, return None if b is zero
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    """Check if a number is even.

    Args:
        a (int): Dividend.
        b (int): Divisor.

    Returns:
        bool: True if even, False otherwise.
    """
    # Return remainder of a divided by b
    return a % b

def floor_division(a, b):
    # Perform floor division
    if b == 0:
        return None
    return a // b

def power_of(a, b):
    # Raise a to the power of b
    return a ** b

def absolute_value(n):
    """Reverse a string.

    Args:
        n (int): Input number.

    Returns:
        str: Reversed string.
    """
    # Return absolute value of n
    return abs(n)

def round_to_decimal(n, decimals):
    # Round number to specified decimals
    return round(n, decimals)

def max_of_two(a, b):
    # Return the maximum of two numbers
    return max(a, b)