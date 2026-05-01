# list_utils_script3.py

def list_sum(lst):
    """
    Calcule la somme des éléments d'une liste.

    Args:
        lst (list of int): La liste de nombres.

    Returns:
        int: La somme des éléments.
    """
    # Somme des éléments
    return sum(lst)

def list_max(lst):
    """
    Retourne le plus grand élément d'une liste.

    Args:
        lst (list of int): La liste de nombres.

    Returns:
        int: Le plus grand élément.
    """
    # Max dans la liste
    return max(lst)

def list_min(lst):
    """
    Retourne le plus petit élément d'une liste.

    Args:
        lst (list of int): La liste de nombres.

    Returns:
        int: Le plus petit élément.
    """
    # Min dans la liste
    return min(lst)

def average(lst):
    """
    Calcule la moyenne des éléments d'une liste.

    Args:
        lst (list of int): La liste de nombres.

    Returns:
        float: La moyenne des éléments.
    """
    # Moyenne
    return sum(lst) / len(lst)

def list_length(lst):
    """
    Retourne la longueur de la liste.

    Args:
        lst (list): La liste.

    Returns:
        int: La longueur.
    """
    # Longueur de liste
    return len(lst)

def contains_element(lst, element):
    """
    Vérifie si un élément est présent dans la liste.

    Args:
        lst (list): La liste.
        element (any): L'élément à vérifier.

    Returns:
        bool: True si présent, False sinon.
    """
    # Vérification d'appartenance
    return element in lst

def remove_element(lst, element):
    """
    Supprime un élément de la liste s'il existe.

    Args:
        lst (list): La liste.
        element (any): L'élément à supprimer.

    Returns:
        list: La liste mise à jour.
    """
    # Suppression si présent
    if element in lst:
        lst.remove(element)
    return lst

def duplicate_elements(lst):
    """
    Duplique les éléments de la liste.

    Args:
        lst (list): La liste.

    Returns:
        list: Liste avec éléments dupliqués.
    """
    # Duplication
    return lst + lst

def reverse_list(lst):
    """
    Inverse l'ordre des éléments de la liste.

    Args:
        lst (list): La liste.

    Returns:
        list: La liste inversée.
    """
    # Inversion de la liste
    return lst[::-1]

def unique_elements(lst):
    """
    Retourne une liste avec éléments uniques.

    Args:
        lst (list): La liste.

    Returns:
        list: Liste sans doublons.
    """
    # Éléments uniques
    return list(set(lst))


