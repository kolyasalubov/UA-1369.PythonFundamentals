# TASK 1

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    elif i % 3 == 0:
        print(i, "is odd and divisible by 3")
    else:
        print(i, "is not divisible by 2 and 3")

# TASK 2

while True:
    login = input("Enter your login:")
    if login == "First":
        print("Hello, you are logged in")
        break
    else:
        print("ERROR")
