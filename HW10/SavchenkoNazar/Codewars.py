import random
import math

# Task 1 Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular.
"""
class Ball ():
    def __init__(self,ball_type="regular"):  #підхід якщо не задано, пише regular
        self.ball_type = ball_type  
ball_one = Ball("Best")
ball_two = Ball()

print(ball_one.ball_type)
print(ball_two.ball_type)

"""

# Color-ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

'''
class Ghost():
    colors = ["white","yellow","purple","red"]
    def __init__(self):
        self.color = random.choice(Ghost.colors)

casper_one = Ghost()
casper_two = Ghost()

print(casper_one.color)
print(casper_two.color)

'''

# Basic subclasses - Adam and Eve
'''
class Human():
    pass

class Woman(Human):
    pass

class Man(Human):
    pass

def God():
    return [Woman(), Man()]

lord = God()

print(type(lord[0]))
print(type(lord[1]))
'''

#  Classy-classes 
'''

class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

ppl = Person("Nazar",35)
print (ppl.info)

'''
# Building Spheres 
'''
class Sphere():
    def __init__(self,radius,mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        volume = (4.0 * 3.0) / math.pi * (self.radius ** 3)
        return round(volume,5)
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius**2)
        return round(surface_area,5)
    
    def get_density (self):
        volume = self.get_volume()
        density = self.mass / volume
        return round(density,5)
ball = Sphere(2,50)

print(ball.get_radius())      
print(ball.get_mass())         
print(ball.get_volume())     
print(ball.get_surface_area()) 
print(ball.get_density())

'''
# Python's Dynamic Classes #1 

def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("Invalid class name")
    cls.__name__ = new_name