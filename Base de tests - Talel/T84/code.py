"""
Module for list manipulation operations.
"""

def sum_list(numbers: list) -> float:
    """
    Compute the sum of a list of numbers.
    
    Args:
        numbers (list): List of numbers.
    
    Returns:
        float: Sum of the list.
    """
    return sum(numbers)

def average_list(numbers: list) -> float:
    """
    Compute the average of a list of numbers.
    
    Args:
        numbers (list): List of numbers.
    
    Returns:
        float: Average of the list.
    """
    return sum(numbers) / len(numbers)

def max_in_list(numbers: list) -> float:
    """
    Find the maximum value in a list.
    
    Args:
        numbers (list): List of numbers.
    
    Returns:
        float: Maximum value.
    """
    return max(numbers)

def min_in_list(numbers: list) -> float:
    """
    Find the minimum value in a list.
    
    Args:
        numbers (list): List of numbers.
    
    Returns:
        float: Minimum value.
    """
    return min(numbers)

def reverse_list(lst: list) -> list:
    """
    Reverse a list.
    
    Args:
        lst (list): Input list.
    
    Returns:
        list: Reversed list.
    """
    return lst[::-1]

def flatten_list(nested_list: list) -> list:
    """
    Flatten a nested list.
    
    Args:
        nested_list (list): Nested list.
    
    Returns:
        list: Flattened list.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def remove_duplicates(lst: list) -> list:
    """
    Remove duplicates from a list.
    
    Args:
        lst (list): Input list.
    
    Returns:
        list: List without duplicates.
    """
    return list(set(lst))

def count_occurrences(lst: list, element) -> int:
    """
    Count occurrences of an element in a list.
    
    Args:
        lst (list): Input list.
        element: Element to count.
    
    Returns:
        int: Number of occurrences.
    """
    return lst.count(element)

def merge_lists(*args: list) -> list:
    """
    Merge multiple lists into one.
    
    Args:
        *args (list): Lists to merge.
    
    Returns:
        list: Merged list.
    """
    merged = []
    for lst in args:
        merged.extend(lst)
    return merged

def rotate_list(lst: list, n: int) -> list:
    """
    Rotate a list by n positions.
    
    Args:
        lst (list): Input list.
        n (int): Number of positions to rotate.
    
    Returns:
        list: Rotated list.
    """
    n = n % len(lst)
    return lst[-n:] + lst[:-n]