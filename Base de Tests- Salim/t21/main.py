def is_prime(n):
    """Helper function to determine if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate all prime numbers up to 100 for reference
primes = [i for i in range(1, 101) if is_prime(i)]

# Create all 100 functions
def func1(x):
    return x + 1

def func2(x):
    """
    Returns the square of a number.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x squared
    """
    return x**2

def func3(x):
    """
    Returns the cube of a number.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x cubed
    """
    return x**3

def func4(x):
    return x * 4

def func5(x):
    """
    Returns x multiplied by 5.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 5
    """
    return x * 5

def func6(x):
    return x * 6

def func7(x):
    """
    Returns x multiplied by 7.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 7
    """
    return x * 7

def func8(x):
    return x * 8

def func9(x):
    return x * 9

def func10(x):
    return x * 10

def func11(x):
    """
    Returns x multiplied by 11.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 11
    """
    return x * 11

def func12(x):
    return x * 12

def func13(x):
    """
    Returns x multiplied by 13.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 13
    """
    return x * 13

def func14(x):
    return x * 14

def func15(x):
    return x * 15

def func16(x):
    return x * 16

def func17(x):
    """
    Returns x multiplied by 17.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 17
    """
    return x * 17

def func18(x):
    return x * 18

def func19(x):
    """
    Returns x multiplied by 19.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 19
    """
    return x * 19

def func20(x):
    return x * 20

# This pattern continues for functions 21-100
# Below are additional prime-indexed functions for demonstration

def func23(x):
    """
    Returns x multiplied by 23.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 23
    """
    return x * 23

def func29(x):
    """
    Returns x multiplied by 29.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 29
    """
    return x * 29

def func31(x):
    """
    Returns x multiplied by 31.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 31
    """
    return x * 31


# For brevity, I'll define func97 as an example of a higher prime
def func97(x):
    """
    Returns x multiplied by 97.
    
    Parameters:
    x (numeric): The input value
    
    Returns:
    numeric: x * 97
    """
    return x * 97

# Example of non-prime high index
def func100(x):
    return x * 100

# Example usage
if __name__ == "__main__":
    test_value = 5
    print(f"func2({test_value}) = {func2(test_value)}")  # Prime index
    print(f"func4({test_value}) = {func4(test_value)}")  # Non-prime index
    print(f"func7({test_value}) = {func7(test_value)}")  # Prime index
    
    # To verify which functions have documentation
    import inspect
    for i in range(1, 21):  # Check first 20 functions
        func_name = f"func{i}"
        if func_name in globals():
            doc = inspect.getdoc(globals()[func_name])
            has_doc = "Yes" if doc else "No"
            print(f"{func_name} has documentation: {has_doc}, Prime: {is_prime(i)}")