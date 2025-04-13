import module3task as mod

if __name__ == '__main__':
    while True:
        figure = input("What area you want to calculate?\n1) Triangle"
                       "\n2) Rectangle\n3) Circle\n")
        if figure == "1" or figure == "2":
            while True:
                a, b = map(float, input("Enter 2 sides: ").split())
                if a > 0 and b > 0:
                    if figure == "1":
                        print(mod.triangle_area(a, b))
                    elif figure == "2":
                        print(mod.rectangle_area(a, b))
                    break
                else:
                    print("Sides must be greater than zero."
                          " Please enter again.")
            break
        elif figure == "3":
            while True:
                a = float(input("Enter radius: "))
                if a > 0:
                    print(mod.circle_area(a))
                    break
                else:
                    print("Radius must be greater than zero."
                          " Please enter again.")
            break
        else:
            print("Invalid input.")
