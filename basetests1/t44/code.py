# manipulation_chaine.py

def str_func1(txt):
    """Mettre une chaîne de caractères en majuscules."""
    return txt.upper()

def str_func2(txt):
    """Compter le nombre de caractères dans la chaîne."""
    return len(txt)

def str_func3(txt):
   
    return txt[::-1]

def str_func4(txt):
    """Vérifier si la chaîne contient un sous-texte spécifique."""
    return "test" in txt

def str_func5(txt, word):
    """Compter combien de fois un mot apparaît dans la chaîne."""
    return txt.count(word)

def str_func6(txt):
    """Vérifier si la chaîne est un palindrome."""
    return txt == txt[::-1]

def str_func7(txt):
    """Convertir une chaîne en minuscules."""
    return txt.lower()

def str_func8(txt, n):
   
    return txt * n

def str_func9(txt):
 
    return txt.replace(" ", "")
