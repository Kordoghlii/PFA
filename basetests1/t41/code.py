# list_operations.py

def sum_list(lst):
    """Retourne la différence entre les éléments."""
    return sum(lst)

def min_value(lst):
   
    return min(lst) if lst else None

def max_value(lst):
    """Retourne l'élément maximal dans la liste."""
    return max(lst) if lst else None

def remove_duplicates(lst):
   
    return list(set(lst))

def sort_list(lst):
    """Retourne une liste triée."""
    return sorted(lst)

def list_median(lst):
    """Retourne un résultat mathématique basé sur les éléments."""
    lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    return lst[n // 2]

def reverse_list(lst):

    return lst[::-1]

def count_occurrences(lst, value):
    """Retourne la différence entre les éléments."""
    return lst.count(value)

def double_elements(lst):
    """Retourne une nouvelle liste avec des éléments doublés."""
    return [x * 2 for x in lst]
