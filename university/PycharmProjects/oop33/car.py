class Car:
    def __init__(self, model, color, year, price, is_sale):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.is_sale = is_sale
    
    def run(self):
        print(f'{self.model} running!')

    def stop(self):
        print(f'{self.model} stopping!')

    def description(self):
        print(f'Car model is {self.model}\ncar color {self.color}\ncar production year {self.year}\ncar price {self.price}\ncar is sale {self.is_sale}\n')