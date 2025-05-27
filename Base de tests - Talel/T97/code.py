import math

def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.
    
    Returns:
        float: La somme des deux nombres.
    """
    # Addition de a et b
    return a + b

def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier.
    
    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.
    
    Returns:
        float: La différence entre a et b.
    """
    # Soustraction de b de a
    return a - b

def multiply(a, b):
    """
    Multiplie deux nombres.
    
    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.
    
    Returns:
        float: Le produit de a et b.
    """
    # Multiplication de a et b
    return a * b

def divide(a, b):
    """
    Divise le premier nombre par le deuxième.
    
    Args:
        a (float): Le numérateur.
        b (float): Le dénominateur.
    
    Returns:
        float: Le résultat de la division de a par b.
    
    Raises:
        ZeroDivisionError: Si b est égal à 0.
    """
    # Vérification de la division par zéro
    if b == 0:
        raise ZeroDivisionError("Division par zéro non autorisée")
    return a / b

def square_root(x):
    """
    Calcule la racine carrée d'un nombre.
    
    Args:
        x (float): Le nombre.
    
    Returns:
        float: La racine carrée de x.
    
    Raises:
        ValueError: Si x est négatif.
    """
    # Vérification que x est positif
    if x < 0:
        raise ValueError("Le nombre ne peut pas être négatif")
    return math.sqrt(x)

def power(a, b):
    """
    Élève un nombre à une certaine puissance.
    
    Args:
        a (float): Le nombre de base.
        b (float): L'exposant.
    
    Returns:
        float: Le résultat de a élevé à la puissance b.
    """
    # Élève a à la puissance b
    return math.pow(a, b)

def log(x):
    """
    Calcule le logarithme népérien d'un nombre.
    
    Args:
        x (float): Le nombre.
    
    Returns:
        float: Le logarithme naturel de x.
    
    Raises:
        ValueError: Si x est inférieur ou égal à 0.
    """
    # Vérification que x est positif
    if x <= 0:
        raise ValueError("x doit être strictement positif")
    return math.log(x)

def factorial(n):
    """
    Calcule la factorielle d'un nombre entier positif.
    
    Args:
        n (int): Le nombre entier.
    
    Returns:
        int: La factorielle de n.
    
    Raises:
        ValueError: Si n est inférieur à 0.
    """
    # Vérification que n est un entier positif
    if n < 0:
        raise ValueError("n doit être un entier positif")
    return math.factorial(n)

def sin_angle(angle):
    """
    Calcule le sinus d'un angle en radians.
    
    Args:
        angle (float): L'angle en radians.
    
    Returns:
        float: Le sinus de l'angle.
    """
    # Calcul du sinus de l'angle
    return math.sin(angle)

def cos_angle(angle):
    """
    Calcule le cosinus d'un angle en radians.
    
    Args:
        angle (float): L'angle en radians.
    
    Returns:
        float: Le cosinus de l'angle.
    """
    # Calcul du cosinus de l'angle
    return math.cos(angle)
