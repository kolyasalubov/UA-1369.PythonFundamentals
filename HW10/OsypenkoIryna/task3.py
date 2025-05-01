# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which
# the employee class is inherited (__base__), the class namespace (__dict__), the
# class name (__name__), the module name in which the class is defined
# (__module__), the documentation bar ( __doc__)


class Employee:

    employee_count = 0

    def __init__(self, name: str, salary: float = 0.0):
        self.name = name
        self.salary = salary
        Employee.employee_count +=1
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total(cls):
        print(f"Total employees: {cls.employee_count}")


empl1 = Employee("Harry", 200)
empl2 = Employee("Potter", 600)

empl1.display_info()
empl2.display_info()

Employee.total()

print("\n--- Class Info ---")
print("Base class:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)