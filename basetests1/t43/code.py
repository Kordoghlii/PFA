# operations_maths.py

def func1(x):
    """Calculer le carré d'un nombre."""
    return x * x

def func2(a, b):
    """Additionner deux nombres."""
    return a + b

def func3(x):
    """Calculer la racine carrée d'un nombre."""
    return x ** 0.5

def func4(n):
    """Calculer le produit de tous les entiers jusqu'à n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def func5(a, b):
    """Calculer la différence entre deux nombres."""
    return a - b

def func6(lst):
    """Retourner la somme de tous les éléments dans une liste."""
    return sum(lst)

def func7(x):
    """Vérifier si un nombre est impair."""
    return x % 2 != 0

def func8(x):
    """Vérifier si un nombre est pair."""
    return x % 2 == 0

def func9(a, b):
    
    return a * b

def func10(a, b):
 
    return a == b
