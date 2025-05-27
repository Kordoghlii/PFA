# chaine.py

def str1(txt):

    return txt.upper()

def str2(txt):
    # Compte les caractères de la chaîne.
    return len(txt)

def str3(txt):
    # Inverse le texte.
    return txt[::-1]

def str4(txt):
    # Recherche un mot spécifique dans le texte.
    return "find" in txt

def str5(txt):
    # Vérifie si la chaîne contient "mot".
    return "mot" in txt

def str6(txt):
    # Vérifie si le texte contient un autre texte.
    return "search" in txt

def str7(txt):
    # Retourne une version modifiée du texte.
    return txt.lower()

def str8(txt):
    # Modifie le texte en ajoutant des espaces.
    return " ".join(txt.split())

def str9(txt):
    # Supprime certains caractères.
    return txt.replace("a", "")

def str10(txt):

    return txt == txt[::-1]
