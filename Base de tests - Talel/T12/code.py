def is_multiple(n, divisor):
    """Check if n is a multiple of divisor.

    Args:
        n (int): The number to check.
        divisor (int): The divisor.

    Returns:
        bool: True if n is a multiple of divisor, False otherwise.
    """
    return n % divisor == 0

def round_number(num, decimals):
    return round(num, decimals)

def absolute_difference(a, b):
    # Calculate absolute difference between two numbers
    return abs(a - b)

def to_binary(n):
    """Convert a number to binary string.

    Args:
        n (int): The number to convert.

    Returns:
        str: The binary representation.
    """
    return bin(n)[2:]

def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n

def sum_of_squares(n):
    # Sum of squares from 1 to n
    return sum(i * i for i in range(1, n + 1))

def is_power_of_two(n):
    """Check if a number is a power of two.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a power of two, False otherwise.
    """
    return n > 0 and (n & (n - 1)) == 0

def next_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    n += 1
    while not is_prime(n):
        n += 1
    return n

def digit_count(n):
    return len(str(abs(n)))

def clamp(num, min_val, max_val):
    """Clamp a number between min_val and max_val.

    Args:
        num (float): The number to clamp.
        min_val (float): The minimum value.
        max_val (float): The maximum value.

    Returns:
        float: The clamped number.
    """
    return max(min_val, min(num, max_val))