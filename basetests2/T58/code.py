import math

def circle_area(radius):
    """Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def rectangle_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def rectangle_perimeter(length, width):
    # Calculate perimeter of rectangle
    return 2 * (length + width)

def triangle_area(base, height):
    return 0.5 * base * height

def is_right_triangle(a, b, c):
    """Check if a triangle is right-angled.

    Args:
        a (float): Length of first side.
        b (float): Length of second side.
        c (float): Length of third side.

    Returns:
        bool: True if the triangle is right-angled, False otherwise.
    """
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10

def distance_2d(x1, y1, x2, y2):
    # Calculate Euclidean distance between two points
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def slope(x1, y1, x2, y2):
    """Calculate the slope of a line between two points.

    Args:
        x1 (float): X-coordinate of first point.
        y1 (float): Y-coordinate of first point.
        x2 (float): X-coordinate of second point.
        y2 (float): Y-coordinate of second point.

    Returns:
        float or None: The slope, or None if vertical.
    """
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

def is_collinear(x1, y1, x2, y2, x3, y3):
    # Check if three points are collinear using area of triangle
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) < 1e-10

def regular_polygon_area(sides, side_length):
    return (sides * side_length**2) / (4 * math.tan(math.pi / sides))