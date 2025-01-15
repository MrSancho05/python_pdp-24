class Technical:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

class Phone(Technical):
    def call(self, model):
        print(f'calling {model}!...')

class TV(Technical):
    def watch(self, model):
        print(f'watching {model}!...')

class Fridge(Technical):
    def frize(self, model):
        print(f'frizing {model}!...')