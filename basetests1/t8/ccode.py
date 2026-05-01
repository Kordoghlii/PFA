def add_numbers(a: int, b: int) -> int:
    #Adding numbers
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two input integers.
    """
    return a + b


def is_prime(n: int) -> bool:
    """
    Determines if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    # Check divisibility from 2 up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    # Recursively compute factorial
    return n * factorial(n - 1)


def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    # Use slicing to reverse the string
    return s[::-1]


def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filters even numbers from a list of integers.

    Args:
        numbers (list[int]): The list of integers to filter.

    Returns:
        list[int]: A list containing only the even numbers from the input.
    """
    # Use list comprehension to select even numbers
    return [num for num in numbers if num % 2 == 0]
