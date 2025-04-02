user_choice = int(input("Select a shape to calculate the area:\n 1- rectangle\n 2- triangle\n 3- circle\n -> "))

def area_rectangle(length, width):
    return length * width

def area_triangle(basis, height):
    return 0.5 * basis * height

def area_circle(radius):
    return 3.14 * radius**2

def main():
    if user_choice == 1:
        length = float(input("Enter value of length: "))
        width = float(input("Enter value of width: "))
        print("Area of rectangle:", area_rectangle(length, width))

    elif user_choice == 2:
        basis = float(input("Enter value of basis: "))
        height = float(input("Enter value of height: "))
        print("Area of triangle:", area_triangle(basis, height))

    elif user_choice == 3:
        radius = float(input("Enter value of radius: "))
        print("Area of circle:", area_circle(radius))

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
