class Human:
    species = "Homosapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def welcome(self):
        print("Welcome {}".format(self.name))

    @classmethod
    def print_species(cls):
        return f"Human is: {cls.species}"

    @staticmethod
    def arbitrary_method(message = "You entered nothing"):
        return f"{message}"



Joe = Human("Joe", 24)
Joe.welcome()
print(Joe.arbitrary_method())
print(Joe.arbitrary_method("Now something is entered"))

print(Human.arbitrary_method("Class method with something entered"))
print(Human.print_species())

