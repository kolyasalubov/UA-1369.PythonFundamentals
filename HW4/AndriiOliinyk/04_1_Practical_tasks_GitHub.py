def celsius_to_fahrenheit(celsius):
    """
    Перетворює температуру з градусів Цельсія в градуси Фаренгейта.

    Аргументи:
        celsius (float): Температура в градусах Цельсія.

    Повертає:
        float: Температура в градусах Фаренгейта.
        Повертає рядок з помилкою, якщо температура нижче абсолютного нуля.
    """
    if celsius < -273.15:
        return "Помилка: Температура нижче абсолютного нуля (-273.15 °C)"
    else:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

# Отримуємо введення користувача
celsius_temperature = float(input("Введіть температуру в градусах Цельсія: "))

# Перетворюємо температуру
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

# Виводимо результат
print(f"{celsius_temperature} °C еквівалентно {fahrenheit_temperature} °F")