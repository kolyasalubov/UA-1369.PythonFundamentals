from func import rectangle_area
from func import triangle_area 
from func import circle_area

def area_calculation():
    while True:
        choice = input("Please choose Rectangle, Triangle, Circle: ").lower()
        if choice not in ["rectangle", "triangle", "circle"]:  
            print ("Invalid choice. Try again:")
        elif choice == "circle":
           radius = float(input("Input the radius of the circle : "))
           print("The area of the circle with radius ", circle_area(radius))
        elif choice == "triangle": 
           base = float(input("Input the base of the Triangle : "))
           height = float(input("InpuTt the height of the Triangle : "))
           print("The area of the Triangle : ", triangle_area(base, height))
        else: 
           choice == "Rectangle"
           width = float(input("Input the width of the Rectangle : "))
           height = float(input("InpuTt the height of the Rectangle : "))
           print("The area of the Rectangle : ",rectangle_area(width, height))
        break
area_calculation()