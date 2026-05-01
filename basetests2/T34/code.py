"""
Module for basic math operations with unit tests.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
    
    Returns:
        float: Sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
    
    Returns:
        float: Result of a - b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a (float): First number.
        b (float): Second number.
    
    Returns:
        float: Product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide two numbers.
    
    Args:
        a (float): Numerator.
        b (float): Denominator (must be non-zero).
    
    Returns:
        float: Result of a / b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base: float, exponent: float) -> float:
    """
    Compute the power of a number.
    
    Args:
        base (float): Base number.
        exponent (float): Exponent.
    
    Returns:
        float: base raised to the exponent.
    """
    return base ** exponent

def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer.
    
    Returns:
        int: Factorial of n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check.
    
    Returns:
        bool: True if prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two numbers.
    
    Args:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        int: GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Compute the least common multiple of two numbers.
    
    Args:
        a (int): First number.
        b (int): Second number.
    
    Returns:
        int: LCM of a and b.
    """
    return a * b // gcd(a, b)

def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number.
    
    Args:
        n (int): Index in the Fibonacci sequence.
    
    Returns:
        int: nth Fibonacci number.
    """
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b