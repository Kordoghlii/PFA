# utils.py

def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Parameters:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    # Effectue l'addition de deux nombres
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a and return the result.

    Parameters:
        a (float): First number
        b (float): Number to subtract from a

    Returns:
        float: Result of a - b
    """
    # Effectue la soustraction
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the product.

    Parameters:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of a and b
    """
    # Effectue la multiplication
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b and return the result.

    Parameters:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: Result of division

    Raises:
        ZeroDivisionError: If b is zero
    """
    # Vérifie que le dénominateur n'est pas nul
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    # Effectue la division
    return a / b


def is_even(n: int) -> bool:
    """
    Check if a number is even.

    Parameters:
        n (int): Integer to check

    Returns:
        bool: True if n is even, False otherwise
    """
    # Un nombre est pair si le reste de la division par 2 est nul
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """
    Check if a number is odd.

    This works correctly for both positive and negative integers.
    An integer is odd if it is not divisible evenly by 2.

    Parameters:
        n (int): Integer to check

    Returns:
        bool: True if n is odd, False otherwise
    """
    # Un nombre est impair s'il n'est pas divisible par 2
    return n % 2 != 0


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using iteration.

    Parameters:
        n (int): Non-negative integer

    Returns:
        int: n factorial

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    # Multiplie tous les entiers de 2 à n
    for i in range(2, n + 1):
        result *= i
    return result


def power(base: float, exponent: int) -> float:
    """
    Raise a number to a power.

    Parameters:
        base (float): The base number
        exponent (int): The exponent

    Returns:
        float: base raised to the power of exponent
    """
    # Utilise l'opérateur **
    return base ** exponent


def maximum(a: float, b: float) -> float:
    """
    Return the greater of two numbers.

    Parameters:
        a (float): First number
        b (float): Second number

    Returns:
        float: The larger number
    """
    # Compare a et b et retourne le plus grand
    return a if a > b else b


def minimum(a: float, b: float) -> float:
    """
    Return the smaller of two numbers.

    Parameters:
        a (float): First number
        b (float): Second number

    Returns:
        float: The smaller number
    """
    # Compare a et b et retourne le plus petit
    return a if a < b else b


def average(numbers: list[float]) -> float:
    """
    Calculate the average (mean) of a list of numbers.

    Parameters:
        numbers (list): List of floats or ints

    Returns:
        float: The mean value

    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("List is empty.")
    
    # Somme des éléments divisée par la taille de la liste
    return sum(numbers) / len(numbers)


def count_occurrences(lst: list, item) -> int:
    """
    Count how many times an item appears in a list.

    Parameters:
        lst (list): The list to search
        item (any): The item to count

    Returns:
        int: Number of occurrences of item
    """
    # Utilise la méthode .count() de Python
    return lst.count(item)


def reverse_list(lst: list) -> list:
    """
    Return the reversed version of a list.

    Parameters:
        lst (list): The list to reverse

    Returns:
        list: Reversed list
    """
    # Utilise le slicing pour inverser la liste
    return lst[::-1]


def is_palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome (reads the same forward and backward).

    Parameters:
        word (str): The word to check

    Returns:
        bool: True if palindrome, False otherwise
    """
    # On ignore la casse et les espaces
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def capitalize_words(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a sentence.

    Parameters:
        sentence (str): A sentence string

    Returns:
        str: The capitalized sentence
    """
    # Utilise str.capitalize() sur chaque mot
    return " ".join(word.capitalize() for word in sentence.split())
