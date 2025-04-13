# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(int(self.n))]
#
#     def outputSides(self):
#         for i in range(int(self.n)):
#             print(f"Side {i+1}: {self.sides[i]}")
#
# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self, 2)
#
#     def area(self):
#         a, b = self.sides
#         return f"Area of rectangle: {a * b}"
#
# r1 = Rectangle()
# r1.inputSides()
# r1.outputSides()
# print(r1.area())







# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def welcome(self):
#         super().__init__()
#         return f"Hello {self.age}yrs old {self.name}!"
#
#     def homosapiens(self):
#         return f"{self.name} you are a Homosapiens."
#
#     @staticmethod
#     def arbitrary():
#         return f"Thank u"
#
# human = Human("Mark",31)
# print(human.welcome())
# print(human.homosapiens())
# print(human.arbitrary())




# class Employee:
#     '''
#     Something to see __doc__
#     '''
#     list_of_employees = []
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#         Employee.list_of_employees.append(self)
#
#     @classmethod
#     def total_employee(cls):
#         print(f"Total number of employees: {len(cls.list_of_employees)}")
#
#     @classmethod
#     def total_info(cls):
#         print("\nInfo about the all employees")
#         for employee in cls.list_of_employees:
#             print(f"Name: {employee.name}, Salary: {employee.salary}")
#
#
# h1 = Employee("Max", 20)
# h2 = Employee("Artur", 0)
# h3 = Employee("Bill", 20)
#
# Employee.total_employee()
# Employee.total_info()
#
# print(Employee.__bases__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)




























