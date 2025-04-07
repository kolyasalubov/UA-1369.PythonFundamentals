import re

while True:
    password = input("Password must be 6 characters minimum, "
                     "maximum 16 characters,\ncontain at least 1 small letter,"
                     " 1 capital letter, 1 number,\nand one special symbol "
                     "like $#@.\n\nEnter password: ")

    if (6 <= len(password) <= 16 and re.search(pattern, password)
        for pattern in [r"[a-z]", r"[A-Z]", r"[0-9]", r"[$#@]"]):

        print(f"Password << {password} >> is valid")
        break

    else:
        print(f"Password << {password} >> is INVALID.\nTry again\n")
