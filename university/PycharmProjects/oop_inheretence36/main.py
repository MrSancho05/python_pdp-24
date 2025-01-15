from computer import *
from phone import *
def main():
    # hp = HP('HP', 2020, 350, True, False)
    # hp.compInfo()
    # mac = MAC('Mac', 2022, 560, True, True)
    # mac.compInfo()
    # lenovo = Lenovo('Lenovo', 2024, 520, False, False)
    # lenovo.compInfo()
    # acer = Acer('Acer', 2019, 120, False, False)
    # acer.compInfo()
    # print(f'Total comp count: {Computer.compCounter}')

    samsung = Samsung('A21', 4, 32, 'Yellow', 2017)
    samsung.phoneInfo()
    samsung.pencil()
    iphone = Iphone('13Pro', 6, 64, 'Red', 2022)
    iphone.phoneInfo()
    iphone.kamera()
    xiomi = Xiomi('Poco x3 NFC', 4, 64, 'Black', 2022)
    xiomi.phoneInfo()
    xiomi.charge()



if __name__ == '__main__':
    main()