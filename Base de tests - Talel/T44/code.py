# string_utils_script2.py

def reverse_string(s):
    """
    Inverse une chaîne de caractères.

    Args:
        s (str): La chaîne à inverser.

    Returns:
        str: La chaîne inversée.
    """
    # Inversion de la chaîne
    return s[::-1]

def is_palindrome(s):
    """
    Vérifie si une chaîne est un palindrome.

    Args:
        s (str): La chaîne à vérifier.

    Returns:
        bool: True si palindrome, False sinon.
    """
    # Vérification palindrome
    return s == s[::-1]

def to_upper(s):
    """
    Convertit une chaîne en majuscules.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        str: La chaîne en majuscules.
    """
    # Conversion en majuscules
    return s.upper()

def to_lower(s):
    """
    Convertit une chaîne en minuscules.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        str: La chaîne en minuscules.
    """
    # Conversion en minuscules
    return s.lower()

def count_vowels(s):
    """
    Compte le nombre de voyelles dans une chaîne.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        int: Le nombre de voyelles.
    """
    # Compte des voyelles
    return sum(1 for c in s.lower() if c in 'aeiou')

def count_consonants(s):
    """
    Compte le nombre de consonnes dans une chaîne.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        int: Le nombre de consonnes.
    """
    # Compte des consonnes
    return sum(1 for c in s.lower() if c.isalpha() and c not in 'aeiou')

def remove_spaces(s):
    """
    Supprime tous les espaces dans une chaîne.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        str: La chaîne sans espaces.
    """
    # Suppression des espaces
    return s.replace(" ", "")

def capitalize_words(s):
    """
    Met en majuscule la première lettre de chaque mot.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        str: La chaîne avec chaque mot capitalisé.
    """
    # Capitalisation des mots
    return s.title()

def string_length(s):
    """
    Retourne la longueur d'une chaîne.

    Args:
        s (str): La chaîne d'entrée.

    Returns:
        int: La longueur de la chaîne.
    """
    # Longueur de chaîne
    return len(s)

def contains_digit(s):
    """
    Vérifie si une chaîne contient au moins un chiffre.

    Args:
        s (str): La chaîne à vérifier.

    Returns:
        bool: True si un chiffre est présent, False sinon.
    """
    # Présence de chiffre
    return any(c.isdigit() for c in s)


