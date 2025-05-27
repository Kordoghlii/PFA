"""
Module contenant 30 fonctions avec différents niveaux de documentation et de commentaires.
"""
import math
import random
import string
import unittest


# ==============================
# Fonctions documentées et commentées
# ==============================

def calculer_aire_cercle(rayon):
    """Calcule l'aire d'un cercle à partir de son rayon.
    Args:
        rayon (float): Le rayon du cercle
    Returns:
        float: L'aire du cercle
    """
    # On utilise la formule mathématique : aire = π × r²
    return math.pi * (rayon ** 2)


def est_palindrome(texte):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    
    Args:
        texte (str): La chaîne à vérifier
        
    Returns:
        bool: True si c'est un palindrome, False sinon
    """
    # On retire les espaces et on convertit en minuscules
    texte_propre = texte.lower().replace(" ", "")
    # On compare la chaîne avec sa version inversée
    return texte_propre == texte_propre[::-1]


def compteur_mots(phrase):
    """
    Compte le nombre de mots dans une phrase.
    
    Args:
        phrase (str): La phrase à analyser
        
    Returns:
        int: Le nombre de mots dans la phrase
    """
    # On divise la phrase par les espaces et on compte les éléments non vides
    return len([mot for mot in phrase.split() if mot])


def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    
    Args:
        nombres (list): Liste de nombres
        
    Returns:
        float: La moyenne des nombres, ou None si la liste est vide
    """
    # Vérification si la liste n'est pas vide
    if not nombres:
        return None
    # Calcul de la somme divisée par le nombre d'éléments
    return sum(nombres) / len(nombres)


def generer_mot_de_passe(longueur=8):
    """
    Génère un mot de passe aléatoire avec la longueur spécifiée.
    
    Args:
        longueur (int, optional): Longueur du mot de passe. Par défaut 8.
        
    Returns:
        str: Mot de passe généré
    """
    # On définit les caractères possibles
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # On génère un mot de passe aléatoire
    return ''.join(random.choice(caracteres) for _ in range(longueur))


# ==============================
# Fonctions documentées mais non commentées
# ==============================

def fibonacci(n):
    """
    Calcule le nième terme de la suite de Fibonacci.
    
    Args:
        n (int): L'indice du terme à calculer (commençant à 0)
        
    Returns:
        int: Le nième terme de la suite
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def est_premier(nombre):
    """
    Vérifie si un nombre est premier.
    
    Args:
        nombre (int): Le nombre à vérifier
        
    Returns:
        bool: True si le nombre est premier, False sinon
    """
    if nombre <= 1:
        return False
    if nombre <= 3:
        return True
    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
    i = 5
    while i * i <= nombre:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i += 6
    return True


def inverser_dictionnaire(dico):
    """
    Inverse les clés et les valeurs d'un dictionnaire.
    
    Args:
        dico (dict): Le dictionnaire à inverser
        
    Returns:
        dict: Un nouveau dictionnaire avec clés et valeurs inversées
    """
    return {valeur: cle for cle, valeur in dico.items()}


def celsius_vers_fahrenheit(celsius):
    """
    Convertit une température de Celsius à Fahrenheit.
    
    Args:
        celsius (float): La température en degrés Celsius
        
    Returns:
        float: La température en degrés Fahrenheit
    """
    return (celsius * 9/5) + 32


def compter_voyelles(texte):
    """
    Compte le nombre de voyelles dans un texte.
    
    Args:
        texte (str): Le texte à analyser
        
    Returns:
        int: Le nombre de voyelles
    """
    return sum(1 for char in texte.lower() if char in "aeiouy")


# ==============================
# Fonctions commentées mais non documentées
# ==============================

def pgcd(a, b):
    # Calcule le Plus Grand Commun Diviseur de deux nombres
    # en utilisant l'algorithme d'Euclide
    while b:
        a, b = b, a % b
    return a


def factorielle(n):
    # Calcule la factorielle de n (n!)
    # Retourne 1 pour n=0, sinon n * (n-1)!
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


def filtrer_pairs(liste):
    # Filtre et retourne uniquement les nombres pairs d'une liste
    return [x for x in liste if x % 2 == 0]


def formater_nom(prenom, nom):
    # Met en forme un nom complet avec le prénom et le nom
    # Le prénom a une majuscule initiale, le nom est en majuscules
    return f"{prenom.capitalize()} {nom.upper()}"


def fusionner_listes(*listes):
    # Fusionne plusieurs listes en une seule sans doublons
    # et retourne la liste triée
    resultat = []
    for liste in listes:
        resultat.extend(liste)
    return sorted(set(resultat))


def convertir_temps(secondes):
    # Convertit un nombre de secondes en format heures:minutes:secondes
    h = secondes // 3600
    m = (secondes % 3600) // 60
    s = secondes % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


# ==============================
# Fonctions ni documentées ni commentées
# ==============================

def somme_liste(liste):
    return sum(liste)


def trouver_maximum(liste):
    if not liste:
        return None
    return max(liste)


def inverser_chaine(texte):
    return texte[::-1]


def est_anagramme(mot1, mot2):
    return sorted(mot1.lower()) == sorted(mot2.lower())


def appliquer_tva(montant, taux=20):
    return montant * (1 + taux/100)


def compter_occurrences(liste, element):
    return liste.count(element)


def extraire_extension(nom_fichier):
    parties = nom_fichier.split('.')
    if len(parties) > 1:
        return parties[-1]
    return ""


def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)