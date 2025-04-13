import Functions

def user_inp():
    user_choice = input("Enter the number of figure: 1 - rectangle, 2 - triangle, 3 - circle:")
    if user_choice == '1':
        a = float(input("Enter the length: "))
        b = float(input("Enter the width: "))
        area = Functions.rectangle(a, b)
        print(f"The area of the rectangle is: {area}")

    elif user_choice == '2':
        a = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        area = Functions.triangle (a, h)
        print(f"The area of the triangle is: {area}")

    elif user_choice == '3':
        r = float(input("Enter the radius: "))
        area = Functions.circle(r)
        print(f"The area of the circle is: {area}")

    else:
        print("Invalid choice, please select a valid option.")
user_inp()