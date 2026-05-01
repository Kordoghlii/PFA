import pytest
from math_operations import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, -5) == 15

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_factorial():
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False

def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(17, 23) == 1

def test_lcm():
    assert lcm(4, 6) == 12
    assert lcm(5, 7) == 35

def test_fibonacci():
    assert fibonacci(6) == 8
    assert fibonacci(0) == 0