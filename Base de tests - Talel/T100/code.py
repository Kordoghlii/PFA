import os

def create_file(filename, content=""):
    """
    Crée un fichier avec un contenu donné.
    
    Args:
        filename (str): Le nom du fichier à créer.
        content (str): Le contenu initial du fichier (par défaut une chaîne vide).
    
    Returns:
        bool: True si le fichier a été créé avec succès, sinon False.
    """
    # Création du fichier avec le contenu spécifié
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Erreur lors de la création du fichier: {e}")
        return False

def read_file(filename):
    """
    Lit le contenu d'un fichier.
    
    Args:
        filename (str): Le nom du fichier à lire.
    
    Returns:
        str: Le contenu du fichier.
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    # Lecture du fichier
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas")
    with open(filename, 'r') as file:
        return file.read()

def append_to_file(filename, content):
    """
    Ajoute du contenu à un fichier existant.
    
    Args:
        filename (str): Le nom du fichier.
        content (str): Le contenu à ajouter.
    
    Returns:
        bool: True si le contenu a été ajouté avec succès, sinon False.
    """
    # Ajout de contenu au fichier existant
    try:
        with open(filename, 'a') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Erreur lors de l'ajout au fichier: {e}")
        return False

def delete_file(filename):
    """
    Supprime un fichier.
    
    Args:
        filename (str): Le nom du fichier à supprimer.
    
    Returns:
        bool: True si le fichier a été supprimé avec succès, sinon False.
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    # Suppression du fichier
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas")
    try:
        os.remove(filename)
        return True
    except Exception as e:
        print(f"Erreur lors de la suppression du fichier: {e}")
        return False

def create_directory(directory):
    """
    Crée un répertoire.
    
    Args:
        directory (str): Le chemin du répertoire à créer.
    
    Returns:
        bool: True si le répertoire a été créé avec succès, sinon False.
    """
    # Création du répertoire
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        print(f"Erreur lors de la création du répertoire: {e}")
        return False

def list_files_in_directory(directory):
    """
    Liste les fichiers dans un répertoire donné.
    
    Args:
        directory (str): Le chemin du répertoire à explorer.
    
    Returns:
        list: Une liste des fichiers dans le répertoire.
    
    Raises:
        FileNotFoundError: Si le répertoire n'existe pas.
    """
    # Vérification que le répertoire existe
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Le répertoire {directory} n'existe pas")
    return os.listdir(directory)

def check_file_exists(filename):
    """
    Vérifie si un fichier existe.
    
    Args:
        filename (str): Le nom du fichier à vérifier.
    
    Returns:
        bool: True si le fichier existe, sinon False.
    """
    # Vérification de l'existence du fichier
    return os.path.exists(filename)

def move_file(source, destination):
    """
    Déplace un fichier d'un endroit à un autre.
    
    Args:
        source (str): Le chemin source du fichier.
        destination (str): Le chemin de destination du fichier.
    
    Returns:
        bool: True si le fichier a été déplacé avec succès, sinon False.
    
    Raises:
        FileNotFoundError: Si le fichier source n'existe pas.
    """
    # Vérification que le fichier source existe
    if not os.path.exists(source):
        raise FileNotFoundError(f"Le fichier source {source} n'existe pas")
    try:
        os.rename(source, destination)
        return True
    except Exception as e:
        print(f"Erreur lors du déplacement du fichier: {e}")
        return False

def get_file_size(filename):
    """
    Obtient la taille d'un fichier en octets.
    
    Args:
        filename (str): Le nom du fichier.
    
    Returns:
        int: La taille du fichier en octets.
    
    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    # Vérification que le fichier existe
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'existe pas")
    return os.path.getsize(filename)

def get_directory_size(directory):
    """
    Calcule la taille totale des fichiers dans un répertoire.
    
    Args:
        directory (str): Le chemin du répertoire.
    
    Returns:
        int: La taille totale en octets des fichiers dans le répertoire.
    
    Raises:
        FileNotFoundError: Si le répertoire n'existe pas.
    """
    # Vérification que le répertoire existe
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Le répertoire {directory} n'existe pas")
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size
