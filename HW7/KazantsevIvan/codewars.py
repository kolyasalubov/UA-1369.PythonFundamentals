# Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round((((x1 - x2)**2 + (y1-y2)**2)**0.5),2)

# No yelling!

def filter_words(st):
    temp = " ".join(st.lower().capitalize().split())
    return temp

# Convert a Number to a String

def number_to_string(num):
    return str(num)

# Reversing Words in a String

def reverse(st):
    temp = st.split()
    temp.reverse()
    return " ".join(temp)

# Reverse List Order

def reverse_list(l):
  return list(reversed(l))

# Multiples of 3 or 5

def solution(number):
    mylist = []
    if number<0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i%5 == 0:
            mylist.append(i)
    return sum(mylist)

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left*mpg < distance_to_pump:
        return False
    return True

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name+" plays banjo"
    return name+" does not play banjo"

# Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

# Counting sheep

def count_sheeps(sheep):
    return sheep.count(True)

# Is this my tail?

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    return False

