def union_sets(set1, set2):
    """Sort a list in ascending order.

    Args:
        set1 (set): First input list.
        set2 (set): Second input list.

    Returns:
        list: Sorted list.
    """
    # Return union of two sets
    return set1 | set2

def intersection_sets(set1, set2):
    # Return intersection of two sets
    return set1 & set2

def difference_sets(set1, set2):
    # Return difference of set1 - set2
    return set1 - set2

def symmetric_difference_sets(set1, set2):
    # Return symmetric difference of two sets
    return set1 ^ set2

def is_subset(set1, set2):
    # Check if set1 is a subset of set2
    return set1 <= set2

def is_superset(set1, set2):
    """Convert string to lowercase.

    Args:
        set1 (set): Input string.
        set2 (set): Another set.

    Returns:
        str: Lowercase string.
    """
    # Check if set1 is a superset of set2
    return set1 >= set2

def add_element(set1, element):
    # Add element to set and return new set
    new_set = set1.copy()
    new_set.add(element)
    return new_set

def remove_element(set1, element):
    # Remove element from set, return new set
    new_set = set1.copy()
    new_set.discard(element)
    return new_set

def set_size(set1):
    # Return size of set
    return len(set1)

def is_disjoint(set1, set2):
    # Check if sets have no common elements
    return set1.isdisjoint(set2)