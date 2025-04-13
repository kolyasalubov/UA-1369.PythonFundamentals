import math

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

__all__= ["rectangle_area", "triangle_area", "circle_area"]