class Staf:
    stafCounter = 0
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        Staf.stafCounter += 1
    
    def stafInfo(self):
        print(f'Staf count: {Staf.stafCounter}')
        print(f'{self.name} is a {self.position} and (he|she) is {self.age} years old\n')
    

class Staf1(Staf):
    pass

class Staf2(Staf):
    pass

class Staf3(Staf):
    pass


class Fish:
    fishCounter = 0
    def __init__(self, name, age, is_wild):
        self.name = name
        self.age = age
        self.is_wild = is_wild
        Fish.fishCounter += 1
    
    def fishInfo(self):
        print(f'Fish count: {Fish.fishCounter}')
        print(f'Name: {self.name}\nAge: {self.age}\nIs wild?: {self.is_wild}\n') 
    

class Delphin(Fish):
    pass

class Shark(Fish):
    pass

class Whale(Fish):
    pass