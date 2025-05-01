# Task2. Create a class Human, everyone has a name, create a method in the
# class that displays a welcome message to each person. Create a class method
# in the class that returns information that it is a species of "Homosapiens". And
# in the class create a static method that returns an arbitrary message.


class Human:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print (f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens", cls
    
    @staticmethod
    def arbitrary_message():
        return 'Arbitrary message'
    

h = Human("Harry")
h.display()
print(h.species())
print(h.arbitrary_message())