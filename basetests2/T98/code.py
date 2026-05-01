def to_uppercase(s):
    """
    Convertit une chaîne en majuscules.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        str: La chaîne convertie en majuscules.
    """
    # Conversion de la chaîne en majuscules
    return s.upper()

def to_lowercase(s):
    """
    Convertit une chaîne en minuscules.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        str: La chaîne convertie en minuscules.
    """
    # Conversion de la chaîne en minuscules
    return s.lower()

def reverse_string(s):
    """
    Inverse une chaîne de caractères.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        str: La chaîne inversée.
    """
    # Inversion de la chaîne
    return s[::-1]

def concatenate_strings(s1, s2):
    """
    Concatène deux chaînes de caractères.
    
    Args:
        s1 (str): La première chaîne.
        s2 (str): La deuxième chaîne.
    
    Returns:
        str: La chaîne résultante de la concaténation de s1 et s2.
    """
    # Concatenation de s1 et s2
    return s1 + s2

def count_characters(s):
    """
    Compte le nombre de caractères dans une chaîne.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        int: Le nombre de caractères dans la chaîne.
    """
    # Comptage des caractères
    return len(s)

def replace_substring(s, old, new):
    """
    Remplace une sous-chaîne par une autre dans une chaîne.
    
    Args:
        s (str): La chaîne de caractères.
        old (str): La sous-chaîne à remplacer.
        new (str): La sous-chaîne de remplacement.
    
    Returns:
        str: La chaîne après remplacement.
    """
    # Remplacement de l'ancienne sous-chaîne par la nouvelle
    return s.replace(old, new)

def split_string(s, delimiter=" "):
    """
    Divise une chaîne en sous-chaînes selon un délimiteur.
    
    Args:
        s (str): La chaîne de caractères.
        delimiter (str): Le délimiteur pour diviser la chaîne (par défaut un espace).
    
    Returns:
        list: Une liste de sous-chaînes.
    """
    # Division de la chaîne selon le délimiteur
    return s.split(delimiter)

def string_length(s):
    """
    Renvoie la longueur d'une chaîne.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        int: La longueur de la chaîne.
    """
    # Renvoie la longueur de la chaîne
    return len(s)

def check_palindrome(s):
    """
    Vérifie si une chaîne est un palindrome.
    
    Args:
        s (str): La chaîne de caractères.
    
    Returns:
        bool: True si la chaîne est un palindrome, sinon False.
    """
    # Vérification si la chaîne est égale à sa version inversée
    return s == s[::-1]

def format_string(s, width, fill_char=" "):
    """
    Formate une chaîne pour qu'elle ait une largeur spécifique.
    
    Args:
        s (str): La chaîne de caractères.
        width (int): La largeur cible.
        fill_char (str): Le caractère à utiliser pour remplir (par défaut un espace).
    
    Returns:
        str: La chaîne formatée.
    """
    # Formatage de la chaîne avec un remplissage
    return s.rjust(width, fill_char)
