def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def variance(numbers):
    # Calcule la variance
    if not numbers:
        return 0
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5

def min_value(numbers):
    return min(numbers) if numbers else 0

def max_value(numbers):
    return max(numbers) if numbers else 0

def range_value(numbers):
    return max_value(numbers) - min_value(numbers)

def count_outliers(numbers):
    if not numbers:
        return 0
    m, sd = mean(numbers), standard_deviation(numbers)
    return sum(1 for x in numbers if abs(x - m) > 2 * sd)

def sum_numbers(numbers):
    return sum(numbers)

def frequency(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    return freq