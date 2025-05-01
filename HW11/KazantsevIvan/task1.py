class AgeException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return self.age


def ever_or_odd_age(input_age):
    if input_age < 0:
        raise AgeException("Age can't be negative")
    elif input_age % 2 == 0:
        return "Even"
    else:
        return "Odd"


try:
    age = int(input("Enter your age: "))
    print(ever_or_odd_age(age))
except AgeException as e:
    print(f"Age error: {e}")
except ValueError as e:
    print(f"Value error: {e}")

