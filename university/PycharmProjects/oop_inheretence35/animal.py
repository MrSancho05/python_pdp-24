class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('this is animal constructor')

    def animalInfo(self):
        print(f'Animal name: {self.name}\nAnimal is {self.age} years old')

class Dog(Animal):
    pass