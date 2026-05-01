def add_numbers(a: float, b: float) -> float:
    """Additionne deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La somme des deux nombres.
    """
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """Soustrait deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La différence entre les deux nombres.
    """
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """Multiplie deux nombres.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: Le produit des deux nombres.
    """
    return a * b

def divide_numbers(a: float, b: float) -> float:
    """Divise deux nombres.

    Args:
        a (float): Dividende.
        b (float): Diviseur.

    Returns:
        float: Le quotient des deux nombres.
    """
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

def power_number(base: float, exponent: int) -> float:
    """Calcule la puissance d'un nombre.

    Args:
        base (float): Base.
        exponent (int): Exposant.

    Returns:
        float: La base élevée à la puissance de l'exposant.
    """
    return base ** exponent

def square_root(number: float) -> float:
    """Calcule la racine carrée d'un nombre.

    Args:
        number (float): Nombre non négatif.

    Returns:
        float: La racine carrée du nombre.
    """
    if number < 0:
        raise ValueError("Racine carrée d'un nombre négatif")
    return number ** 0.5

def absolute_value(number: float) -> float:
    """Calcule la valeur absolue d'un nombre.

    Args:
        number (float): Nombre.

    Returns:
        float: La valeur absolue du nombre.
    """
    return abs(number)

def is_even(number: int) -> bool:
    """Vérifie si un nombre est pair.

    Args:
        number (int): Nombre à vérifier.

    Returns:
        bool: True si le nombre est pair, False sinon.
    """
    return number % 2 == 0

def factorial(n: int) -> int:
    """Calcule la factorielle d'un nombre.

    Args:
        n (int): Nombre non négatif.

    Returns:
        int: La factorielle du nombre.
    """
    if n < 0:
        raise ValueError("Factorielle d'un nombre négatif")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci.

    Args:
        n (int): Index du nombre (non négatif).

    Returns:
        int: Le n-ième nombre de Fibonacci.
    """
    if n < 0:
        raise ValueError("Index négatif")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)