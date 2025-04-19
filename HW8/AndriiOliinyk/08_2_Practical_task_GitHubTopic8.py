import re

def validate_password(password):
    """
    Перевіряє, чи відповідає пароль заданим критеріям.

    Args:
        password (str): Пароль для перевірки.

    Returns:
        bool: True, якщо пароль дійсний, False - якщо ні.
    """

    if not 6 <= len(password) <= 16:
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[$#@]", password):
        return False

    return True

# Приклад використання
password = input("Введіть пароль: ")

if validate_password(password):
    print("Пароль дійсний.")
else:
    print("Пароль недійсний.")