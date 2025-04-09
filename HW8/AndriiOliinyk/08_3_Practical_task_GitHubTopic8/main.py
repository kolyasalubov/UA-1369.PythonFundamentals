import areas

def main():
    """Головна функція програми."""
    while True:
        print("\nОберіть фігуру для обчислення площі:")
        print("1. Прямокутник")
        print("2. Трикутник")
        print("3. Коло")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            a = float(input("Введіть довжину сторони a: "))
            b = float(input("Введіть довжину сторони b: "))
            area = areas.rectangle_area(a, b)
            print(f"Площа прямокутника: {area}")
        elif choice == "2":
            h = float(input("Введіть висоту трикутника: "))
            a = float(input("Введіть довжину основи трикутника: "))
            area = areas.triangle_area(h, a)
            print(f"Площа трикутника: {area}")
        elif choice == "3":
            r = float(input("Введіть радіус кола: "))
            area = areas.circle_area(r)
            print(f"Площа кола: {area}")
        elif choice == "4":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()