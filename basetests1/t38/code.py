# string_utilities.py

def to_uppercase(text):
    """Transforme toute la chaîne en majuscules."""
    return text.upper()

def word_count(text):
    return len(text.split())

def reverse_words(text):
    """Inverse l'ordre des mots dans la chaîne."""
    return ' '.join(text.split()[::-1])

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def concatenate_strings(a, b):
    """Concatène deux chaînes et les sépare par un espace."""
    return a + " " + b

def first_letters(text):
    return ''.join([word[0] for word in text.split()])

def repeat_string(text, n):
    """Répète la chaîne text, n fois."""
    return text * n

def remove_vowels(text):
    return ''.join([char for char in text if char.lower() not in 'aeiou'])

def longest_word(text):
    """Retourne le mot le plus long dans la chaîne."""
    return max(text.split(), key=len) if text else ''
