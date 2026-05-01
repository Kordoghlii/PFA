# utils_script1.py

def add(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    # Addition simple
    return a + b

def subtract(a, b):
    """
    Soustrait deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: Le résultat de la soustraction.
    """
    # Soustraction simple
    return a - b

def multiply(a, b):
    """
    Multiplie deux nombres.

    Args:
        a (int): Le premier facteur.
        b (int): Le deuxième facteur.

    Returns:
        int: Le produit des deux nombres.
    """
    # Multiplication simple
    return a * b

def divide(a, b):
    """
    Divise un nombre par un autre.

    Args:
        a (int): Le dividende.
        b (int): Le diviseur.

    Returns:
        float: Le résultat de la division.
    """
    # Division avec gestion de zéro
    if b == 0:
        return None
    return a / b

def power(a, b):
    """
    Élève un nombre à la puissance d'un autre.

    Args:
        a (int): La base.
        b (int): L'exposant.

    Returns:
        int: Le résultat de l'exponentiation.
    """
    # Exponentiation
    return a ** b

def mod(a, b):
    """
    Calcule le modulo de deux nombres.

    Args:
        a (int): Le dividende.
        b (int): Le diviseur.

    Returns:
        int: Le reste de la division.
    """
    # Modulo
    return a % b

def is_even(n):
    """
    Vérifie si un nombre est pair.

    Args:
        n (int): Le nombre à vérifier.

    Returns:
        bool: True si pair, False sinon.
    """
    # Vérification de parité
    return n % 2 == 0

def is_odd(n):
    """
    Vérifie si un nombre est impair.

    Args:
        n (int): Le nombre à vérifier.

    Returns:
        bool: True si impair, False sinon.
    """
    # Vérification d'impair
    return n % 2 != 0

def max_of_two(a, b):
    """
    Retourne le maximum entre deux nombres.

    Args:
        a (int): Premier nombre.
        b (int): Deuxième nombre.

    Returns:
        int: Le plus grand des deux nombres.
    """
    # Retour du max
    return a if a > b else b

def min_of_two(a, b):
    """
    Retourne le minimum entre deux nombres.

    Args:
        a (int): Premier nombre.
        b (int): Deuxième nombre.

    Returns:
        int: Le plus petit des deux nombres.
    """
    # Retour du min
    return a if a < b else b


