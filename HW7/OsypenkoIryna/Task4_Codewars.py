# Task1
# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. '
# 'She added a special case to her function, but she made a mistake.
# Can you help her?


# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return f"Hello, {name}!"


#################################################################################################


# Task2
# Given two ordered pairs calculate the distance between them. Round to two decimal places. 
# This should be easy to do in 0(1) timing.

# def distance(x1, y1, x2, y2):
#     count = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     return round(count, 2)


################################################################################################


# Task3
# Write a function taking in a string like WOW this is REALLY          amazing 
# and returning Wow this is really amazing. String should be capitalized and properly spaced. 
# Using re and string is not allowed.

# def filter_words(st):
#     st_1 = st.lower()
#     st_2 = st_1.split()
#     st_3 = " ".join(st_2)
#     return st_3.capitalize()


###################################################################################################


#Task4
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

# def number_to_string(num):
#     #return str(num)
#     #return "{}".format(num)
#     return f"{num}" 


##################################################################################################


#Task5
# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.


# def reverse(st):
#     list_st = st.split()
#     list_st.reverse()
#     st = " ".join(list_st)
#     return st


##################################################################################################


#Task6
# In this kata you will create a function that takes in a list and returns a list 
# with the reverse order.

# def reverse_list(l):
#     new_l = l[::-1]
#     return new_l


#################################################################################################


#Task7
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If the number is a multiple of both 3 and 5, only count it once.

# def solution(number):
#     if number < 0:
#         return 0
#     else:
#         return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)


################################################################################################


#Task8
# You were camping with your friends far away from home, but when it's time to go back, 
# you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, 
# your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left


##################################################################################################


#Task9
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

# import re

# def are_you_playing_banjo(name):
#     result_1 = re.findall("^r", name)
#     result_2 = re.findall("^R", name)
#     if result_1 or result_2:
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"


####################################################################################################


#Task10
# Complete the method that takes a boolean value and return a "Yes" string for true, 
# or a "No" string for false.

# def bool_to_word(boolean):
#     if boolean:
#         return 'Yes'
#     else:
#         return 'No'


#####################################################################################################


#Task11
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).
# Hint: Don't forget to check for bad values like null/undefined

# def count_sheeps(sheep):
#     return sheep.count(True)


#####################################################################################################


#Task12
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. 
# To help her, you must correct the broken function to make sure that the second argument (tail), 
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False