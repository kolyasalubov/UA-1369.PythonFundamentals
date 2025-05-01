def day_of_week (number):
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    if number in days:
        return f"The day is: {days[number]}"
    else:
        return "There is no such day of the week"

try:
    user_input = int(input("Enter a number from 1 to 7: "))
    result = day_of_week (user_input)
    print (result)
except ValueError:
    print("Number must be between 1 and 7")