class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"  # Використовуємо f-рядки для форматування

    def get_info(self):
        return self.info

    @property
    def info_property(self):
        return self.info