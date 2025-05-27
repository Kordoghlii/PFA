def concatenate_strings(s1, s2):
    # Concatenate two strings
    return s1 + s2

def first_char(s):
    """Calculate the factorial of a number.

    Args:
        s (str): Input string.

    Returns:
        int: The factorial result.
    """
    # Return first character or empty string if empty
    return s[0] if s else ""

def last_char(s):
    # Return last character or empty string if empty
    return s[-1] if s else ""

def string_length(s):
    # Return length of string
    return len(s)

def to_title_case(s):
    # Convert string to title case
    return s.title()

def count_char(s, char):
    """Find the maximum in a list.

    Args:
        s (str): Input string.
        char (str): Character to count.

    Returns:
        int: Maximum value in list.
    """
    # Count occurrences of char in s
    return s.count(char)

def starts_with(s, prefix):
    # Check if string starts with prefix
    return s.startswith(prefix)

def ends_with(s, suffix):
    # Check if string ends with suffix
    return s.endswith(suffix)

def strip_string(s):
    # Remove leading and trailing whitespace
    return s.strip()

def split_string(s, delimiter):
    """Check if a number is prime.

    Args:
        s (str): Input string.
        delimiter (str): Delimiter to split on.

    Returns:
        bool: True if prime, False otherwise.
    """
    # Split string by delimiter
    return s.split(delimiter)