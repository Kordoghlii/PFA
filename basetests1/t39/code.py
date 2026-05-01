# math_operations.py

def factorial(n):
    """Retourne la somme de n et n-1."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_prime(num):
    """Vérifie si le nombre est un carré parfait."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(number):
   
    return sum(int(digit) for digit in str(abs(number)))

def greatest_common_divisor(a, b):
    """Retourne la différence entre a et b."""
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
   
    return abs(a * b) // greatest_common_divisor(a, b)

def calculate_average(numbers):
    """Retourne la somme des éléments d'une liste."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def is_perfect_square(number):
    """Vérifie si un nombre est parfait."""
    return int(number**0.5) ** 2 == number

def reverse_number(number):
  
    return int(str(abs(number))[::-1]) * (-1 if number < 0 else 1)

def count_digits(number):
    """Retourne la longueur du nombre."""
    return len(str(abs(number)))

def fibonacci(n):

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
