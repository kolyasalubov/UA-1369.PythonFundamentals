def check_age(age_str):
    """
    Перевіряє, чи є введений вік парним або непарним.
    Генерує виняток ValueError, якщо введено від'ємне число.

    Args:
        age_str: Рядок, що представляє вік користувача.

    Returns:
        Рядок з повідомленням про парність або непарність віку.

    Raises:
        ValueError: Якщо введено від'ємне число.
    """
    try:
        age = int(age_str)
        if age < 0:
            raise ValueError("Вік не може бути від'ємним.")
        elif age % 2 == 0:
            return f"Введений вік ({age}) є парним."
        else:
            return f"Введений вік ({age}) є непарним."
    except ValueError as e:
        raise e
    except TypeError:
        raise ValueError("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    while True:
        try:
            age_input = input("Будь ласка, введіть ваш вік: ")
            result = check_age(age_input)
            print(result)
            break  # Вийти з циклу після успішного введення та обробки
        except ValueError as error:
            print(f"Помилка: {error}")