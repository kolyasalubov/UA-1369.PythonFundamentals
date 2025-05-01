class Polygon:
    def __init__(self, number_of_sides):
        self.sides_amount = number_of_sides
        self.sides = [float(input(f"Enter length of side {_ + 1}: "))
                      for _ in range(number_of_sides)]

    def print_sides(self):
        i = 1
        for side in self.sides:
            print(f"Side {i}: {side}")
            i += 1

    def change_side(self, side):
        self.sides[side-1] = float(input(f"Length of side {side} "
                                         f"is {self.sides[side-1]}\n"
                                         f"Enter new length of side {side}: "))

class Rectangle(Polygon):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        return self.sides[0] * self.sides[1]


rectangle_A = Rectangle(2)
print("Rectangle_A sides:",rectangle_A.sides)
print("Area of rectangle:", rectangle_A.area())

rectangle_A.change_side(2)
print("Rectangle_A sides after changing:",rectangle_A.sides)
print("Area of rectangle:", rectangle_A.area())
