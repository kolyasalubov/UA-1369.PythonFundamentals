#Task1: Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

###############################################################################################

#Task3:Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.

# def distance(x1, y1, x2, y2):
#     count = ((x1-x2)**2+(y1-y2)**2)**0.5
#     return round(count, 2)

###############################################################################################

#Task2:Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.

# def filter_words(st):
#     words = st.split() 
#     formatted = " ".join(words) 
#     return formatted.capitalize()  


###############################################################################################

#Task4: We need a function that can transform a number (integer) into a string.

# def number_to_string(num):
#     transform = str(num)
#     return transform
    

###############################################################################################

#Task3:  You need to write a function that reverses the words in a given string. Words are always separated by a single space.

# def reverse(st):
#     words = st.split()  
#     reversed_words = words[::-1]  
#     return " ".join(reversed_words) 
#     return st
    
    
###############################################################################################

#Task6: In this kata you will create a function that takes in a list and returns a list with the reverse order.

# def reverse_list(l):
#     transform = l[::-1]
#     return transform


###############################################################################################

#Task7: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# def solution(n):
#     if n < 0:
#         return 0  
    
#     total = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:  
#             total += i
#     return total


###############################################################################################

#Task8: You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     max_distance = fuel_left * mpg  
#     return max_distance >= distance_to_pump  


###############################################################################################

# #Task9: ate a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!


# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r': 
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"


###############################################################################################

# #Task10: Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"


###############################################################################################

# #Task11: Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
 
# def count_sheeps(sheep):
#     return sheep.count(True)


###############################################################################################

# #Task12: Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

# If the tail is right return true, else return false.

# The arguments will always be non empty strings, and normal letters.

# def correct_tail(body, tail):
   
#     if body[-1] == tail:
#         return True
#     else:
#         return False