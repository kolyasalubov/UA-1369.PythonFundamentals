# def process_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     elif age == 0:
#         raise ValueError("Age cannot be zero")
#     elif age % 2 == 0:
#         return "Your age is even"
#     else:
#         return "Your age is odd"
#
# try:
#     user_age = int(input("Enter your age: "))
#     result = process_age(user_age)
#     print(result)
# except ValueError as e:
#     print(e)










# def days_of_week(number):
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     if number < 1 or number > len(days):
#         raise ValueError("Number must be between 1 and 7")
#
#     return days[number - 1]
#
# try:
#     user = int(input("Enter a number: "))
#     result = days_of_week(user)
#     print(result)
# except ValueError as e:
#     print(e)
