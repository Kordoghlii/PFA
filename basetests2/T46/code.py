# utils_math.py

def add(a, b):
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    # Simple addition of two values
    return a + b

def subtract(a, b):
    """
    Subtract one number from another.

    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.

    Returns:
        float: The result of a - b.
    """
    # Subtract b from a
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    # Basic multiplication
    return a * b

def divide(a, b):
    """
    Divide one number by another.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: The result of division.

    Raises:
        ValueError: If b is zero.
    """
    # Handle division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base, exponent):
    """
    Raise a number to the power of another.

    Args:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: base raised to the power of exponent.
    """
    # Exponential calculation
    return base ** exponent

def mod(a, b):
    """
    Get the modulus of two numbers.

    Args:
        a (int): Dividend.
        b (int): Divisor.

    Returns:
        int: Remainder of a divided by b.
    """
    # Use modulus operator
    return a % b

def is_even(n):
    """
    Check if a number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if even, False otherwise.
    """
    # A number is even if divisible by 2
    return n % 2 == 0

def is_odd(n):
    """
    Check if a number is odd.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if odd, False otherwise.
    """
    # A number is odd if not divisible by 2
    return n % 2 != 0

def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    # Factorial only defined for non-negative integers
    if n < 0:
        raise ValueError("Negative values not allowed.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def average(numbers):
    """
    Compute the average of a list of numbers.

    Args:
        numbers (list of float): List of numbers.

    Returns:
        float: The average value.

    Raises:
        ValueError: If the list is empty.
    """
    # Avoid division by zero for empty list
    if not numbers:
        raise ValueError("List cannot be empty.")
    return sum(numbers) / len(numbers)
