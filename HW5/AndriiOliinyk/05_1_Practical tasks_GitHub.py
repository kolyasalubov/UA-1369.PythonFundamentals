# Запит на введення користувачем довільної кількісті цілих чисел
user_input = input("Введіть довільну кількість цілих чисел, розділених пробілами: ")

# Розбиваємо введення на список рядків
input_list = user_input.split()

# Перетворюємо рядки на цілі числа і створюємо список
my_list = [int(num) for num in input_list]

# Перетворюємо кожне ціле число на число з плаваючою комою
for i in range(len(my_list)):
  my_list[i] = float(my_list[i])

# Виводимо змінений список
print(my_list)