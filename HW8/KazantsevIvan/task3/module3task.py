from math import pi, pow

def rectangle_area(a,b):
    """
    Finds the area of rectangle.

    Parameters:
        a (float/int): One side of the rectangle.
        b (float/int): Second side of the rectangle.

    Returns:
        float/int: The area of rectangle.
    """
    return a*b

def triangle_area(a,b):
    """
    Finds the area of triangle.

    Parameters:
        a (float/int): One side of the triangle.
        b (float/int): Second side of the triangle.

    Returns:
        float/int: The area of triangle.
    """
    return a*b*0.5

def circle_area(radius):
    """
    Finds the area of circle.

    Parameters:
        radius (float/int): Radius of the circle.

    Returns:
        float: The area of circle.
    """
    return pi*pow(radius, 2)
