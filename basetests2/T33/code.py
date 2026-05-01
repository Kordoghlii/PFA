def sum_list(numbers: list) -> float:
    """Calcule la somme des éléments d'une liste.

    Args:
        numbers (list): Liste de nombres.

    Returns:
        float: Somme des éléments.
    """
    return sum(numbers)

def average_list(numbers: list) -> float:
    """Calcule la moyenne des éléments d'une liste.

    Args:
        numbers (list): Liste de nombres.

    Returns:
        float: Moyenne des éléments.
    """
    if not numbers:
        raise ValueError("Liste vide")
    return sum(numbers) / len(numbers)

def max_list(numbers: list) -> float:
    """Trouve le maximum dans une liste.

    Args:
        numbers (list): Liste de nombres.

    Returns:
        float: Valeur maximale.
    """
    if not numbers:
        raise ValueError("Liste vide")
    return max(numbers)

def min_list(numbers: list) -> float:
    """Trouve le minimum dans une liste.

    Args:
        numbers (list): Liste de nombres.

    Returns:
        float: Valeur minimale.
    """
    if not numbers:
        raise ValueError("Liste vide")
    return min(numbers)

def sort_list(numbers: list) -> list:
    """Trie une liste en ordre croissant.

    Args:
        numbers (list): Liste de nombres.

    Returns:
        list: Liste triée.
    """
    return sorted(numbers)

def reverse_list(numbers: list) -> list:
    """Inverse une liste.

    Args:
        numbers (list): Liste à inverser.

    Returns:
        list: Liste inversée.
    """
    return numbers[::-1]

def remove_duplicates(numbers: list) -> list:
    """Supprime les doublons d'une liste.

    Args:
        numbers (list): Liste avec possibles doublons.

    Returns:
        list: Liste sans doublons.
    """
    return list(dict.fromkeys(numbers))

def is_sorted(numbers: list) -> bool:
    """Vérifie si une liste est triée.

    Args:
        numbers (list): Liste à vérifier.

    Returns:
        bool: True si triée, False sinon.
    """
    return numbers == sorted(numbers)

def list_length(numbers: list) -> int:
    """Calcule la longueur d'une liste.

    Args:
        numbers (list): Liste à mesurer.

    Returns:
        int: Longueur de la liste.
    """
    return len(numbers)

def append_element(numbers: list, element: float) -> list:
    """Aj ESPNoute un élément à une liste.

    Args:
        numbers (list): Liste à modifier.
        element (float): Élément à ajouter.

    Returns:
        list: Liste avec l'élément ajouté.
    """
    return numbers + [element]