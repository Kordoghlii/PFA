def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first.

    Args:
        a (int): The number to subtract from.
        b (int): The number to subtract.

    Returns:
        int: The result of the subtraction.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two floating-point numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of the two numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def is_even(n: int) -> bool:
    """
    Checks whether a number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if even, False otherwise.
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> list[int]:
    """
    Generates a Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of Fibonacci elements to generate.

    Returns:
        list[int]: A list of the first n Fibonacci numbers.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


def reverse_string(s: str) -> str:
    """
    Reverses a given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filters even numbers from a list.

    Args:
        numbers (list[int]): The list of integers.

    Returns:
        list[int]: A list of even integers.
    """
    return [n for n in numbers if n % 2 == 0]


def average(numbers: list[float]) -> float:
    """
    Calculates the average of a list of floats.

    Args:
        numbers (list[float]): List of float numbers.

    Returns:
        float: The average value.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def count_words(text: str) -> int:
    """
    Counts the number of words in a string.

    Args:
        text (str): The input text.

    Returns:
        int: The word count.
    """
    return len(text.split())


def capitalize_words(sentence: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with each word capitalized.
    """
    return " ".join(word.capitalize() for word in sentence.split())


def remove_duplicates(items: list[int]) -> list[int]:
    """
    Removes duplicate values from a list.

    Args:
        items (list[int]): The list with potential duplicates.

    Returns:
        list[int]: A list with duplicates removed, original order preserved.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def merge_dicts(d1: dict, d2: dict) -> dict:
    """
    Merges two dictionaries.

    Args:
        d1 (dict): The first dictionary.
        d2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing all key-value pairs.
    """
    return {**d1, **d2}
