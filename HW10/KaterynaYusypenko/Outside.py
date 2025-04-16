# Ball-super-ball
#
# class Ball:
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
# #####################################################

# Color-ghost

# import random
#
# class Ghost(object):
#   def __init__(self):
#     self.color = random.choice(["white", "yellow", "purple", "red"])
# ghost1 = Ghost()
# print(ghost1.color)
######################################################

# Basic-subclasses-Adam-and-Eve

# def God():
#     adam = Man("Adam")
#     eve = Woman("Eve")
#     return [adam, eve]
#
# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Man(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)
# humans = God()
# for human in humans:
#     print(human.name)
##################################################

# Classy-classes

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f"{name}s age is {age}"  # Використовуємо f-рядки для форматування
#
#     def get_info(self):
#         return self.info
#
#     @property
#     def info_property(self):
#         return self.info
################################################

#Building Spheres

# from math import pi
#
#
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = round(4 * pi * radius ** 3 / 3, 5)
#         self.surface_area = round(4 * pi * radius ** 2, 5)
#         self.density = round(self.mass / self.volume, 5)
#
#     def __getattr__(self, name):
#         return lambda: getattr(self, name[4:])
# sphere = Sphere(5, 100)
#
# print(sphere.volume)
# print(sphere.surface_area)
# print(sphere.density)
# print(sphere.get_volume())
# print(sphere.get_surface_area())
# print(sphere.get_density())
###################################################

#Dynamic Classes
#
# class InvalidClassNameError(Exception):
#     pass
#
# def class_name_changer(cls, new_name):
#     if not new_name[0].isupper() or not new_name.isalnum():
#         raise InvalidClassNameError(
#             'Invalid class name!')
#
#     cls.__name__ = new_name
#
# class MyClass:
#     pass
#
# print(MyClass.__name__)
#
# try:
#     class_name_changer(MyClass, "NewName")
#     print(MyClass.__name__)
# except InvalidClassNameError as e:
#     print(e)
#
# try:
#     class_name_changer(MyClass, "invalid_class")
# except InvalidClassNameError as e:
#     print(e)





