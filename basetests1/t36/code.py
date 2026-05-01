# liste.py

def lst1(lst):
    # Additionne les éléments d'une liste.
    return sum(lst)

def lst2(lst):
    # Trouve l'élément maximum de la liste.
    return max(lst)

def lst3(lst):
    # Trouve l'élément minimum de la liste.
    return min(lst)

def lst4(lst):
    # Trie la liste d'éléments.
    return sorted(lst)

def lst5(lst):
    # Vérifie si un élément est dans la liste.
    return 3 in lst

def lst6(lst):
    # Compte combien de fois un élément est présent dans la liste.
    return lst.count(3)

def lst7(lst):
    # Ajoute un élément à la fin de la liste.
    lst.append(10)
    return lst

def lst8(lst):
    # Supprime un élément de la liste.
    lst.remove(3)
    return lst

def lst9(lst):
 
    return lst[::-1]

def lst10(lst):
    # Supprime les doublons dans la liste.
    return list(set(lst))
