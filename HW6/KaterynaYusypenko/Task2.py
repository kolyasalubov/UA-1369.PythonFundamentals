#I want to do more useful code for user
while True:
    login = input("Enter your login:")
    if login != "First":
        print("Error")
        tip = input("Need a tip? ")
        if tip == "Yes":
            print("Fi...")
        continue
    else:
        print("Hello, user!")
        break

