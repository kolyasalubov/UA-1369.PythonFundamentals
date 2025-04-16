"""Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square
of rectangle."""

class Polygon:
    def __init__(self,sides):
        self.sides = sides
    
    def perimeter(self):
        return sum(self.sides)  

class Rectangle(Polygon):
    def __init__(self,width, height):
        sides = [width, height, width, height]
        super().__init__(sides)
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width   
rec = Rectangle(6,7)
print (f"Rectangle Aren is : {rec.area()}")

