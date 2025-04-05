def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return 3.14 * radius**2

def main():
    first_choice = int(input("Choose a shape to calculate the area:\n 1- rectangle\n 2- triangle\n 3- circle\n  "))

    if first_choice == 1:
        length = float(input("Enter value of length: "))
        width = float(input("Enter value of width: "))
        print("Area of rectangle:", area_rectangle(length, width))

    elif first_choice == 2:
        basis = float(input("Enter value of basis: "))
        height = float(input("Enter value of height: "))
        print("Area of triangle:", area_triangle(basis, height))

    elif first_choice == 3:
        radius = float(input("Enter value of radius: "))
        print("Area of circle:", area_circle(radius))

    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()