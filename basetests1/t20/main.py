def func1(x):
    return x + 1

def func2(x):
    """
    Doubles the input value.
    
    Parameters:
    x (numeric): The value to double
    
    Returns:
    numeric: x multiplied by 2
    """
    return x * 2

def func3(x):
    """
    Calculates the cube of the input value.
    
    Parameters:
    x (numeric): The value to cube
    
    Returns:
    numeric: x raised to the power of 3
    """
    return x ** 3

def func4(x):
    return x / 2

def func5(x):
    """
    Calculates the square root of the input value.
    
    Parameters:
    x (numeric): The value to find the square root of (should be non-negative)
    
    Returns:
    float: The square root of x
    """
    return x ** 0.5

def func6(x):
    return x - 10

def func7(x):
    """
    Calculates the negative of the input value.
    
    Parameters:
    x (numeric): The value to negate
    
    Returns:
    numeric: The negative of x
    """
    return -x

def func8(x):
    return abs(x)

def func9(x):
    return x % 2

def func10(x):
    return x * x * x * x

def func11(x):
    """
    Converts the input to a string and adds an exclamation mark.
    
    Parameters:
    x (any): The value to convert to string
    
    Returns:
    str: String representation of x with an exclamation mark
    """
    return str(x) + "!"

def func12(x):
    return round(x, 2)

def func13(x):
    """
    Calculates the reciprocal of the input value.
    
    Parameters:
    x (numeric): The value to find the reciprocal of (should not be zero)
    
    Returns:
    float: 1 divided by x
    """
    return 1 / x

def func14(x):
    return x + x + x

def func15(x):
    return x ** 2 + 2 * x + 1

# Example usage
if __name__ == "__main__":
    x = 5
    print(f"func1({x}) = {func1(x)}")
    print(f"func2({x}) = {func2(x)}")
    print(f"func3({x}) = {func3(x)}")
    print(f"func4({x}) = {func4(x)}")
    print(f"func5({x}) = {func5(x)}")
    print(f"func6({x}) = {func6(x)}")
    print(f"func7({x}) = {func7(x)}")
    print(f"func8({x}) = {func8(x)}")
    print(f"func9({x}) = {func9(x)}")
    print(f"func10({x}) = {func10(x)}")
    print(f"func11({x}) = {func11(x)}")
    print(f"func12({x}) = {func12(x)}")
    print(f"func13({x}) = {func13(x)}")
    print(f"func14({x}) = {func14(x)}")
    print(f"func15({x}) = {func15(x)}")