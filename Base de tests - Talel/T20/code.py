def count_letters(text):
    """Count the number of alphabetic characters in text.

    Args:
        text (str): Input text.

    Returns:
        int: Number of alphabetic characters.
    """
    # Count alphabetic characters
    return sum(c.isalpha() for c in text)

def count_digits(text):
    # Count digit characters
    return sum(c.isdigit() for c in text)

def count_spaces(text):
    # Count space characters
    return sum(c.isspace() for c in text)

def count_punctuation(text):
    """Count punctuation characters in text.

    Args:
        text (str): Input text.

    Returns:
        int: Number of punctuation characters.
    """
    # Count punctuation characters
    import string
    return sum(c in string.punctuation for c in text)

def average_word_length(text):
    # Calculate average word length
    words = text.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def longest_word_length(text):
    # Find length of longest word
    words = text.split()
    return max(len(word) for word in words) if words else 0

def shortest_word_length(text):
    """Find length of shortest word in text.

    Args:
        text (str): Input text.

    Returns:
        int: Length of shortest word, or 0 if empty.
    """
    # Find length of shortest word
    words = text.split()
    return min(len(word) for word in words) if words else 0

def count_unique_words(text):
    # Count unique words (case-insensitive)
    words = text.lower().split()
    return len(set(words))

def most_common_char(text):
    # Find most common character (excluding spaces)
    from collections import Counter
    chars = [c for c in text.lower() if not c.isspace()]
    return Counter(chars).most_common(1)[0][0] if chars else ""

def has_special_chars(text):
    """Check if text contains special characters.

    Args:
        text (str): Input text.

    Returns:
        bool: True if special characters are present, False otherwise.
    """
    # Check for special characters
    import string
    return any(c in string.punctuation for c in text)