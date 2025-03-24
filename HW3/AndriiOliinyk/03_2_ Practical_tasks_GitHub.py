def analyze_number(number):
    """Аналізує чотиризначне число та виводить результати."""

    # Перевірка, чи число чотиризначне
    if not (1000 <= number <= 9999):
        print("Будь ласка, введіть чотиризначне число.")
        return

    # Перетворення числа на рядок для зручності роботи з цифрами
    number_str = str(number)

    # Обчислення добутку цифр
    product = 1
    for digit in number_str:
        product *= int(digit)

    # Створення числа у зворотному порядку
    reversed_number = int(number_str[::-1])

    # Сортування цифр у порядку зростання
    sorted_digits = sorted(number_str)
    sorted_number = int("".join(sorted_digits))

    # Виведення результатів
    print(f"Добуток цифр: {product}")
    print(f"Число у зворотному порядку: {reversed_number}")
    print(f"Відсортовані цифри: {sorted_number}")


# Запит на введення числа
try:
    number = int(input("Введіть чотиризначне натуральне число: "))
    analyze_number(number)
except ValueError:
    print("Будь ласка, введіть ціле число.")