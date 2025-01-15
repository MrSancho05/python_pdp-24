from technical import *
class Person(Phone, TV, Fridge):
    def __init__(self, name, age, adress, is_Student, model, color, year, price):

        super().__init__(model, color, year, price)
        self.name = name
        self.age = age
        self.adress = adress
        self.is_Student = is_Student
        print("test")

    def infoPerson(self):
        print(f'Name: {self.name} is {self.age} years old\nis_Student: {self.is_Student}\nAdress: {self.adress}')
        print(f'Phone model: {self.model}')

    def __str__(self):
        return f'\nPerson info: {self.name} is {self.age} years old\nis_Student: {self.is_Student}\nAdress: {self.adress}\nPhone model: {self.model}\n'