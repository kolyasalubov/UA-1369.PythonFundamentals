import area_calc

def main():
    
    num = int(input("The area of which figure you want to find? A rectangle - enter 1, a triangle - enter 2, a circle  - enter 3. Enter the number: "))
    
    if num == 1:
        a = float(input("Enter the width: "))
        b = float(input("Enter the length: "))
        print(area_calc.rectangle_area(a,b))
    elif num == 2:
        h = float(input("Enter the height: "))
        a = float(input("Enter the base: "))
        print(area_calc.triangle_area(a,h))
    elif num == 3:
        r = float(input("Enter the radius: "))
        print(round(area_calc.circle_area(r), 2))
    else:
        print("Error message. You enter the number bigger than 3")

main()