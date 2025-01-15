class Computer:
    compCounter = 0
    def __init__(self, brend, year, memory, hasFingerprint, hasFaceID):
        self.brend  = brend
        self.year = year
        self.memory = memory
        self.hasFingerprint = hasFingerprint
        self.hasFaceID = hasFaceID
        Computer.compCounter += 1
    
    def compInfo(self):
        print(f'Comp count: {Computer.compCounter}')
        print(f'Comp brend: {self.brend}\nComp year: {self.year}\nComp memory: {self.memory}\nComp hasFingerprint: {self.hasFingerprint}\nComp hasFaceID: {self.hasFaceID}\n')

    
class HP(Computer):
    pass

class MAC(Computer):
    pass

class Lenovo(Computer):
    pass

class Acer(Computer):
    pass