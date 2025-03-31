import math

def area_rectangle():
    a = float(input("Enter the side a: "))
    b = float(input("Enter the side b: "))
    if a > 0 and b > 0:
        print(f"Area of triangle: {a * b}")
    else:
        print("Sides cant be negative")

def area_triangle():
    h = float(input("Enter the height: "))
    a = float(input("Enter the side a: "))
    if a > 0 and h > 0:
        print(f"Area of triangle: {0.5 * h * a}")
    else:

        print("Sides cant be negative")

def area_circle():
    radius = float(input("Enter the radius: "))
    if radius > 0:
        print(f"Area of circle: {math.pi * pow(radius, 2)}")
    else:
        print("Radius cant be negative")

