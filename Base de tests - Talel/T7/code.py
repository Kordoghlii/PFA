import math

def square(num):
    """Calculate the square of a number.

    Args:
        num (int or float): The number to square.

    Returns:
        int or float: The square of the input number.
    """
    return num * num

def cube(num):
    return num ** 3

def is_even(num):
    # Check if number is divisible by 2
    return num % 2 == 0

def factorial(n):
    """Calculate factorial of a non-negative integer.

    Args:
        n (int): The number to compute factorial for.

    Returns:
        int or None: The factorial of n, or None if n is negative.
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate the least common multiple of two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The LCM of a and b.
    """
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sum_digits(n):
    # Sum all digits in a number
    return sum(int(d) for d in str(abs(n)))

def power(base, exp):
    """Raise base to the power of exp.

    Args:
        base (int or float): The base number.
        exp (int): The exponent.

    Returns:
        int or float: The result of base raised to exp.
    """
    return base ** exp