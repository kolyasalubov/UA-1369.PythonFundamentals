def days_of_the_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if number < 1 or number > len(days):
        raise ValueError("Number must be between 1 and 7")

    return days[number - 1]

try:
    user = int(input("Enter a number: "))
    result = days_of_the_week(user)
    print(result)
except ValueError as e:
    print(e)