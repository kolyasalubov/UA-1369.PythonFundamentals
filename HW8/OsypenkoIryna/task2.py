import re

password = input("Enter your password: ")

min_length = 6
max_length = 16

def validation(password):
    if not re.findall(r"[a-z]", password):
        print("Password must contain at least one lowercase letter from a to Z.")
        return
    elif not re.search(r"[A-Z]", password):
        print("Password must contain at least one highercase letter from A to Z.")
        return
    elif not re.findall(r"\d", password):
        print("Password must contain at least one number between 0 to 9.")
        return
    elif len(password) < min_length or len(password) > max_length:
        print("Password must be between 6 and 16 characters.")
        return
    elif not re.search(r"[$#@]", password):
        print("The password must contain at least one special character: $, #, or @.")
        return
    else:
        print("Password is valid!")

validation(password)