def caesar_encrypt(text, shift):
    """Encrypt text using a Caesar cipher.

    Args:
        text (str): Input text to encrypt.
        shift (int): Number of positions to shift.

    Returns:
        str: Encrypted text.
    """
    # Encrypt text with Caesar cipher
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    # Decrypt text with Caesar cipher
    return caesar_encrypt(text, -shift)

def is_letter(char):
    # Check if character is a letter
    return char.isalpha()

def count_letters(text):
    # Count letters in text
    return sum(1 for c in text if c.isalpha())

def reverse_text(text):
    """Reverse the input text.

    Args:
        text (str): Input text.

    Returns:
        str: Reversed text.
    """
    # Reverse the text
    return text[::-1]

def to_ascii(text):
    # Convert text to ASCII values
    return [ord(c) for c in text]

def from_ascii(numbers):
    # Convert ASCII values to text
    return ''.join(chr(n) for n in numbers)

def is_palindrome(text):
    # Check if text is a palindrome (ignoring case and non-letters)
    cleaned = ''.join(c.lower() for c in text if c.isalpha())
    return cleaned == cleaned[::-1]

def letter_frequency(text):
    """Calculate frequency of letters in text.

    Args:
        text (str): Input text.

    Returns:
        dict: Dictionary with letter counts (case-insensitive).
    """
    # Calculate letter frequency
    freq = {}
    for c in text.lower():
        if c.isalpha():
            freq[c] = freq.get(c, 0) + 1
    return freq

def simple_hash(text):
    # Calculate a simple hash of text
    hash_value = 0
    for c in text:
        hash_value = (hash_value * 31 + ord(c)) % 1000000
    return hash_value