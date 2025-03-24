while True:
    login = input("Введіть логін: ")
    if login == "First":
        print("Привіт, користувачу!")
        break  # Виходимо з циклу, якщо логін правильний
    else:
        print("Помилка! Неправильний логін.")