"""Create a class Human, everyone has a name, create a method in the
class that displays a welcome message to each person. Create a class method
in the class that returns information that it is a species of "Homosapiens". And
in the class create a static method that returns an arbitrary message."""

class Human():
    def __init__(self,name):
        self.name = name 
    
    def hola(self):
        print (f"Welcome {self.name}!")

    @classmethod
    def information(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary ():
        return "Nice to meet you"
    
person = Human("Nazar")
person.hola()

print(person.information())  
print(person.arbitrary())





    