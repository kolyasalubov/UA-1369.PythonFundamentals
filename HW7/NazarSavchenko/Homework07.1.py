import math

def rectangle_area(width, height):
    return width * height

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

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



'''def figures ():
    while True:
        choice = input("Please choose Rectangle, Triangle or Circle: ")
        if choice not in  ["Cectangle", "Triangle", "Circle"]:  
            print ("Invalid choice. Try again:")
        elif choice == "circle":
           radius = float(input("Input the radius of the circle : "))
           area = math.pi * radius **2
           print("The area of the circle with radius " + str(radius) + " is: " + str(area))
        elif choice == "triangle":
            base = float(input("Input the base of the triangle : "))
            height = float(input("Input the height of the triangle : "))
            print (("The area of the triangle", 0.5*base*height))
        elif choice == "rectangle":
            width = float(input("Input the width of the rectangle : "))
            height = float(input("Input the height of the rectangle : "))
            print ("The area of the rectangle", width*height)
        break
user_choice = figures()'''