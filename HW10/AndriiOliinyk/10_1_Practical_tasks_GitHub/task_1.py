# Завдання 1
# Створіть клас Polygon та клас Rectangle, який успадковує клас 
# Polygon і знаходить площу прямокутника.

class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Приклад використання

rectangle = Rectangle(5, 10)
print(f"Площа прямокутника: {rectangle.area()}")
