import area_cal


def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter the number of your choice: ")
    if choice == '1':  # Прямокутник
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = area_cal.rectangle_area(a, b)
        print(f"The area of the rectangle is: {area:.2f}")

    elif choice == '2':  # Трикутник
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = area_cal.triangle_area(a, h)
        print(f"The area of the triangle is: {area:.2f}")

    elif choice == '3':  # Коло
        r = float(input("Enter the radius of the circle: "))
        area = area_cal.circle_area(r)
        print(f"The area of the circle is: {area:.2f}")

    else:
        print("Invalid choice, please select a valid option.")


if __name__ == "__main__":
    main()