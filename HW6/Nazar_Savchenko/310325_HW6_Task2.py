name = input ("Hi, please enter your login :")
login = "First"
while login != name :
    print ("This login is not correct , please try again")
    name = input ("Hi, please enter your login :")
else:
    name == login
    print (f"Welcome", name)