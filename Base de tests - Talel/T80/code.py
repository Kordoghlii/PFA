def to_uppercase(text: str) -> str:
    """Convertit une chaîne en majuscules.

    Args:
        text (str): Chaîne à convertir.

    Returns:
        str: Chaîne en majuscules.
    """
    return text.upper()

def to_lowercase(text: str) -> str:
    """Convertit une chaîne en minuscules.

    Args:
        text (str): Chaîne à convertir.

    Returns:
        str: Chaîne en minuscules.
    """
    return text.lower()

def reverse_string(text: str) -> str:
    """Inverse une chaîne.

    Args:
        text (str): Chaîne à inverser.

    Returns:
        str: Chaîne inversée.
    """
    return text[::-1]

def count_vowels(text: str) -> int:
    """Compte le nombre de voyelles dans une chaîne.

    Args:
        text (str): Chaîne à analyser.

    Returns:
        int: Nombre de voyelles.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def is_palindrome(text: str) -> bool:
    """Vérifie si une chaîne est un palindrome.

    Args:
        text (str): Chaîne à vérifier.

    Returns:
        bool: True si palindrome, False sinon.
    """
    text = text.lower()
    return text == text[::-1]

def remove_spaces(text: str) -> str:
    """Supprime les espaces d'une chaîne.

    Args:
        text (str): Chaîne à modifier.

    Returns:
        str: Chaîne sans espaces.
    """
    return text.replace(" ", "")

def capitalize_words(text: str) -> str:
    """Met en majuscule la première lettre de chaque mot.

    Args:
        text (str): Chaîne à modifier.

    Returns:
        str: Chaîne avec mots capitalisés.
    """
    return text.title()

def count_words(text: str) -> int:
    """Compte le nombre de mots dans une chaîne.

    Args:
        text (str): Chaîne à analyser.

    Returns:
        int: Nombre de mots.
    """
    return len(text.split())

def replace_char(text: str, old: str, new: str) -> str:
    """Remplace un caractère par un autre dans une chaîne.

    Args:
        text (str): Chaîne à modifier.
        old (str): Caractère à remplacer.
        new (str): Nouveau caractère.

    Returns:
        str: Chaîne modifiée.
    """
    return text.replace(old, new)

def is_alpha(text: str) -> bool:
    """Vérifie si une chaîne contient uniquement des lettres.

    Args:
        text (str): Chaîne à vérifier.

    Returns:
        bool: True si uniquement lettres, False sinon.
    """
    return text.isalpha()