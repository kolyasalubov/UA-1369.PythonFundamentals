import re

password = input("Введіть ваш пароль: ")
mandatory = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"

if re.match (mandatory,password):
    print ("Ласкаво просимо")
else:
    print ("Пароль не підійшов, він має містити букви маленькі та велиці літери і знаки $#@ ")