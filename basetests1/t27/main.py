import random
import re
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
import json
def inverser_dictionnaire(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Inverse les clés et valeurs d'un dictionnaire."""
    # Vérifie si le dictionnaire est vide
    return {v: k for k, v in d.items()}

def fusionner_dictionnaires(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Fusionne deux dictionnaires."""
    # Vérifie si les deux dictionnaires sont vides
    resultat = d1.copy()
    resultat.update(d2)
    return resultat

def filtrer_dictionnaire(d: Dict[str, Any], condition) -> Dict[str, Any]:
    """Filtre un dictionnaire selon une condition."""
    # Vérifie si la condition est une fonction
    return {k: v for k, v in d.items() if condition(k, v)}

def compter_valeurs(d: Dict[Any, Any]) -> Dict[Any, int]:
    #Validation de la fonction
    """Compte les occurrences de chaque valeur dans un dictionnaire."""
    compteur = {}
    for valeur in d.values():
        compteur[valeur] = compteur.get(valeur, 0) + 1
    return compteur

def dictionnaire_vers_liste_tuples(d: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
    #Validation de la fonction
    """Convertit un dictionnaire en liste de tuples."""
    return list(d.items())

def liste_tuples_vers_dictionnaire(lst: List[Tuple[Any, Any]]) -> Dict[Any, Any]:
    #Validation de la fonction
    """Convertit une liste de tuples en dictionnaire."""
    return dict(lst)

def obtenir_cles_par_valeur(d: Dict[Any, Any], valeur: Any) -> List[Any]:
    #Validation de la fonction
    """Obtient toutes les clés ayant une valeur donnée."""
    return [k for k, v in d.items() if v == valeur]

def dictionnaire_profond_get(d: Dict[str, Any], chemin: str, separateur: str = '.') -> Any:
    """Obtient une valeur dans un dictionnaire imbriqué."""
    #Validation de la fonction
    cles = chemin.split(separateur)
    resultat = d
    for cle in cles:
        if isinstance(resultat, dict) and cle in resultat:
            resultat = resultat[cle]
        else:
            return None
    return resultat

def aplatir_dictionnaire(d: Dict[str, Any], separateur: str = '.') -> Dict[str, Any]:
    #Validation de la fonction
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
    #Verification de la valeur 
    """Ajoute des valeurs par défaut à un dictionnaire."""
    resultat = defauts.copy()
    resultat.update(d)
    return resultat


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