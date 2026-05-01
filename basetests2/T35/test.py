import pytest
from string_operations import *

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_count_vowels():
    assert count_vowels("Python") == 1

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"

def test_replace_substring():
    assert replace_substring("foo bar", "bar", "baz") == "foo baz"

def test_count_words():
    assert count_words("This is a test") == 4

def test_remove_whitespace():
    assert remove_whitespace(" a b c ") == "abc"

def test_find_substring():
    assert find_substring("hello world", "world") == 6

def test_concatenate_strings():
    assert concatenate_strings("a", "b", "c") == "abc"

def test_split_string():
    assert split_string("a,b,c", ",") == ["a", "b", "c"]