from areas import *

l = """
1. Find area of rectangle
2. Find area of triangle
3. Find area of circle
"""
print(l)
choose = int(input("Choose figure to calculate area: "))
match choose:
    case 1:
        area_rectangle()
    case 2:
        area_triangle()
    case 3:
        area_circle()
    case _:
        print("Sorry, I don't know what you are looking for")
