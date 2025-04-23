def age_check ():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError ("Age cannot be negative.")
    elif age % 2 == 0 :
        print ("Your age is even.")
    elif age % 2 == 1:
        print ("Your age is odd.")
try:
    age_check()
except ValueError as e:
    print ("Issue :", e)
