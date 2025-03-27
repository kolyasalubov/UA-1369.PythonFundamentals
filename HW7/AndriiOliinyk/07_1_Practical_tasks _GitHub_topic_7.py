def find_largest(num1, num2):
  """
  Повертає найбільше число з двох заданих чисел.

  Args:
    num1: Перше число.
    num2: Друге число.

  Returns:
    Найбільше число з num1 та num2.
  """
  if num1 > num2:
    return num1
  else:
    return num2

# Приклад використання:
largest_number = find_largest(10, 5)
print(f"Найбільше число: {largest_number}")  # Виведе: Найбільше число: 10

largest_number2 = find_largest(-10, 5)
print(f"Найбільше число: {largest_number2}") # виведе: Найбільше число: 5