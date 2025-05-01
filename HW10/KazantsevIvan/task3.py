class Employee:
    """
    Represents an employee

    Attributes:
        name (str): The name of the employee
        salary (int): The salary of the employee
        counter (int): Amount of the employees

    Methods:
        getName(self): Returns the name of the employee
        getSalary(self): Returns the salary of the employee
        getCounter(self): Returns the number of employees
        getInfo(self): Returns the information about the employee
    """
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    @classmethod
    def get_counter(cls):
        return cls.counter

    def get_info(self):
        return f"Name:{self.name}, salary: {self.salary}."

    def __del__(self):
        Employee.counter -= 1



print("Employees at start:",Employee.get_counter())

Joe = Employee("Joe", 20000)
print("Employees after adding Joe:",Employee.get_counter())
Sylvia = Employee("Sylvia", 90000)
print("Employees after adding Sylvia:",Employee.get_counter())
Shawn = Employee("Shawn", 123)
print("Employees after adding Shawn:",Employee.get_counter())
del Sylvia
print("Employees after deleting Sylvia:",Employee.get_counter())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)


