def add_to_list(lst, item):
    """
    Ajoute un élément à une liste.
    
    Args:
        lst (list): La liste d'origine.
        item (any): L'élément à ajouter à la liste.
    
    Returns:
        list: La liste mise à jour.
    """
    # Ajout de l'élément à la liste
    lst.append(item)
    return lst

def remove_from_list(lst, item):
    """
    Retire un élément d'une liste.
    
    Args:
        lst (list): La liste d'origine.
        item (any): L'élément à retirer.
    
    Returns:
        list: La liste mise à jour.
    
    Raises:
        ValueError: Si l'élément n'est pas trouvé dans la liste.
    """
    # Retrait de l'élément de la liste
    if item not in lst:
        raise ValueError("Élément non trouvé dans la liste")
    lst.remove(item)
    return lst

def find_max(lst):
    """
    Trouve le plus grand élément d'une liste.
    
    Args:
        lst (list): La liste d'éléments.
    
    Returns:
        any: Le plus grand élément de la liste.
    
    Raises:
        ValueError: Si la liste est vide.
    """
    # Recherche du plus grand élément
    if not lst:
        raise ValueError("La liste est vide")
    return max(lst)

def find_min(lst):
    """
    Trouve le plus petit élément d'une liste.
    
    Args:
        lst (list): La liste d'éléments.
    
    Returns:
        any: Le plus petit élément de la liste.
    
    Raises:
        ValueError: Si la liste est vide.
    """
    # Recherche du plus petit élément
    if not lst:
        raise ValueError("La liste est vide")
    return min(lst)

def sum_list(lst):
    """
    Calcule la somme des éléments d'une liste.
    
    Args:
        lst (list): La liste d'éléments numériques.
    
    Returns:
        float: La somme des éléments de la liste.
    """
    # Calcul de la somme des éléments
    return sum(lst)

def average_list(lst):
    """
    Calcule la moyenne des éléments d'une liste.
    
    Args:
        lst (list): La liste d'éléments numériques.
    
    Returns:
        float: La moyenne des éléments.
    
    Raises:
        ValueError: Si la liste est vide.
    """
    # Vérification de la liste vide
    if not lst:
        raise ValueError("La liste est vide")
    return sum(lst) / len(lst)

def sort_list(lst):
    """
    Trie les éléments d'une liste par ordre croissant.
    
    Args:
        lst (list): La liste d'éléments.
    
    Returns:
        list: La liste triée.
    """
    # Tri de la liste
    return sorted(lst)

def filter_even_numbers(lst):
    """
    Filtre les nombres pairs d'une liste.
    
    Args:
        lst (list): La liste d'entiers.
    
    Returns:
        list: La liste des nombres pairs.
    """
    # Filtrage des nombres pairs
    return [x for x in lst if x % 2 == 0]

def filter_odd_numbers(lst):
    """
    Filtre les nombres impairs d'une liste.
    
    Args:
        lst (list): La liste d'entiers.
    
    Returns:
        list: La liste des nombres impairs.
    """
    # Filtrage des nombres impairs
    return [x for x in lst if x % 2 != 0]

def merge_lists(lst1, lst2):
    """
    Fusionne deux listes en une seule.
    
    Args:
        lst1 (list): La première liste.
        lst2 (list): La deuxième liste.
    
    Returns:
        list: La liste fusionnée.
    """
    # Fusion des deux listes
    return lst1 + lst2
