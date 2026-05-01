def find_max(lst):
    """Return the maximum value in the list.

    Args:
        lst (list): The input list.

    Returns:
        any or None: The maximum value, or None if list is empty.
    """
    return max(lst) if lst else None

def find_min(lst):
    return min(lst) if lst else None

def list_sum(lst):
    # Sum all elements
    return sum(lst)

def list_average(lst):
    """Calculate average of list elements.

    Args:
        lst (list): The input list.

    Returns:
        float: The average of elements, or 0 if list is empty.
    """
    return sum(lst) / len(lst) if lst else 0

def remove_duplicates_list(lst):
    return list(dict.fromkeys(lst))

def reverse_list(lst):
    """Reverse the input list.

    Args:
        lst (list): The input list.

    Returns:
        list: The reversed list.
    """
    return lst[::-1]

def sort_list(lst):
    # Sort list in ascending order
    return sorted(lst)

def is_sorted(lst):
    return lst == sorted(lst)

def merge_lists(lst1, lst2):
    """Merge two lists and sort the result.

    Args:
        lst1 (list): First input list.
        lst2 (list): Second input list.

    Returns:
        list: Sorted merged list.
    """
    return sorted(lst1 + lst2)

def chunk_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]