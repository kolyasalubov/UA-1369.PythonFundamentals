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
        print("Arbitrary message.")

human1 = Human("Kate")
human1.welcome()
print(human1.species())
human1.arbitrary_message()