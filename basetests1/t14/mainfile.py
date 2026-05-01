import os
import json
import logging
import re
from datetime import datetime
from typing import Dict, Any

def read_json_file(filepath: str) -> Dict[str, Any]:
    """
    Lit un fichier JSON et renvoie son contenu sous forme de dictionnaire.

    Args:
        filepath (str): Le chemin du fichier JSON à lire.

    Returns:
        dict: Le contenu du fichier JSON sous forme de dictionnaire.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        json.JSONDecodeError: Si le fichier n'est pas un JSON valide.
    """
    # Ouverture du fichier JSON en mode lecture
    with open(filepath, 'r') as file:
        # Retourne le contenu du fichier sous forme de dictionnaire
        return json.load(file)


def write_json_file(filepath: str, data: Dict[str, Any]) -> None:
    """
    Écrit un dictionnaire sous forme de JSON dans un fichier.

    Args:
        filepath (str): Le chemin du fichier où écrire les données.
        data (dict): Le dictionnaire à écrire dans le fichier.

    Raises:
        IOError: Si une erreur survient lors de l'écriture du fichier.
    """
    # Ouverture du fichier en mode écriture
    with open(filepath, 'w') as file:
        # Sérialisation du dictionnaire en JSON et écriture dans le fichier
        json.dump(data, file, indent=4)


def get_file_size(filepath: str) -> int:
    """
    Renvoie la taille d'un fichier en octets.

    Args:
        filepath (str): Le chemin du fichier.

    Returns:
        int: La taille du fichier en octets.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    # Utilisation de la fonction os pour obtenir la taille du fichier en octets
    return os.path.getsize(filepath)


def create_logger(name: str, level: int) -> logging.Logger:
    """
    Crée un logger pour le projet avec un niveau de log spécifique.

    Args:
        name (str): Le nom du logger.
        level (int): Le niveau de log (par exemple, logging.DEBUG).

    Returns:
        logging.Logger: Le logger configuré.
    """
    # Création d'un logger avec le nom spécifié
    logger = logging.getLogger(name)
    # Définition du niveau de log
    logger.setLevel(level)
    # Création d'un handler pour afficher les logs dans la console
    handler = logging.StreamHandler()
    # Définition du format du message de log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Ajout du handler au logger
    logger.addHandler(handler)
    return logger


def slugify(text: str) -> str:
    """
    Convertit une chaîne de caractères en un format 'slug' (exemple: 'Hello World' -> 'hello-world').

    Args:
        text (str): Le texte à convertir.

    Returns:
        str: La version slugifiée de la chaîne d'entrée.
    """
    # Supprime les espaces excessifs et convertit tout le texte en minuscules
    return re.sub(r'\s+', '-', text.strip().lower())


def is_valid_url(url: str) -> bool:
    """
    Vérifie si une chaîne est une URL valide.

    Args:
        url (str): L'URL à vérifier.

    Returns:
        bool: True si l'URL est valide, False sinon.
    """
    # Définition d'une expression régulière pour valider l'URL
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// ou https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domaine
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ou IP
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ou IPv6
        r'(?::\d+)?' # port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    # Retourne True si l'URL correspond à l'expression régulière
    return re.match(regex, url) is not None


def format_datetime_iso(dt: datetime) -> str:
    """
    Formate un objet datetime en une chaîne ISO 8601 (ex: '2025-04-25T14:45:00').

    Args:
        dt (datetime): L'objet datetime à formater.

    Returns:
        str: La chaîne ISO 8601.
    """
    # Utilisation de la méthode isoformat() pour formater l'objet datetime
    return dt.isoformat()


def parse_datetime_iso(dt_str: str) -> datetime:
    """
    Analyse une chaîne ISO 8601 et la convertit en un objet datetime.

    Args:
        dt_str (str): La chaîne à analyser (format ISO 8601).

    Returns:
        datetime: L'objet datetime correspondant.
    
    Raises:
        ValueError: Si la chaîne n'est pas au format ISO 8601 valide.
    """
    # Utilisation de la méthode fromisoformat() pour convertir la chaîne en datetime
    return datetime.fromisoformat(dt_str)


def ensure_directory(path: str) -> None:
    """
    Crée un dossier si celui-ci n'existe pas.

    Args:
        path (str): Le chemin du dossier à créer.

    Raises:
        OSError: Si une erreur se produit lors de la création du dossier.
    """
    # Vérification si le dossier n'existe pas
    if not os.path.exists(path):
        # Création du dossier avec os.makedirs()
        os.makedirs(path)


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Aplatie un dictionnaire imbriqué en un seul niveau avec des clés concaténées.

    Args:
        d (dict): Le dictionnaire à aplatir.
        parent_key (str): Le préfixe de la clé.
        sep (str): Le séparateur entre les clés.

    Returns:
        dict: Le dictionnaire aplati avec des clés combinées.
    """
    items = []  # Liste pour stocker les éléments aplatis
    for k, v in d.items():
        # Création d'une nouvelle clé en concaténant le parent_key avec la clé courante
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):  # Si la valeur est un dictionnaire
            # Appel récursif pour aplatir les sous-dictionnaires
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            # Ajout de la clé et de la valeur dans la liste
            items.append((new_key, v))
    # Retour du dictionnaire aplati
    return dict(items)
