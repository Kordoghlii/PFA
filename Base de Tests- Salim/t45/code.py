# operations_listes.py

def lst_func1(lst):
    """Retourner la somme de tous les éléments d'une liste."""
    return sum(lst)

def lst_func2(lst):
    """Retourner le plus grand élément dans une liste."""
    return max(lst)

def lst_func3(lst):
    """Retourner le plus petit élément dans une liste."""
    return min(lst)

def lst_func4(lst):
    """Trier la liste par ordre croissant."""
    return sorted(lst)

def lst_func5(lst):
    """Vérifier si un élément est présent dans la liste."""
    return 3 in lst

def lst_func6(lst):
    """Compter le nombre d'occurrences d'un élément dans la liste."""
    return lst.count(2)

def lst_func7(lst):
    """Ajouter un élément à la fin de la liste."""
    lst.append(10)
    return lst

def lst_func8(lst):
    """Supprimer un élément de la liste."""
    if 3 in lst:
        lst.remove(3)
    return lst

def lst_func9(lst):
    """Retourner une copie de la liste inversée."""
    return lst[::-1]
