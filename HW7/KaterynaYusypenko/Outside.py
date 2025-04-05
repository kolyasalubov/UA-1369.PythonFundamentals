# Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {}!".format(name)
# print(greet("Johnny"))

####################################################################

# Find The Distance Between Two Points
# import math
#
# def calculate_distance(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2
#
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
#     return round(distance, 2)
#
#
# point1 = (1, 5)
# point2 = (4, 6)
#
# print("Distance:", calculate_distance(point1, point2))

###################################################################

# No yelling
# def filter_words(st):
#     words = st.split()
#     normal = ' '.join(words)
#     normal = normal.lower()
#     if not normal:
#         return ''
#     return normal[0].upper() + normal[1:]
#
# print(filter_words('HELLO CAN YOU HEAR ME'))

####################################################################

# Convert a Number to a String
# def number_to_string(num):
#     return str(num)
# resolt = number_to_string(3)
# print(resolt)
# print(type(resolt))

####################################################################

# Reversing Words in a String
# def reverse_a_string(words):
#     sentense = words.split()
#     reverse_a_words = sentense[::-1]
#     return ' '.join(reverse_a_words)
# resolt = reverse_a_string('Hello, Python')
# print(resolt)

####################################################################

# Reverse List Order
# list1 = [1,2,3]
# def reverse_a_list(list1):
#     return (list1[::-1])
# print(reverse_a_list(list1))

####################################################################

# Multiples of 3 or 5
# def solution(number):
#     if number < 0:
#         return 0
#
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total
#
# print(solution(15))

####################################################################

# Will you make it?
# def reach_pump(distance, miles, galon):
#     return miles * galon >= distance
#
# print(reach_pump(50, 25, 2))

###################################################################

# Are You Playing Banjo?
# def playing(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
# print(playing("Loly"))

###################################################################

# Convert boolean values to strings 'Yes' or 'No’
# def bool_to_word(value):
#     return "Yes" if value else "No"
# print(bool_to_word(True))

###################################################################

#Counting sheep
# def count_sheeps(sheep):
#     return sum(1 for s in sheep if s is True)
# sheep_list = [
#     True,  True,  True,  False,
#     True,  True,  True,  True,
#     True,  False, True,  False,
#     True,  False, False, True,
#     True,  True,  True,  True,
#     False, False, True,  True
# ]
#
# print(count_sheeps(sheep_list))

####################################################################

# Is this my tail?
# def correct_tail(body, tail):
#     sub = body[-len(tail):]
#     if sub == tail:
#         return True
#     else:
#         return False