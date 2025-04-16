# Завдання 3
#Створіть клас Employee. Кожен працівник має такі характеристики, як ім'я та зарплата. 
# Клас повинен мати лічильник, який обчислює загальну #кількість працівників, а також метод, 
# який друкує загальну кількість працівників, і метод, який відображає інформацію про кожного працівника 
# #зокрема, а саме ім'я та зарплату.
# Крім створення класу, відобразіть інформацію про базові класи, від яких успадковується клас Employee (__base__),
#  про простір імен класу 
#(__dict__), назву класу (__name__), назву модуля, в якому визначено клас (__module__), рядок документації (__doc__).

class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def employee_info(self):
        return f"Ім'я: {self.name}, Зарплата: {self.salary}"

    @classmethod
    def total_employees(cls):
        return f"Загальна кількість працівників: {cls.count}"
    

# Відображення інформації про клас Employee

print(f"Базові класи: {Employee.__base__}")
print(f"Простір імен: {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")
print(f"Рядок документації: {Employee.__doc__}")
    


# Приклад використання

employee1 = Employee("Петро", 5000)
employee2 = Employee("Марія", 6000)
print(employee1.employee_info())
print(employee2.employee_info())
print(Employee.total_employees())
