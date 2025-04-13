class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        print("This is an arbitrary message.")


human1 = Human("John")
human1.welcome()  

print(human1.species())  

human1.arbitrary_message()  
