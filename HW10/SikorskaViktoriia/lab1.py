class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, width, height):
   
        sides = [width, height, width, height]
        super().__init__(sides)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(4, 5)
print(f"Rectangle Area: {rectangle.area()}")  
