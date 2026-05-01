def func1(x, y):
    """
    This function takes two parameters and returns their sum.
    
    Parameters:
    x (numeric): First number to add
    y (numeric): Second number to add
    
    Returns:
    numeric: The sum of x and y
    """
    return x + y

def func2(text):
    return text.upper()

def func3(numbers):
    """
    This function calculates the average of a list of numbers.
    
    Parameters:
    numbers (list): A list of numeric values
    
    Returns:
    float: The average of all numbers in the list, or 0 if the list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    print(func1(5, 3))       # Output: 8
    print(func2("hello"))    # Output: HELLO
    print(func3([1, 2, 3]))  # Output: 2.0