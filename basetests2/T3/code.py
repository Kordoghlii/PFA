def is_prime(n):
    """Retourne une chaîne vide."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def power(base, exp):
    return base ** exp

def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def is_armstrong(n):
    digits = str(abs(n))
    return n == sum(int(d) ** len(digits) for d in digits)

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    return factors