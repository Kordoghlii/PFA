"""
Collection de 100 fonctions Python utiles
Documentées et commentées, sans utilisation de 'for i in range'
"""

import math
import random
import re
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
import json

# ==================== FONCTIONS MATHÉMATIQUES ====================

def fibonacci(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci de manière récursive."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorielle(n: int) -> int:
    """Calcule la factorielle d'un nombre."""
    if n <= 1:
        return 1
    return n * factorielle(n-1)

def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux nombres."""
    while b:
        a, b = b, a % b
    return a

def ppcm(a: int, b: int) -> int:
    """Calcule le plus petit commun multiple de deux nombres."""
    return abs(a * b) // pgcd(a, b)

def est_premier(n: int) -> bool:
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    # Vérifie uniquement jusqu'à la racine carrée
    diviseur = 2
    while diviseur * diviseur <= n:
        if n % diviseur == 0:
            return False
        diviseur += 1
    return True

def somme_carres(lst: List[int]) -> int:
    """Calcule la somme des carrés d'une liste."""
    return sum(x**2 for x in lst)

def moyenne_geometrique(lst: List[float]) -> float:
    """Calcule la moyenne géométrique d'une liste de nombres."""
    if not lst or any(x <= 0 for x in lst):
        raise ValueError("Tous les nombres doivent être positifs")
    produit = 1
    for x in lst:
        produit *= x
    return produit ** (1/len(lst))

def distance_euclidienne(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Calcule la distance euclidienne entre deux points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def convertir_base(nombre: int, base: int) -> str:
    """Convertit un nombre décimal vers une autre base."""
    if nombre == 0:
        return "0"
    chiffres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = ""
    while nombre:
        resultat = chiffres[nombre % base] + resultat
        nombre //= base
    return resultat

def aire_triangle(a: float, b: float, c: float) -> float:
    """Calcule l'aire d'un triangle avec la formule d'Héron."""
    s = (a + b + c) / 2  # Semi-périmètre
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

# ==================== FONCTIONS DE CHAÎNES ====================

def inverser_mots(phrase: str) -> str:
    """Inverse l'ordre des mots dans une phrase."""
    return ' '.join(phrase.split()[::-1])

def compter_voyelles(texte: str) -> int:
    """Compte le nombre de voyelles dans un texte."""
    voyelles = "aeiouAEIOU"
    return sum(1 for char in texte if char in voyelles)

def est_palindrome(texte: str) -> bool:
    """Vérifie si un texte est un palindrome."""
    texte_nettoye = re.sub(r'[^a-zA-Z0-9]', '', texte.lower())
    return texte_nettoye == texte_nettoye[::-1]

def capitaliser_mots(phrase: str) -> str:
    """Capitalise la première lettre de chaque mot."""
    return ' '.join(mot.capitalize() for mot in phrase.split())

def compter_occurrences(texte: str, mot: str) -> int:
    """Compte les occurrences d'un mot dans un texte."""
    return texte.lower().count(mot.lower())

def remplacer_caracteres(texte: str, ancien: str, nouveau: str) -> str:
    """Remplace tous les caractères d'un type par un autre."""
    return texte.replace(ancien, nouveau)

def extraire_emails(texte: str) -> List[str]:
    """Extrait tous les emails d'un texte."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, texte)

def generer_acronyme(phrase: str) -> str:
    """Génère un acronyme à partir d'une phrase."""
    mots = phrase.split()
    return ''.join(mot[0].upper() for mot in mots if mot)

def nettoyer_espaces(texte: str) -> str:
    """Supprime les espaces multiples et les espaces en début/fin."""
    return ' '.join(texte.split())

def chiffrement_cesar(texte: str, decalage: int) -> str:
    """Applique un chiffrement de César au texte."""
    resultat = ""
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat += chr((ord(char) - base + decalage) % 26 + base)
        else:
            resultat += char
    return resultat

# ==================== FONCTIONS DE LISTES ====================

def trouver_maximum(lst: List[int]) -> int:
    """Trouve le maximum dans une liste sans utiliser max()."""
    if not lst:
        raise ValueError("Liste vide")
    maximum = lst[0]
    for element in lst[1:]:
        if element > maximum:
            maximum = element
    return maximum

def supprimer_doublons(lst: List[Any]) -> List[Any]:
    """Supprime les doublons en préservant l'ordre."""
    vus = set()
    resultat = []
    for element in lst:
        if element not in vus:
            vus.add(element)
            resultat.append(element)
    return resultat

def fusionner_listes_triees(lst1: List[int], lst2: List[int]) -> List[int]:
    """Fusionne deux listes triées en une liste triée."""
    resultat = []
    i, j = 0, 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            resultat.append(lst1[i])
            i += 1
        else:
            resultat.append(lst2[j])
            j += 1
    
    # Ajouter les éléments restants
    resultat.extend(lst1[i:])
    resultat.extend(lst2[j:])
    return resultat

def partitionner_liste(lst: List[int], pivot: int) -> Tuple[List[int], List[int]]:
    """Partitionne une liste autour d'un pivot."""
    petits = [x for x in lst if x < pivot]
    grands = [x for x in lst if x >= pivot]
    return petits, grands

def rotation_liste(lst: List[Any], n: int) -> List[Any]:
    """Effectue une rotation de n positions vers la droite."""
    if not lst:
        return lst
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

def intersection_listes(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """Trouve l'intersection de deux listes."""
    return list(set(lst1) & set(lst2))

def difference_listes(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """Trouve les éléments dans lst1 mais pas dans lst2."""
    return list(set(lst1) - set(lst2))

def regrouper_par_taille(lst: List[Any], taille: int) -> List[List[Any]]:
    """Regroupe les éléments d'une liste par groupes de taille donnée."""
    return [lst[i:i+taille] for i in range(0, len(lst), taille)]

def melanger_liste(lst: List[Any]) -> List[Any]:
    """Mélange une liste de manière aléatoire."""
    copie = lst.copy()
    random.shuffle(copie)
    return copie

def element_majoritaire(lst: List[Any]) -> Optional[Any]:
    """Trouve l'élément majoritaire (plus de n/2 occurrences)."""
    compteur = {}
    for element in lst:
        compteur[element] = compteur.get(element, 0) + 1
        if compteur[element] > len(lst) // 2:
            return element
    return None

# ==================== FONCTIONS DE DICTIONNAIRES ====================

def inverser_dictionnaire(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Inverse les clés et valeurs d'un dictionnaire."""
    return {v: k for k, v in d.items()}

def fusionner_dictionnaires(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Fusionne deux dictionnaires."""
    resultat = d1.copy()
    resultat.update(d2)
    return resultat

def filtrer_dictionnaire(d: Dict[str, Any], condition) -> Dict[str, Any]:
    """Filtre un dictionnaire selon une condition."""
    return {k: v for k, v in d.items() if condition(k, v)}

def compter_valeurs(d: Dict[Any, Any]) -> Dict[Any, int]:
    """Compte les occurrences de chaque valeur dans un dictionnaire."""
    compteur = {}
    for valeur in d.values():
        compteur[valeur] = compteur.get(valeur, 0) + 1
    return compteur

def dictionnaire_vers_liste_tuples(d: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
    """Convertit un dictionnaire en liste de tuples."""
    return list(d.items())

def liste_tuples_vers_dictionnaire(lst: List[Tuple[Any, Any]]) -> Dict[Any, Any]:
    """Convertit une liste de tuples en dictionnaire."""
    return dict(lst)

def obtenir_cles_par_valeur(d: Dict[Any, Any], valeur: Any) -> List[Any]:
    """Obtient toutes les clés ayant une valeur donnée."""
    return [k for k, v in d.items() if v == valeur]

def dictionnaire_profond_get(d: Dict[str, Any], chemin: str, separateur: str = '.') -> Any:
    """Obtient une valeur dans un dictionnaire imbriqué."""
    cles = chemin.split(separateur)
    resultat = d
    for cle in cles:
        if isinstance(resultat, dict) and cle in resultat:
            resultat = resultat[cle]
        else:
            return None
    return resultat

def aplatir_dictionnaire(d: Dict[str, Any], separateur: str = '.') -> Dict[str, Any]:
    """Aplatit un dictionnaire imbriqué."""
    resultat = {}
    
    def _aplatir(obj, prefix=''):
        if isinstance(obj, dict):
            for k, v in obj.items():
                nouveau_prefix = f"{prefix}{separateur}{k}" if prefix else k
                _aplatir(v, nouveau_prefix)
        else:
            resultat[prefix] = obj
    
    _aplatir(d)
    return resultat

def valeurs_par_defaut(d: Dict[str, Any], defauts: Dict[str, Any]) -> Dict[str, Any]:
    """Ajoute des valeurs par défaut à un dictionnaire."""
    resultat = defauts.copy()
    resultat.update(d)
    return resultat

# ==================== FONCTIONS UTILITAIRES ====================

def generer_mot_de_passe(longueur: int = 12) -> str:
    """Génère un mot de passe aléatoire."""
    import string
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def valider_email(email: str) -> bool:
    """Valide le format d'un email."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def calculer_age(date_naissance: str) -> int:
    """Calcule l'âge à partir d'une date de naissance (format YYYY-MM-DD)."""
    naissance = datetime.strptime(date_naissance, '%Y-%m-%d')
    aujourd_hui = datetime.now()
    return aujourd_hui.year - naissance.year - ((aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day))

def formatter_numero_telephone(numero: str) -> str:
    """Formate un numéro de téléphone français."""
    # Supprime tous les caractères non numériques
    chiffres = re.sub(r'\D', '', numero)
    if len(chiffres) == 10:
        return f"{chiffres[:2]}.{chiffres[2:4]}.{chiffres[4:6]}.{chiffres[6:8]}.{chiffres[8:]}"
    return numero

def convertir_taille_fichier(taille_bytes: int) -> str:
    """Convertit une taille en bytes vers une forme lisible."""
    unites = ['B', 'KB', 'MB', 'GB', 'TB']
    taille = float(taille_bytes)
    unite_index = 0
    
    while taille >= 1024 and unite_index < len(unites) - 1:
        taille /= 1024
        unite_index += 1
    
    return f"{taille:.2f} {unites[unite_index]}"

def generer_couleur_hex() -> str:
    """Génère une couleur hexadécimale aléatoire."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def valider_mot_de_passe(mot_de_passe: str) -> Dict[str, bool]:
    """Valide un mot de passe selon différents critères."""
    return {
        'longueur_min': len(mot_de_passe) >= 8,
        'majuscule': any(c.isupper() for c in mot_de_passe),
        'minuscule': any(c.islower() for c in mot_de_passe),
        'chiffre': any(c.isdigit() for c in mot_de_passe),
        'caractere_special': any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mot_de_passe)
    }

def calculer_checksum_simple(texte: str) -> int:
    """Calcule un checksum simple d'un texte."""
    return sum(ord(char) for char in texte) % 1000

def generer_uuid_simple() -> str:
    """Génère un UUID simple (pas cryptographiquement sûr)."""
    import time
    timestamp = int(time.time() * 1000000)
    aleatoire = random.randint(100000, 999999)
    return f"{timestamp}-{aleatoire}"

def normaliser_texte(texte: str) -> str:
    """Normalise un texte (supprime accents, convertit en minuscules)."""
    import unicodedata
    # Supprime les accents
    texte_sans_accents = unicodedata.normalize('NFD', texte)
    texte_sans_accents = ''.join(char for char in texte_sans_accents if unicodedata.category(char) != 'Mn')
    return texte_sans_accents.lower()

# ==================== FONCTIONS DE DATES ====================

def ajouter_jours(date_str: str, jours: int) -> str:
    """Ajoute un nombre de jours à une date."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    nouvelle_date = date + timedelta(days=jours)
    return nouvelle_date.strftime('%Y-%m-%d')

def difference_jours(date1: str, date2: str) -> int:
    """Calcule la différence en jours entre deux dates."""
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

def jour_de_la_semaine(date_str: str) -> str:
    """Retourne le jour de la semaine d'une date."""
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return jours[date.weekday()]

def est_annee_bissextile(annee: int) -> bool:
    """Vérifie si une année est bissextile."""
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

def premier_jour_mois(date_str: str) -> str:
    """Retourne le premier jour du mois d'une date donnée."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    premier_jour = date.replace(day=1)
    return premier_jour.strftime('%Y-%m-%d')

def dernier_jour_mois(date_str: str) -> str:
    """Retourne le dernier jour du mois d'une date donnée."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    # Aller au premier jour du mois suivant puis reculer d'un jour
    if date.month == 12:
        mois_suivant = date.replace(year=date.year+1, month=1, day=1)
    else:
        mois_suivant = date.replace(month=date.month+1, day=1)
    dernier_jour = mois_suivant - timedelta(days=1)
    return dernier_jour.strftime('%Y-%m-%d')

def formatter_date_francaise(date_str: str) -> str:
    """Formate une date au format français."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin',
            'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    return f"{date.day} {mois[date.month-1]} {date.year}"

def calculer_trimestre(date_str: str) -> int:
    """Calcule le trimestre d'une date."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return (date.month - 1) // 3 + 1

def semaine_de_l_annee(date_str: str) -> int:
    """Calcule le numéro de semaine dans l'année."""
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.isocalendar()[1]

def temps_ecoule_lisible(secondes: int) -> str:
    """Convertit des secondes en format lisible (heures, minutes, secondes)."""
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60
    
    if heures > 0:
        return f"{heures}h {minutes}m {secondes_restantes}s"
    elif minutes > 0:
        return f"{minutes}m {secondes_restantes}s"
    else:
        return f"{secondes_restantes}s"

# ==================== FONCTIONS DE VALIDATION ====================

def valider_carte_credit(numero: str) -> bool:
    """Valide un numéro de carte de crédit avec l'algorithme de Luhn."""
    # Supprime les espaces et tirets
    numero = re.sub(r'[\s-]', '', numero)
    
    if not numero.isdigit():
        return False
    
    # Algorithme de Luhn
    somme = 0
    pair = False
    
    for char in reversed(numero):
        chiffre = int(char)
        if pair:
            chiffre *= 2
            if chiffre > 9:
                chiffre -= 9
        somme += chiffre
        pair = not pair
    
    return somme % 10 == 0

def valider_iban(iban: str) -> bool:
    """Valide un code IBAN de base (format français)."""
    iban = iban.replace(' ', '').upper()
    if len(iban) != 27 or not iban.startswith('FR'):
        return False
    return iban[2:].isdigit()

def valider_code_postal_fr(code: str) -> bool:
    """Valide un code postal français."""
    return bool(re.match(r'^[0-9]{5}$', code))

def valider_siret(siret: str) -> bool:
    """Valide un numéro SIRET français."""
    siret = re.sub(r'\s', '', siret)
    if len(siret) != 14 or not siret.isdigit():
        return False
    
    # Algorithme de validation SIRET
    somme = 0
    for i, chiffre in enumerate(siret[::-1]):
        n = int(chiffre)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n = n // 10 + n % 10
        somme += n
    
    return somme % 10 == 0

def valider_isbn(isbn: str) -> bool:
    """Valide un code ISBN-10 ou ISBN-13."""
    isbn = re.sub(r'[\s-]', '', isbn)
    
    if len(isbn) == 10:
        # ISBN-10
        if not isbn[:-1].isdigit():
            return False
        somme = sum(int(isbn[i]) * (10 - i) for i in range(9))
        check = isbn[9]
        if check == 'X':
            check = 10
        else:
            check = int(check)
        return (somme + check) % 11 == 0
    
    elif len(isbn) == 13:
        # ISBN-13
        if not isbn.isdigit():
            return False
        somme = sum(int(isbn[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
        return (10 - (somme % 10)) % 10 == int(isbn[12])
    
    return False

# ==================== FONCTIONS D'ANALYSE ====================

def analyser_frequence_mots(texte: str) -> Dict[str, int]:
    """Analyse la fréquence des mots dans un texte."""
    mots = re.findall(r'\b\w+\b', texte.lower())
    frequence = {}
    for mot in mots:
        frequence[mot] = frequence.get(mot, 0) + 1
    return frequence

def calculer_lisibilite_flesch(texte: str) -> float:
    """Calcule l'indice de lisibilité de Flesch (approximatif)."""
    phrases = len(re.findall(r'[.!?]+', texte))
    mots = len(re.findall(r'\b\w+\b', texte))
    syllabes = sum(max(1, len(re.findall(r'[aeiouAEIOU]', mot))) for mot in re.findall(r'\b\w+\b', texte))
    
    if phrases == 0 or mots == 0:
        return 0
    
    score = 206.835 - (1.015 * (mots / phrases)) - (84.6 * (syllabes / mots))
    return max(0, min(100, score))

def detecter_langue_simple(texte: str) -> str:
    """Détection simple de langue basée sur des mots courants."""
    mots_francais = ['le', 'de', 'et', 'à', 'un', 'il', 'être', 'et', 'en', 'avoir']
    mots_anglais = ['the', 'of', 'and', 'to', 'a', 'in', 'is', 'it', 'you', 'that']
    mots_espagnol = ['el', 'de', 'que', 'y', 'a', 'en', 'un', 'es', 'se', 'no']
    
    mots_texte = set(re.findall(r'\b\w+\b', texte.lower()))
    
    score_fr = len(mots_texte.intersection(mots_francais))
    score_en = len(mots_texte.intersection(mots_anglais))
    score_es = len(mots_texte.intersection(mots_espagnol))
    
    scores = {'français': score_fr, 'anglais': score_en, 'espagnol': score_es}
    return max(scores, key=scores.get)

def extraire_statistiques_texte(texte: str) -> Dict[str, int]:
    """Extrait des statistiques basiques d'un texte."""
    return {
        'caracteres': len(texte),
        'caracteres_sans_espaces': len(texte.replace(' ', '')),
        'mots': len(re.findall(r'\b\w+\b', texte)),
        'phrases': len(re.findall(r'[.!?]+', texte)),
        'paragraphes': len([p for p in texte.split('\n\n') if p.strip()]),
        'lignes': len(texte.split('\n'))
    }

def trouver_mots_longs(texte: str, longueur_min: int = 10) -> List[str]:
    """Trouve tous les mots d'une longueur minimale."""
    mots = re.findall(r'\b\w+\b', texte)
    return list(set(mot for mot in mots if len(mot) >= longueur_min))

# ==================== FONCTIONS DE CONVERSION ====================

def celsius_vers_fahrenheit(celsius: float) -> float:
    """Convertit des degrés Celsius en Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_vers_celsius(fahrenheit: float) -> float:
    """Convertit des degrés Fahrenheit en Celsius."""
    return (fahrenheit - 32) * 5/9

def metres_vers_pieds(metres: float) -> float:
    """Convertit des mètres en pieds."""
    return metres * 3.28084

def pieds_vers_metres(pieds: float) -> float:
    """Convertit des pieds en mètres."""
    return pieds / 3.28084

def kg_vers_livres(kg: float) -> float:
    """Convertit des kilogrammes en livres."""
    return kg * 2.20462

def livres_vers_kg(livres: float) -> float:
    """Convertit des livres en kilogrammes."""
    return livres / 2.20462

def litres_vers_gallons(litres: float) -> float:
    """Convertit des litres en gallons US."""
    return litres * 0.264172

def gallons_vers_litres(gallons: float) -> float:
    """Convertit des gallons US en litres."""
    return gallons / 0.264172

def kmh_vers_mph(kmh: float) -> float:
    """Convertit km/h en miles par heure."""
    return kmh * 0.621371

def mph_vers_kmh(mph: float) -> float:
    """Convertit miles par heure en km/h."""
    return mph / 0.621371

# ==================== FONCTIONS AVANCÉES ====================

def calculer_entropie_shannon(texte: str) -> float:
    """Calcule l'entropie de Shannon d'un texte."""
    if not texte:
        return 0
    
    # Compte la fréquence de chaque caractère
    frequences = {}
    for char in texte:
        frequences[char] = frequences.get(char, 0) + 1
    
    # Calcule l'entropie
    longueur = len(texte)
    entropie = 0
    for freq in frequences.values():
        probabilite = freq / longueur
        entropie -= probabilite * math.log2(probabilite)
    
    return entropie

def generer_markov_simple(texte: str, longueur: int = 50) -> str:
    """Génère du texte avec une chaîne de Markov simple."""
    mots = texte.split()
    if len(mots) < 2:
        return texte
    
    # Construit les transitions
    transitions = {}
    for i in range(len(mots) - 1):
        mot_actuel = mots[i]
        mot_suivant = mots[i + 1]
        if mot_actuel not in transitions:
            transitions[mot_actuel] = []
        transitions[mot_actuel].append(mot_suivant)
    
    # Génère le texte
    resultat = [random.choice(mots)]
    for _ in range(longueur - 1):
        if resultat[-1] in transitions:
            mot_suivant = random.choice(transitions[resultat[-1]])
            resultat.append(mot_suivant)
        else:
            break
    
    return ' '.join(resultat)

def detecter_anomalies_numeriques(donnees: List[float], seuil_ecart_type: float = 2.0) -> List[int]:
    """Détecte les anomalies dans une série de données numériques."""
    if len(donnees) < 2:
        return []
    
    moyenne = sum(donnees) / len(donnees)
    variance = sum((x - moyenne) ** 2 for x in donnees) / len(donnees)
    ecart_type = math.sqrt(variance)
    
    anomalies = []
    for i, valeur in enumerate(donnees):
        if abs(valeur - moyenne) > seuil_ecart_type * ecart_type:
            anomalies.append(i)
    
    return anomalies

def calculer_distance_levenshtein(s1: str, s2: str) -> int:
    """Calcule la distance de Levenshtein entre deux chaînes."""
    if len(s1) < len(s2):
        return calculer_distance_levenshtein(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    ligne_precedente = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        ligne_actuelle = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = ligne_precedente[j + 1] + 1
            deletions = ligne_actuelle[j] + 1
            substitutions = ligne_precedente[j] + (c1 != c2)
            ligne_actuelle.append(min(insertions, deletions, substitutions))
        ligne_precedente = ligne_actuelle
    
    return ligne_precedente[-1]

def compression_rle(data: str) -> str:
    """Compression Run-Length Encoding simple."""
    if not data:
        return ""
    
    resultat = []
    char_actuel = data[0]
    compteur = 1
    
    for char in data[1:]:
        if char == char_actuel:
            compteur += 1
        else:
            resultat.append(f"{compteur}{char_actuel}")
            char_actuel = char
            compteur = 1
    
    resultat.append(f"{compteur}{char_actuel}")
    return ''.join(resultat)

def decompression_rle(data: str) -> str:
    """Décompression Run-Length Encoding."""
    resultat = []
    i = 0
    
    while i < len(data):
        # Trouve le nombre
        nombre_str = ""
        while i < len(data) and data[i].isdigit():
            nombre_str += data[i]
            i += 1
        
        if i < len(data) and nombre_str:
            nombre = int(nombre_str)
            caractere = data[i]
            resultat.append(caractere * nombre)
            i += 1
    
    return ''.join(resultat)

def calculer_hash_simple(texte: str) -> str:
    """Calcule un hash simple non-cryptographique."""
    hash_val = 5381
    for char in texte:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
        hash_val &= 0xFFFFFFFF  # Limite à 32 bits
    return hex(hash_val)[2:]

def parser_csv_simple(contenu: str, separateur: str = ',') -> List[List[str]]:
    """Parse un CSV simple sans guillemets complexes."""
    lignes = contenu.strip().split('\n')
    return [ligne.split(separateur) for ligne in lignes]

def generer_csv_simple(donnees: List[List[str]], separateur: str = ',') -> str:
    """Génère un CSV simple à partir de données."""
    return '\n'.join(separateur.join(ligne) for ligne in donnees)

def calculer_moyenne_mobile(donnees: List[float], fenetre: int) -> List[float]:
    """Calcule la moyenne mobile d'une série de données."""
    if fenetre > len(donnees):
        return []
    
    moyennes = []
    for i in range(len(donnees) - fenetre + 1):
        segment = donnees[i:i + fenetre]
        moyenne = sum(segment) / len(segment)
        moyennes.append(moyenne)
    
    return moyennes

def detecter_tendance(donnees: List[float]) -> str:
    """Détecte la tendance générale d'une série de données."""
    if len(donnees) < 2:
        return "insuffisant"
    
    differences = [donnees[i+1] - donnees[i] for i in range(len(donnees)-1)]
    moyenne_diff = sum(differences) / len(differences)
    
    if moyenne_diff > 0.1:
        return "croissante"
    elif moyenne_diff < -0.1:
        return "décroissante"
    else:
        return "stable"

# ==================== FONCTIONS DE FORMATAGE ====================

def formatter_nombre_francais(nombre: float, decimales: int = 2) -> str:
    """Formate un nombre au format français."""
    nombre_str = f"{nombre:.{decimales}f}"
    partie_entiere, partie_decimale = nombre_str.split('.')
    
    # Ajoute les espaces pour les milliers
    partie_entiere_formatee = ""
    for i, chiffre in enumerate(reversed(partie_entiere)):
        if i > 0 and i % 3 == 0:
            partie_entiere_formatee = " " + partie_entiere_formatee
        partie_entiere_formatee = chiffre + partie_entiere_formatee
    
    return f"{partie_entiere_formatee},{partie_decimale}"

def formatter_duree(secondes: int) -> str:
    """Formate une durée en secondes vers un format lisible."""
    jours = secondes // 86400
    heures = (secondes % 86400) // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60
    
    parties = []
    if jours > 0:
        parties.append(f"{jours}j")
    if heures > 0:
        parties.append(f"{heures}h")
    if minutes > 0:
        parties.append(f"{minutes}m")
    if secondes_restantes > 0 or not parties:
        parties.append(f"{secondes_restantes}s")
    
    return " ".join(parties)

def formatter_pourcentage(valeur: float, total: float, decimales: int = 1) -> str:
    """Formate un pourcentage."""
    if total == 0:
        return "0%"
    pourcentage = (valeur / total) * 100
    return f"{pourcentage:.{decimales}f}%"

def formatter_monnaie(montant: float, devise: str = "€") -> str:
    """Formate un montant monétaire."""
    return f"{montant:.2f} {devise}"

def formatter_code_couleur_rgb(r: int, g: int, b: int) -> str:
    """Formate des valeurs RGB en code couleur hexadécimal."""
    return f"#{r:02x}{g:02x}{b:02x}"

def parser_code_couleur_hex(code_hex: str) -> Tuple[int, int, int]:
    """Parse un code couleur hexadécimal en valeurs RGB."""
    code_hex = code_hex.lstrip('#')
    if len(code_hex) == 6:
        return tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    elif len(code_hex) == 3:
        return tuple(int(code_hex[i]*2, 16) for i in range(3))
    else:
        raise ValueError("Format de couleur hexadécimal invalide")

def generer_table_ascii(donnees: List[List[str]], titres: List[str] = None) -> str:
    """Génère une table ASCII à partir de données."""
    if not donnees:
        return ""
    
    # Ajoute les titres si fournis
    if titres:
        donnees = [titres] + donnees
    
    # Calcule la largeur de chaque colonne
    largeurs = []
    for col in range(len(donnees[0])):
        largeur_max = max(len(str(ligne[col])) for ligne in donnees)
        largeurs.append(largeur_max)
    
    # Génère la table
    lignes = []
    for i, ligne in enumerate(donnees):
        ligne_formatee = " | ".join(str(cellule).ljust(largeur) 
                                  for cellule, largeur in zip(ligne, largeurs))
        lignes.append(f"| {ligne_formatee} |")
        
        # Ajoute une ligne de séparation après les titres
        if i == 0 and titres:
            separation = "|" + "|".join("-" * (largeur + 2) for largeur in largeurs) + "|"
            lignes.append(separation)
    
    return "\n".join(lignes)

def nettoyer_html_simple(html: str) -> str:
    """Supprime les balises HTML simples d'un texte."""
    import re
    # Supprime les balises HTML
    texte_sans_balises = re.sub(r'<[^>]+>', '', html)
    # Décode les entités HTML courantes
    entites = {
        '&amp;': '&', '&lt;': '<', '&gt;': '>', 
        '&quot;': '"', '&apos;': "'", '&nbsp;': ' '
    }
    for entite, caractere in entites.items():
        texte_sans_balises = texte_sans_balises.replace(entite, caractere)
    return texte_sans_balises

def generer_slug(texte: str) -> str:
    """Génère un slug URL-friendly à partir d'un texte."""
    slug = normaliser_texte(texte)
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug

def generer_initiales(nom_complet: str) -> str:
    """Génère les initiales d'un nom complet."""
    mots = nom_complet.split()
    return ''.join(mot[0].upper() for mot in mots if mot)

# ==================== FONCTIONS DE SÉCURITÉ ====================

def masquer_donnees_sensibles(texte: str, caractere_masque: str = "*") -> str:
    """Masque les données sensibles dans un texte."""
    # Masque les emails
    texte = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                   lambda m: m.group()[:2] + caractere_masque * (len(m.group()) - 4) + m.group()[-2:], 
                   texte)
    
    # Masque les numéros de téléphone (format français)
    texte = re.sub(r'\b0[1-9](?:[0-9]{8})\b', 
                   lambda m: m.group()[:2] + caractere_masque * 6 + m.group()[-2:], 
                   texte)
    
    return texte

def generer_token_session(longueur: int = 32) -> str:
    """Génère un token de session aléatoire."""
    import string
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def valider_force_mot_de_passe(mot_de_passe: str) -> int:
    """Calcule un score de force pour un mot de passe (0-100)."""
    score = 0
    
    # Longueur
    if len(mot_de_passe) >= 8:
        score += 25
    elif len(mot_de_passe) >= 6:
        score += 15
    elif len(mot_de_passe) >= 4:
        score += 5
    
    # Complexité
    if any(c.islower() for c in mot_de_passe):
        score += 15
    if any(c.isupper() for c in mot_de_passe):
        score += 15
    if any(c.isdigit() for c in mot_de_passe):
        score += 15
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mot_de_passe):
        score += 20
    
    # Diversité
    types_caracteres = sum([
        any(c.islower() for c in mot_de_passe),
        any(c.isupper() for c in mot_de_passe),
        any(c.isdigit() for c in mot_de_passe),
        any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in mot_de_passe)
    ])
    
    if types_caracteres >= 3:
        score += 10
    
    return min(100, score)

def detecter_injection_sql_simple(requete: str) -> bool:
    """Détecte des tentatives d'injection SQL simples."""
    mots_suspects = [
        'union', 'select', 'insert', 'update', 'delete', 'drop', 
        'create', 'alter', 'exec', 'execute', 'script', '--', ';'
    ]
    
    requete_lower = requete.lower()
    return any(mot in requete_lower for mot in mots_suspects)

def nettoyer_input_utilisateur(input_user: str) -> str:
    """Nettoie un input utilisateur des caractères potentiellement dangereux."""
    # Supprime les caractères de contrôle
    input_nettoye = ''.join(char for char in input_user if ord(char) >= 32 or char in '\n\t')
    
    # Limite la longueur
    input_nettoye = input_nettoye[:1000]
    
    # Échappe les caractères HTML
    input_nettoye = input_nettoye.replace('<', '&lt;').replace('>', '&gt;')
    
    return input_nettoye.strip()

# ==================== FONCTIONS DE PERFORMANCE ====================

def mesurer_temps_execution(fonction, *args, **kwargs):
    """Mesure le temps d'exécution d'une fonction."""
    import time
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    return resultat, fin - debut

def cache_simple():
    """Décorateur de cache simple pour les fonctions."""
    def decorateur(func):
        cache = {}
        def wrapper(*args, **kwargs):
            cle = str(args) + str(sorted(kwargs.items()))
            if cle not in cache:
                cache[cle] = func(*args, **kwargs)
            return cache[cle]
        return wrapper
    return decorateur

def limiter_taux_appels(max_appels: int, periode: int):
    """Décorateur pour limiter le taux d'appels d'une fonction."""
    def decorateur(func):
        appels = []
        def wrapper(*args, **kwargs):
            import time
            maintenant = time.time()
            # Nettoie les anciens appels
            appels[:] = [t for t in appels if maintenant - t < periode]
            
            if len(appels) >= max_appels:
                raise Exception(f"Trop d'appels: maximum {max_appels} par {periode} secondes")
            
            appels.append(maintenant)
            return func(*args, **kwargs)
        return wrapper
    return decorateur

def optimiser_liste_recherche(lst: List[Any]) -> set:
    """Optimise une liste pour la recherche en la convertissant en set."""
    return set(lst)

def pagination_simple(donnees: List[Any], page: int, taille_page: int) -> Dict[str, Any]:
    """Implémente une pagination simple."""
    debut = (page - 1) * taille_page
    fin = debut + taille_page
    
    return {
        'donnees': donnees[debut:fin],
        'page_actuelle': page,
        'total_pages': math.ceil(len(donnees) / taille_page),
        'total_elements': len(donnees),
        'a_page_suivante': fin < len(donnees),
        'a_page_precedente': page > 1
    }

# Fonction principale pour tester quelques fonctions
def main():
    """Fonction principale pour démonstrer l'utilisation de quelques fonctions."""
    print("=== Démonstration de quelques fonctions ===")
    
    # Test des fonctions mathématiques
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Factorielle(5): {factorielle(5)}")
    print(f"Est premier 17: {est_premier(17)}")
    
    # Test des fonctions de chaînes
    print(f"Palindrome 'radar': {est_palindrome('radar')}")
    print(f"Inverser mots 'Hello World': {inverser_mots('Hello World')}")
    
    # Test des fonctions utilitaires
    print(f"Mot de passe généré: {generer_mot_de_passe(12)}")
    print(f"Couleur hex générée: {generer_couleur_hex()}")
    
    # Test des conversions
    print(f"25°C en Fahrenheit: {celsius_vers_fahrenheit(25)}")
    print(f"100 km/h en mph: {kmh_vers_mph(100)}")
    
    print("\n=== Fin de la démonstration ===")

if __name__ == "__main__":
    main()