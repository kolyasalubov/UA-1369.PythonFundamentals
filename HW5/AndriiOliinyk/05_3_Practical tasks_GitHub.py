def factorial(n):
  """Обчислює факторіал числа n без використання рекурсії."""

  if n < 0:
    return "Факторіал не визначений для від'ємних чисел"
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

# Приклад використання
number = int(input("Введіть число: "))
print(f"{number}! = {factorial(number)}")