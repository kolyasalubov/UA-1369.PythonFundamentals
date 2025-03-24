def fibonacci_to_n(n):
  """Виводить числа Фібоначчі до n.

  Args:
    n: Верхня межа чисел Фібоначчі.
  """
  a, b = 0, 1
  while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# Приклад використання
n = int(input("Введіть число n: "))
fibonacci_to_n(n)