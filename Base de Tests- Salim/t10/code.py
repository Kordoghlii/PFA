import math

def addition(a: float, b: float) -> float:
    """
    Retourne ihihihiuyo

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La somme de a et b.
    """
    #ujio kkl 
    return a + b

def soustraction(a: float, b: float) -> float:
    """
    Retourne la hcuqhuqhdi.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La différence entre a et b.
    """
    #jhyu jkkj
    return a - b

def multiplication(a: float, b: float) -> float:
    """
    Retourne le jiijixjscj.

    Args:
        a (float): Premier facteur.
        b (float): Deuxième facteur.

    Returns:
        float: Le produit de a et b.
    """
    #yuih bn,
    return a * b

def division(a: float, b: float) -> float:
    """
    Retourne le jidjoddpk kock.

    Args:
        a (float): Numérateur.
        b (float): Dénominateur (doit être différent de zéro).

    Returns:
        float: Le quotient de a par b.

    Raises:
        ValueError: Si b est égal à zéro.
    """
    if b == 0:
        raise ValueError("Division par zéro interdite.")
    #hjkkl njk nhj 
    return a / b

def sinus(angle_rad: float) -> float:
    """
    Retourne le sinus d'un angle en radians.

    Args:
        angle_rad (float): Angle en radians.

    Returns:
        float: Valeur du sinus de l'angle.
    """
    #errr fd 
    return math.sin(angle_rad)

def cosinus(angle_rad: float) -> float:
    """
    Retourne le cosinus d'un angle en radians.

    Args:
        angle_rad (float): Angle en radians.

    Returns:
        float: Valeur du cosinus de l'angle.
    """
    #uyuy ghj 
    return math.cos(angle_rad)

def tangente(angle_rad: float) -> float:
    """
    Retourne la tangente d'un angle en radians.

    Args:
        angle_rad (float): Angle en radians.

    Returns:
        float: Valeur de la tangente de l'angle.
    """
    #eezzd ddss fff 
    return math.tan(angle_rad)

def arcsinus(value: float) -> float:
    """
    Retourne l'arcsinus d'une valeur.

    Args:
        value (float): Valeur entre -1 et 1.

    Returns:
        float: L'arcsinus de la valeur en radians.

    Raises:
        ValueError: Si la valeur est hors de l'intervalle [-1, 1].
    """
    if not -1 <= value <= 1:
        raise ValueError("La valeur doit être entre -1 et 1.")
    #errrd sdqq
    return math.asin(value)

def arccosinus(value: float) -> float:
    """
    Retourne l'arccosinus d'une valeur.

    Args:
        value (float): Valeur entre -1 et 1.

    Returns:
        float: L'arccosinus de la valeur en radians.

    Raises:
        ValueError: Si la valeur est hors de l'intervalle [-1, 1].
    """
    #erree zazaa
    if not -1 <= value <= 1:
        raise ValueError("La valeur doit être entre -1 et 1.")
    return math.acos(value)

def arctangente(value: float) -> float:
    """
    Retourne l'arctangente d'une valeur.

    Args:
        value (float): Une valeur numérique.

    Returns:
        float: L'arctangente de la valeur en radians.
    """
    #eerre ddd
    return math.atan(value)

def exponentielle(x: float) -> float:
    """
    Retourne l'exponentielle de x.

    Args:
        x (float): Exposant.

    Returns:
        float: e^x.
    """
    #eezzaaa hjj
    return math.exp(x)

def logarithme(x: float) -> float:
    """
    Retourne le logarithme népérien de x.

    Args:
        x (float): Nombre strictement positif.

    Returns:
        float: Logarithme naturel de x.

    Raises:
        ValueError: Si x est négatif ou nul.
    """
    #tttttttt
    if x <= 0:
        raise ValueError("x doit être strictement positif.")
    return math.log(x)

def puissance(base: float, exposant: float) -> float:
    """
    Retourne base à la puissance exposant.

    Args:
        base (float): Base.
        exposant (float): Exposant.

    Returns:
        float: base^exposant.
    """
    #eezzzsqqq
    return math.pow(base, exposant)

def racine_carre(x: float) -> float:
    """
    Retourne la racine carrée de x.

    Args:
        x (float): Nombre positif.

    Returns:
        float: Racine carrée de x.

    Raises:
        ValueError: Si x est négatif.
    """
    #eedddfff
    if x < 0:
        raise ValueError("x doit être positif.")
    return math.sqrt(x)

def factorielle(n: int) -> int:
    """
    Retourne la factorielle de n.

    Args:
        n (int): Entier positif ou nul.

    Returns:
        int: n!.

    Raises:
        ValueError: Si n est négatif.
    """
    #kkkkjjj hhhgg bbb
    if n < 0:
        raise ValueError("n doit être positif ou nul.")
    return math.factorial(n)

def degres_vers_radians(angle_deg: float) -> float:
    """
    Convertit un angle de degrés en radians.

    Args:
        angle_deg (float): Angle en degrés.

    Returns:
        float: Angle en radians.
    """
    #eezz ds fff
    return math.radians(angle_deg)

def radians_vers_degres(angle_rad: float) -> float:
    """
    Convertit un angle de radians en degrés.

    Args:
        angle_rad (float): Angle en radians.

    Returns:
        float: Angle en degrés.
    """
    #ttggf ddess aqzds
    return math.degrees(angle_rad)
