"""
1. Create an employee class.  +
2. Each employee has characteristics such as name and salary. + 
3. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.
In addition to creating a class, display information about the base classes from which
the employee class is inherited (__base__), the class namespace (__dict__), the
class name (__name__), the module name in which the class is defined
(__module__), the documentation bar ( __doc__)"""

class Employee():
    amount_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.amount_employee +=1 
    
    @classmethod
    def total(cls):
        print (f"Total of Employee {cls.amount_employee}")
    
    def information(self):
        print (f"His name is {self.name}, and his salary {self.salary}")
emp1 = Employee ("Nazar", 2000)
emp2 = Employee ("Serg", 400)

emp1.information()
emp2.information()

print(Employee.__base__)     # Батьківський клас
print(Employee.__dict__)     # Атрибути цього класу
print(Employee.__name__)     # Назва класу
print(Employee.__module__)   # Модуль, в якому клас оголошено
print(Employee.__doc__)



        
    