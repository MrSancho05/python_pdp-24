class Bank:
    foiz = 12.3
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Bank.foiz = Bank.foiz
    
    def describe(self):
        print(f'\nName: {self.name}\nBalance: {self.balance}')