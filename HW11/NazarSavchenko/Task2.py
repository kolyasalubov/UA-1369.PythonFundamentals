# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering nonnumerical data."


week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",5:"Friday",6:"Saturday", 7:"Sunday"}
try:
    choice = int(input("Choice your day, from 1 to 7, please: "))
    # if 1 <= choice <= 7:  # завбрав базову перевірку , бо не працювали except.
    print("Day of the week:", week[choice])
    #else:
    #    print ("Please enter number from 1 to 7, best regards ") # Блокує роботу except
except KeyError as e :
    print("Key error please enter key from 1 to 7 ")
except ValueError as e :
    print("ValueError please enter numbers from 1 to 7 ")

