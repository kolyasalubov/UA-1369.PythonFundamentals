#Task1. 
#Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.

class Polygon:
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)  #super().__init__(3) 

    def findArea(self):
        a, b = self.sides
        square = a * b
        print('The area of the rectangle is %0.2f' %square)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print (f"The area of the triangle is {area:.2f}")
        else:
            print ("The triangle does not exist")

t = Rectangle()
print(Rectangle.__mro__)
t.inputSides()
t.dispSides()
t.findArea()


r = Triangle()
print(Triangle.__mro__)
r.inputSides()
r.dispSides()
r.findArea()