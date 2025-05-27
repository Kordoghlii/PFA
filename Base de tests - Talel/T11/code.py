def count_words(text):
    """Count the number of words in a text.

    Args:
        text (str): The input text.

    Returns:
        int: The number of words.
    """
    return len(text.split())

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    # Convert text to lowercase
    return text.lower()

def count_chars(text):
    """Count the number of characters (excluding spaces).

    Args:
        text (str): The input text.

    Returns:
        int: The number of non-space characters.
    """
    return len(text.replace(" ", ""))

def remove_punctuation(text):
    import string
    return text.translate(str.maketrans("", "", string.punctuation))

def split_sentences(text):
    """Split text into sentences.

    Args:
        text (str): The input text.

    Returns:
        list: List of sentences.
    """
    import re
    return re.split(r'[.!?]+', text.strip())

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def trim_whitespace(text):
    # Remove leading and trailing whitespace
    return text.strip()

def is_all_digits(text):
    return text.isdigit()

def replace_word(text, old, new):
    """Replace all occurrences of a word.

    Args:
        text (str): The input text.
        old (str): The word to replace.
        new (str): The replacement word.

    Returns:
        str: The text with replaced words.
    """
    return text.replace(old, new)