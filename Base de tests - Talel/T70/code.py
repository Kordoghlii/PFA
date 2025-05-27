def mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The mean of the numbers, or 0 if the list is empty.
    """
    # Calculate mean of numbers
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    # Calculate median of numbers
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def variance(numbers):
    """Calculate the variance of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The variance, or 0 if the list is empty.
    """
    # Calculate variance
    if not numbers:
        return 0
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    # Calculate standard deviation
    import math
    return math.sqrt(variance(numbers))

def min_value(numbers):
    # Return minimum value
    return min(numbers) if numbers else None

def max_value(numbers):
    """Return the maximum value in a list.

    Args:
        numbers (list): List of numbers.

    Returns:
        float or None: The maximum value, or None if the list is empty.
    """
    # Return maximum value
    return max(numbers) if numbers else None

def range_values(numbers):
    # Calculate range (max - min)
    if not numbers:
        return 0
    return max(numbers) - min(numbers)

def count_values(numbers, value):
    # Count occurrences of a value
    return numbers.count(value)

def sum_values(numbers):
    """Calculate the sum of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The sum of the numbers.
    """
    # Sum all numbers
    return sum(numbers)

def is_sorted_ascending(numbers):
    # Check if list is sorted in ascending order
    return numbers == sorted(numbers)