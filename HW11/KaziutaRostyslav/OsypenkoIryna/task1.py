class NegativeAgeError(Exception):
    pass

def check_odd_even(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    elif age % 2 == 0:
        return "Entered age is even"
    elif age == 0:
        raise ValueError("Age cannot be zero")
    else:
        return "Entered age is odd"

try:
    user_input = int(input("Enter your age: "))
    result = check_odd_even(user_input)
    print (result)
except ValueError:
    print("You entered not a number.")
except NegativeAgeError as e:
    print(e)