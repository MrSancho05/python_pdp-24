class Phone:
    def __init__(self, model, ram, ssd, color, year):
        self.model = model
        self.ram = ram
        self.ssd = ssd
        self.color = color
        self.year = year

    def phoneInfo(self):
        print(f'\nModel: {self.model}\nRam: {self.ram}\nSSD: {self.ssd}\nColor: {self.color}\nProduction year{self.year}')


class Samsung(Phone):
    def pencil(self):
        print(f'{self.model} ruchkasiga gap yo\'q!\n')

class Iphone(Phone):
    def kamera(self):
        print(f'{self.model} kamerasiga gap yo\'q!\n')

class Xiomi(Phone):
    def charge(self):
        print(f'{self.model} zaryadiga gap yo\'q!\n')