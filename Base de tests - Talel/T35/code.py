"""
Module for string manipulation operations.
"""

def reverse_string(s: str) -> str:
    """
    Reverse a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        str: Reversed string.
    """
    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        int: Number of vowels.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        s (str): Input string.
    
    Returns:
        bool: True if palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        str: String with words capitalized.
    """
    return ' '.join(word.capitalize() for word in s.split())

def replace_substring(s: str, old: str, new: str) -> str:
    """
    Replace all occurrences of a substring in a string.
    
    Args:
        s (str): Original string.
        old (str): Substring to replace.
        new (str): New substring.
    
    Returns:
        str: Modified string.
    """
    return s.replace(old, new)

def count_words(s: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        int: Number of words.
    """
    return len(s.split())

def remove_whitespace(s: str) -> str:
    """
    Remove all whitespace from a string.
    
    Args:
        s (str): Input string.
    
    Returns:
        str: String without whitespace.
    """
    return s.replace(" ", "")

def find_substring(s: str, sub: str) -> int:
    """
    Find the index of the first occurrence of a substring.
    
    Args:
        s (str): Main string.
        sub (str): Substring to find.
    
    Returns:
        int: Index of substring, or -1 if not found.
    """
    return s.find(sub)

def concatenate_strings(*args: str) -> str:
    """
    Concatenate multiple strings.
    
    Args:
        *args (str): Strings to concatenate.
    
    Returns:
        str: Concatenated string.
    """
    return ''.join(args)

def split_string(s: str, delimiter: str) -> list:
    """
    Split a string using a delimiter.
    
    Args:
        s (str): Input string.
        delimiter (str): Delimiter for splitting.
    
    Returns:
        list: List of substrings.
    """
    return s.split(delimiter)