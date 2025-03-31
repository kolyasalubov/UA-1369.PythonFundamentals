import math

def calculate_area():
    """Обчислює площу фігури за вибором користувача."""
    figure = input("Яку фігуру обчислити (прямокутник, трикутник, коло)? ")

    if figure == "прямокутник":
        width = float(input("Ширина: "))
        height = float(input("Висота: "))
        print("Площа:", width * height)
    elif figure == "трикутник":
        base = float(input("Основа: "))
        height = float(input("Висота: "))
        print("Площа:", 0.5 * base * height)
    elif figure == "коло":
        radius = float(input("Радіус: "))
        print("Площа:", math.pi * radius**2)
    else:
        print("Неправильний вибір.")

calculate_area()