class Animal:
    def __init__(self, name, age, hasTail):
        self.name = name
        self.age = age
        self.hasTail = hasTail
        self.is_alive = True
    
    def eat(self):
        print(f'{self.name} eating!')
    
    def run(self):
        print(f'{self.name} running!')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sleep(self):
        print(f'{self.name} is sleeping!')