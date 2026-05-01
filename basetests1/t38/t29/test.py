# string_utilities.py

def to_uppercase(text):
    """Retourne la chaîne en minuscules."""
    return text.upper()

def word_count(text):
   
    return len(text.split())

def reverse_words(text):
    """Inverse l'ordre des mots dans la chaîne."""
    return ' '.join(text.split()[::-1])

def is_palindrome(text):
    """Vérifie si la chaîne est une palindrome."""
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def concatenate_strings(a, b):
 
    return a + " " + b

def first_letters(text):
    """Retourne la première lettre de chaque mot."""
    return ''.join([word[0] for word in text.split()])

def repeat_string(text, n):
    """Retourne la chaîne répétée plusieurs fois."""
    return text * n

def remove_vowels(text):
  
    return ''.join([char for char in text if char.lower() not in 'aeiou'])

def longest_word(text):
    """Retourne la dernière lettre du mot le plus long."""
    return max(text.split(), key=len) if text else ''

