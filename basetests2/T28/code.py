import math

def sphere_volume(radius):
    """Calculate the square of a number.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The squared value.
    """
    # Calculate volume of a sphere
    return (4/3) * math.pi * radius ** 3

def sphere_surface_area(radius):
    """Check if a string is a palindrome.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    return 4 * math.pi * radius ** 2

def cylinder_volume(radius, height):
    """Reverse a list.

    Args:
        radius (float): The radius of the cylinder base.
        height (float): The height of the cylinder.

    Returns:
        list: Reversed list.
    """
    # Calculate volume of a cylinder
    return math.pi * radius ** 2 * height

def cone_volume(radius, height):
    """Count vowels in a string.

    Args:
        radius (float): The radius of the cone base.
        height (float): The height of the cone.

    Returns:
        int: Number of vowels.
    """
    return (1/3) * math.pi * radius ** 2 * height

def rectangular_prism_volume(length, width, height):
    """Find maximum in a list.

    Args:
        length (float): Length of the prism.
        width (float): Width of the prism.
        height (float): Height of the prism.

    Returns:
        float: Maximum value.
    """
    # Calculate volume of a rectangular prism
    return length * width * height

def triangular_prism_volume(base_area, height):
    """Convert string to uppercase.

    Args:
        base_area (float): Area of the triangular base.
        height (float): Height of the prism.

    Returns:
        str: Uppercase string.
    """
    return base_area * height

def pyramid_volume(base_area, height):
    """Calculate factorial of a number.

    Args:
        base_area (float): Area of the pyramid base.
        height (float): Height of the pyramid.

    Returns:
        int: Factorial result.
    """
    # Calculate volume of a pyramid
    return (1/3) * base_area * height

def cube_volume(side):
    """Split a string into words.

    Args:
        side (float): Length of the cube's side.

    Returns:
        list: List of words.
    """
    return side ** 3

def ellipsoid_volume(a, b, c):
    """Check if a number is prime.

    Args:
        a (float): First radius of the ellipsoid.
        b (float): Second radius of the ellipsoid.
        c (float): Third radius of the ellipsoid.

    Returns:
        bool: True if prime, False otherwise.
    """
    # Calculate volume of an ellipsoid
    return (4/3) * math.pi * a * b * c

def torus_volume(inner_radius, outer_radius):
    """Calculate the sum of a list.

    Args:
        inner_radius (float): Inner radius of the torus.
        outer_radius (float): Outer radius of the torus.

    Returns:
        float: Sum of the list.
    """
    return 2 * math.pi ** 2 * inner_radius * (outer_radius - inner_radius) ** 2