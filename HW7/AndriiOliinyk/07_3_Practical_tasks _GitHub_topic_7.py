def count_characters(s):
  """Обчислює кількість символів у рядку.

  Args:
    s: Вхідний рядок.

  Returns:
    Словник, де ключі - це символи, а значення - їх кількість.
  """

  char_counts = {}
  for char in s:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts

# Приклад використання
input_string = "hello"
output = count_characters(input_string)
print(output)