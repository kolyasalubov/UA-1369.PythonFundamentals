# I. Jenny's secret message

# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like 
# to greet him slightly different. She added a special 
# case to her function, but she made a mistake.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {}!".format(name)
    




# II. Find The Distance Between Two Points

# Given two ordered pairs calculate the distance between them. 
# Round to two decimal places. This should be easy to do in 0(1) timing.

    import math

def distance(x1, y1, x2, y2):
  """
  Обчислює відстань між двома точками.

  Args:
    x1: Координата x першої точки.
    y1: Координата y першої точки.
    x2: Координата x другої точки.
    y2: Координата y другої точки.

  Returns:
    Відстань між двома точками, округлена до двох знаків після коми.
  """
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return round(dist, 2)




# III. No yelling!

# Write a function taking in a string like WOW this is REALLY          
# amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. #Using re and string is not allowed.

# Examples:

# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!

def filter_words(st):
    """
    Форматує рядок: перше слово з великої літери, решта слів - з маленької літери.
    

    Args:
      st (str): Вхідний рядок.

    Returns:
      str: Відформатований рядок.
    """
    words = st.split()  # Розбиваємо рядок на слова, автоматично прибираючи зайві пробіли
    if not words:
        return ""

    result = words[0].capitalize()  # Перше слово з великої літери
    for word in words[1:]:
        result += " " + word.lower()  # Решта слів у нижньому регістрі

    return result




# IV. Convert a Number to a String

# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    """
    Перетворює ціле число на рядок.

    Аргументи:
        num: Ціле число для перетворення.

    Повертає:
        Рядок, що представляє число.
    """
    return str(num)



# V. Reversing Words in a String

# You need to write a function that reverses the words in a given string. 
# Words are always separated # by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# Example (Input --> Output)

def reverse(st):
    """
    Реверсує слова в заданому рядку.

    Аргументи:
        st: Рядок для реверсування.

    Повертає:
        Рядок із реверсованими словами.
    """
    words = st.split()  # Розділяє рядок на список слів
    reversed_words = words[::-1]  # Реверсує список слів
    return " ".join(reversed_words)  # Об'єднує реверсовані слова в рядок



# VI. Reverse List Order

# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
  """
  Повертає список з елементами списку l у зворотному порядку.

  Args:
    l: Вхідний список.

  Returns:
    Новий список з елементами у зворотному порядку.
  """
  return l[::-1]



# VII. Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all 
# the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)



def reverse_list(l):
  """
  Повертає список з елементами списку l у зворотному порядку.

  Args:
    l: Вхідний список.

  Returns:
    Новий список з елементами у зворотному порядку.
  """
  return l[::-1]





#  VIII. Will you make it?

# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.


def zero_fuel(distance_to_pump, mpg, fuel_left):
  """
  Визначає, чи можна дістатися до заправки, враховуючи залишок палива, витрату палива та відстань до заправки.

  Args:
    distance_to_pump: Відстань до заправки в милях.
    mpg: Кількість миль, яку автомобіль проїжджає на одному галоні палива.
    fuel_left: Кількість галонів палива, що залишилося.

  Returns:
    True, якщо можна дістатися до заправки, і False, якщо ні.
  """
  return mpg * fuel_left >= distance_to_pump




#IX. Are You Playing Banjo?

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.


def are_you_playing_banjo(name):
  """
  Визначає, чи грає людина на банджо, залежно від першої літери її імені.

  Args:
    name: Ім'я людини.

  Returns:
    Рядок, що повідомляє, чи грає людина на банджо.
  """
  if name.lower().startswith('r'):
    return name + " plays banjo"
  else:
    return name + " does not play banjo"
  


# X. Convert boolean values to strings 'Yes' or 'No’

# Complete the method that takes a boolean value and return a 
# "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
  """
  Перетворює логічне значення на рядок "Yes" або "No".

  Args:
    boolean: Логічне значення (True або False).

  Returns:
    Рядок "Yes", якщо boolean дорівнює True, і рядок "No", якщо boolean дорівнює False.
  """
  if boolean:
    return "Yes"
  else:
    return "No"

 



 #XI. Convert boolean values to strings 'Yes' or 'No’


def count_sheeps(sheep):
  """
  Підраховує кількість нaявних овець у списку.

  Args:
    sheep: Список, де True означає наявність вівці, а False - відсутність.

  Returns:
    Кількість наявних овець.
  """
  if sheep is None:
    return 0
  count = 0
  for s in sheep:
    if s:
      count += 1
  return count



 # XII. Is this my tail?
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

# If the tail is right return true, else return false.

# The arguments will always be non empty strings, and normal letters.



 def correct_tail(body, tail):
    """
    Перевіряє, чи хвіст тварини відповідає її тілу.

    Args:
      body: Рядок, що представляє тіло тварини.
      tail: Рядок, що представляє хвіст тварини.

    Returns:
      True, якщо хвіст відповідає тілу, інакше False.
    """
    if body[-len(tail):] == tail:
        return True
    else:
        return False













