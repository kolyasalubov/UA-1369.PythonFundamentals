import re

def password():
    user_password = input("Enter your password: ")

    if 6 < len(user_password) < 16:
        if re.search(r"[a-z]", user_password) and \
                re.search(r"[A-Z]", user_password) and \
                re.search(r"\d", user_password) and \
                re.search(r"[$#@]", user_password):
            print("Your password is valid")
        else:
            print("Your password is invalid")
    else:
        print("Your password is invalid")

password()