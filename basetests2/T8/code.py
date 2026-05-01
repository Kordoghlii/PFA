def reverse_string(s):
    """Reverse the input string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    # Count vowels in string
    vowels = "aeiou"
    return sum(1 for c in s.lower() if c in vowels)

def capitalize_words(s):
    """Capitalize each word in the string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with each word capitalized.
    """
    return " ".join(word.capitalize() for word in s.split())

def remove_duplicates(s):
    return "".join(dict.fromkeys(s))

def longest_word(s):
    """Find the longest word in the string.

    Args:
        s (str): The input string.

    Returns:
        str: The longest word, or empty string if input is empty.
    """
    words = s.split()
    return max(words, key=len, default="")

def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

def is_substring(sub, s):
    # Check if sub is in s
    return sub in s

def replace_spaces(s):
    """Replace spaces with underscores.

    Args:
        s (str): The input string.

    Returns:
        str: The string with spaces replaced by underscores.
    """
    return s.replace(" ", "_")

def truncate(s, n):
    return s[:n] if len(s) > n else s