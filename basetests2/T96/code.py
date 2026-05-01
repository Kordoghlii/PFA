# utils_list.py

def get_max(lst):
    """
    Return the maximum value in a list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int or float: Maximum value in the list.
    """
    # Use max() to get maximum
    return max(lst)

def get_min(lst):
    """
    Return the minimum value in a list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int or float: Minimum value in the list.
    """
    # Use min() to get minimum
    return min(lst)

def list_sum(lst):
    """
    Return the sum of elements in a list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int or float: Sum of the list elements.
    """
    # Use sum() to calculate total
    return sum(lst)

def unique_elements(lst):
    """
    Return the unique elements in a list.

    Args:
        lst (list): Input list.

    Returns:
        list: List of unique elements.
    """
    # Use set to remove duplicates
    return list(set(lst))

def count_occurrences(lst, value):
    """
    Count how many times a value appears in a list.

    Args:
        lst (list): Input list.
        value: Value to count.

    Returns:
        int: Number of occurrences.
    """
    # Use count() method
    return lst.count(value)

def flatten(nested_list):
    """
    Flatten a nested list (one level).

    Args:
        nested_list (list): List of lists.

    Returns:
        list: Flattened list.
    """
    # Use list comprehension to flatten
    return [item for sublist in nested_list for item in sublist]

def remove_duplicates(lst):
    """
    Remove duplicate values while preserving order.

    Args:
        lst (list): Input list.

    Returns:
        list: List without duplicates.
    """
    # Use set with a loop to preserve order
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def sort_list(lst):
    """
    Return a sorted version of the list.

    Args:
        lst (list): Input list.

    Returns:
        list: Sorted list.
    """
    # Use sorted()
    return sorted(lst)

def list_difference(lst1, lst2):
    """
    Return the difference of two lists (elements in lst1 not in lst2).

    Args:
        lst1 (list): First list.
        lst2 (list): Second list.

    Returns:
        list: Difference between lst1 and lst2.
    """
    # Use list comprehension
    return [item for item in lst1 if item not in lst2]

def chunk_list(lst, size):
    """
    Split list into chunks of given size.

    Args:
        lst (list): Input list.
        size (int): Chunk size.

    Returns:
        list: List of chunks.
    """
    # Use list slicing with step
    return [lst[i:i + size] for i in range(0, len(lst), size)]

