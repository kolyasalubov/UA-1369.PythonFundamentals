def your_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    elif age == 0:
        raise ValueError("Age can't be zero")
    elif age > 110:
        raise ValueError("Nice try, but age can't be greater than 110")
    elif age % 2 == 0:
        return "Age is even"
    else:
        return "Age is odd"

try:
    user_age = int(input("Enter your age: "))
    result = your_age(user_age)
    print(result)
except ValueError as e:
    print(e)
