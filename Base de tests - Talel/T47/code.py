# utils_string.py

def to_uppercase(text):
    """
    Convert a string to uppercase.

    Args:
        text (str): Input string.

    Returns:
        str: Uppercase version of the string.
    """
    # Using upper() to convert text to uppercase
    return text.upper()

def to_lowercase(text):
    """
    Convert a string to lowercase.

    Args:
        text (str): Input string.

    Returns:
        str: Lowercase version of the string.
    """
    # Using lower() to convert text to lowercase
    return text.lower()

def count_words(text):
    """
    Count the number of words in a string.

    Args:
        text (str): Input string.

    Returns:
        int: Number of words in the string.
    """
    # Splitting by whitespace
    return len(text.split())

def reverse_string(text):
    """
    Reverse the characters in a string.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    # Using slicing to reverse the string
    return text[::-1]

def is_palindrome(text):
    """
    Check if a string is a palindrome.

    Args:
        text (str): Input string.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Normalize the string by lowering case and removing spaces
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_punctuation(text):
    """
    Remove all punctuation from a string.

    Args:
        text (str): Input string.

    Returns:
        str: String without punctuation.
    """
    # Remove characters that are not alphanumeric or space
    import string
    return ''.join(char for char in text if char not in string.punctuation)

def capitalize_words(text):
    """
    Capitalize the first letter of each word in a string.

    Args:
        text (str): Input string.

    Returns:
        str: Capitalized string.
    """
    # Using title() method
    return text.title()

def count_vowels(text):
    """
    Count the number of vowels in a string.

    Args:
        text (str): Input string.

    Returns:
        int: Number of vowels.
    """
    # Count vowels using list comprehension
    return sum(1 for char in text.lower() if char in 'aeiou')

def contains_number(text):
    """
    Check if a string contains any digits.

    Args:
        text (str): Input string.

    Returns:
        bool: True if contains digits, False otherwise.
    """
    # Check for any digit in text
    return any(char.isdigit() for char in text)

def remove_spaces(text):
    """
    Remove all spaces from a string.

    Args:
        text (str): Input string.

    Returns:
        str: String without spaces.
    """
    # Remove all space characters
    return text.replace(" ", "")
