def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def capitalize_words(s):
    # Capitalise chaque mot
    return ' '.join(word.capitalize() for word in s.split())

def remove_duplicates(s):
    seen = set()
    return ''.join(c for c in s if not (c in seen or seen.add(c)))

def find_substring(s, sub):
    return s.find(sub)

def replace_chars(s, old, new):
    return s.replace(old, new)

def split_into_words(s):
    return s.split()

def longest_word(s):
    words = s.split()
    return max(words, key=len, default="") if words else ""

def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq