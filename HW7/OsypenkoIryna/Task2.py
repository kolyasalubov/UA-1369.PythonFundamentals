import math

def calculate_the_area ():
    
    num = int(input("The area of which figure you want to find? A rectangle - enter 1, a triangle - enter 2, a circle  - enter 3. Enter the number: "))
    
    if num == 1:
        a = float(input("Enter the width: "))
        b = float(input("Enter the length: "))
        print("The area of the rectangle is:", a * b)
    elif num == 2:
        h = float(input("Enter the height: "))
        a = float(input("Enter the base: "))
        print("The area of the triangle is:", 0.5 * h * a)
    elif num == 3:
        r = float(input("Enter the radius: "))
        print("The area of the circle is:", math.pi * r**2)
    else:
        print("Error message. You enter the number bigger than 3")
calculate_the_area ()