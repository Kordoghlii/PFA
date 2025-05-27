import pytest
from list_operations import *

def test_sum_list():
    assert sum_list([1, 2, 3]) == 6

def test_average_list():
    assert average_list([1, 2, 3]) == 2

def test_max_in_list():
    assert max_in_list([4, 1, 7]) == 7

def test_min_in_list():
    assert min_in_list([4, 1, 7]) == 1

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]

def test_flatten_list():
    assert flatten_list([[1, 2], [3, [4]]]) == [1, 2, 3, 4]

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]

def test_count_occurrences():
    assert count_occurrences([1, 2, 2, 3], 2) == 2

def test_merge_lists():
    assert merge_lists([1, 2], [3, 4]) == [1, 2, 3, 4]

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4], 2) == [3, 4, 1, 2]