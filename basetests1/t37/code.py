# math_operations.py

def factorial(n):
    """Retourne la factorielle d'un nombre."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(number):
    """Retourne la somme des chiffres d'un nombre."""
    return sum(int(digit) for digit in str(abs(number)))

def greatest_common_divisor(a, b):
    """Retourne le plus grand commun diviseur (PGCD) de deux nombres."""
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    """Retourne le plus petit commun multiple (PPCM) de deux nombres."""
    return abs(a * b) // greatest_common_divisor(a, b)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def is_perfect_square(number):
    return int(number**0.5) ** 2 == number

def reverse_number(number):
    return int(str(abs(number))[::-1]) * (-1 if number < 0 else 1)

def count_digits(number):
    """Retourne le nombre de chiffres dans un nombre entier."""
    return len(str(abs(number)))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
