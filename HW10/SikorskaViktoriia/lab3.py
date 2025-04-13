class Employee:
    total_employees = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1  

    @classmethod
    def total(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


employee1 = Employee("Olga", 5000)
employee2 = Employee("Andriy", 4500)


Employee.total()  


employee1.details()  
employee2.details() 


print("Base Classes:", Employee.__bases__)  
print("Class Namespace:", Employee.__dict__)  
print("Class Name:", Employee.__name__)  
print("Module Name:", Employee.__module__)  
print("Documentation:", Employee.__doc__)  
