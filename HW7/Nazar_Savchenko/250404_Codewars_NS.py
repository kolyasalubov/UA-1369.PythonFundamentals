import math
# Task 1 Jenny's secret message
"""def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    
    return "Hello, {name}!".format(name=name)
print(greet("Nazar"))"""

# Task 2  Find The Distance Between Two Points

"""def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
print(distance(1, 1, 0, 0))""" 

# Task 3 No yelling!

'''st = "now THIS is REALLY interesting"

def filter_words(st):
    sentence = st.split()
    st = ' '.join(sentence)
    return st.capitalize()

print(filter_words(st))'''

# Task 4 Convert a Number to a String!

'''num = 67
def number_to_string(num):
    return str(num)
print (number_to_string(num))'''

# Task 5 Reversing Words in a String

'''st = "Hello World"
def reverse(st):
    word_list = st.split()
    return ' '.join(reversed(word_list))
print (reverse(st))'''

# Task 6 Reverse List Order

'''l = [1,2,3,4]
def reverse_list(l):
    return ((l)[::-1])
print (reverse_list(l))'''

# Task 7 Multiples of 3 or 5
'''
def solution(number):
    if number <= 0 : 
        return 0
    list_3_5 = [n for n in range (number) if n % 3 ==0 or n % 5==0]
    return (sum(list_3_5))

result = solution (1000)
print (result)
'''
# Task 8 Will you make it?

'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
   return True if (mpg * fuel_left) >= distance_to_pump else False 
print (zero_fuel(51, 25, 2)) 
'''
# Task 9 Are You Playing Banjo? 
'''def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print (are_you_playing_banjo("Rikke"))
'''
# Task 10 Convert boolean values to strings 'Yes' or 'No'.
'''
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
print (bool_to_word(False))
'''

# Task 11 Counting sheep
'''
sheep = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    return sum (1 for s in sheep if s == True )
print (count_sheeps(sheep))
'''
# Task 12 

def correct_tail(body, tail):
     return body [-1] == tail
print (correct_tail("fox", "x"))