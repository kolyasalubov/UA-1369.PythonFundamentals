# Завдання 2
# Створіть клас Human. Кожна людина має ім'я. 
# Створіть метод у класі, 
# який відображає вітальне повідомлення для кожної людини. 
# Створіть метод класу, який повертає інформацію про те, що це вид "Homo sapiens".
#  А в класі створіть статичний метод, який повертає довільне повідомлення.

class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Вітаємо, {self.name}!"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "Це повідомлення про закінчення програми."


# Приклад використання
human = Human("Андрій")
print(human.welcome())
print(Human.get_species())
print(Human.arbitrary_message())