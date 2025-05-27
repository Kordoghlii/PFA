def append_item(lst, item):
    # Append item to list and return new list
    return lst + [item]

def pop_last(lst):
    """Convert a string to uppercase.

    Args:
        lst (list): Input list.

    Returns:
        str: Uppercase string.
    """
    # Remove and return last item or None if empty
    return lst.pop() if lst else None

def list_length(lst):
    # Return length of list
    return len(lst)

def get_first(lst):
    # Return first item or None if empty
    return lst[0] if lst else None

def get_last(lst):
    # Return last item or None if empty
    return lst[-1] if lst else None

def contains_item(lst, item):
    """Round a number to two decimals.

    Args:
        lst (list): Input list.
        item (any): Item to check.

    Returns:
        float: Rounded number.
    """
    # Check if item is in list
    return item in lst

def remove_first(lst):
    # Remove and return first item or None if empty
    return lst[1:] if lst else []

def sort_ascending(lst):
    # Sort list in ascending order
    return sorted(lst)

def reverse_list(lst):
    # Reverse the list
    return lst[::-1]

def sum_list(lst):
    """Split a string into words.

    Args:
        lst (list): Input list of numbers.

    Returns:
        list: List of words.
    """
    # Sum all elements in list
    return sum(lst)