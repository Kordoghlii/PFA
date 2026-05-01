def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The sum of the two integers.
    """
    # Return the sum of a and b
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
    # Subtract b from a and return the result
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
    # Return the product of a and b
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
    # Check if division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    # Return result of division
    return a / b


def is_even(n: int) -> bool:
    """
    Checks whether a number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if even, False otherwise.
    """
    # Check if number is divisible by 2
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Computes the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the number.
    """
    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)


def fibonacci(n: int) -> list[int]:
    """
    Generates a Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of Fibonacci elements to generate.

    Returns:
        list[int]: A list of the first n Fibonacci numbers.
    """
    # Start with the first two Fibonacci numbers
    sequence = [0, 1]
    # Generate next numbers until we reach n elements
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    # Return only the first n elements
    return sequence[:n]


def reverse_string(s: str) -> str:
    """
    Reverses a given string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    # Use slicing to reverse the string
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Remove spaces and lowercase the string
    cleaned = s.lower().replace(" ", "")
    # Check if string is equal to its reverse
    return cleaned == cleaned[::-1]


def get_even_numbers(numbers: list[int]) -> list[int]:
    """
    Filters even numbers from a list.

    Args:
        numbers (list[int]): The list of integers.

    Returns:
        list[int]: A list of even integers.
    """
    # Return a new list containing only even numbers
    return [n for n in numbers if n % 2 == 0]


def average(numbers: list[float]) -> float:
    """
    Calculates the average of a list of floats.

    Args:
        numbers (list[float]): List of float numbers.

    Returns:
        float: The average value.
    """
    # If list is empty, return 0.0 to avoid division by zero
    if not numbers:
        return 0.0
    # Calculate sum and divide by number of elements
    return sum(numbers) / len(numbers)


def count_words(text: str) -> int:
    """
    Counts the number of words in a string.

    Args:
        text (str): The input text.

    Returns:
        int: The word count.
    """
    # Split the text by whitespace and count resulting words
    return len(text.split())


def capitalize_words(sentence: str) -> str:
    """
    Capitalizes the first letter of each word in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with each word capitalized.
    """
    # Capitalize each word using str.capitalize() in a loop
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
    # Iterate through list and add only new elements
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
    # Use unpacking to merge both dictionaries into a new one
    return {**d1, **d2}
