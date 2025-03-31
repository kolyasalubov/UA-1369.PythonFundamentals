# TASK 1
# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

print("TASK 1")
def largest_number(a, b):
    """
    Finds the largest number between a and b.

    Parameters:
        a (float/int): The first number.
        b (float/int): The second number.

    Returns:
        float/int: The largest number.
    """
    if a > b:
        return a
    else:
        return b

print("The largest number of 5 and 7: ", largest_number(5,7))
print("The largest number of 12 and 11: ",largest_number(12,11))

# TASK 2
# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main
# program depending on the user's choice)

PI = 3.14

def rectangle_area(a,b):
    """
    Finds the area of rectangle.

    Parameters:
        a (float/int): One side of the rectangle.
        b (float/int): Second side of the rectangle.

    Returns:
        float/int: The area of rectangle.
    """
    return a*b

def triangle_area(a,b):
    """
    Finds the area of triangle.

    Parameters:
        a (float/int): One side of the triangle.
        b (float/int): Second side of the triangle.

    Returns:
        float/int: The area of triangle.
    """
    return a*b/2

def circle_area(radius):
    """
    Finds the area of circle.

    Parameters:
        radius (float/int): Radius of the circle.

    Returns:
        float: The area of circle.
    """
    return PI*radius**2

def main():
    print("\nTASK 2")
    while True:
        figure = input("What area you want to calculate?\n1) Triangle"
                       "\n2) Rectangle\n3) Circle\n")
        if figure == "1" or figure == "2":
            while True:
                a, b = map(float, input("Enter 2 sides: ").split())
                if a > 0 and b > 0:
                    if figure == "1":
                        print(triangle_area(a, b))
                    elif figure == "2":
                        print(rectangle_area(a, b))
                    break
                else:
                    print("Sides must be greater than zero."
                          " Please enter again.")
            return False
        elif figure == "3":
            while True:
                a = float(input("Enter radius: "))
                if a > 0:
                    print(circle_area(a))
                    break
                else:
                    print("Radius must be greater than zero."
                          " Please enter again.")
            return False
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()

# TASK 3
# Write a function that calculates the number of characters included
# in given string

def num_of_characters(a):
    """
    Finds the number of characters in a string.

    Parameters:
        a (string): string to be counted.

    Returns:
        dict: The number of characters in a number.
    """
    c = {key: a.count(key) for key in a}
    return c


sentence = input("\nTASK 3\nEnter string: ")

print(num_of_characters(sentence))
