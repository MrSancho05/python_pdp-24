from classes import *

def main():
    staf1 = Staf1('Farxod', 25, 'Dean')
    staf1.stafInfo()
    staf2 = Staf2('Muhammadsobir', 30, 'Teacher')
    staf2.stafInfo()
    staf3 = Staf3('Faruh', 22, 'HR manager')
    staf3.stafInfo()
    print(f'Total staf count: {Staf.stafCounter}\n')

    shark = Shark('Shark', 5, True)
    shark.fishInfo()
    delphin = Delphin('Delphin', 3, False)
    delphin.fishInfo()
    whale = Whale('Whale', 8, False)
    whale.fishInfo()
    print(f'Total fish count: {Staf.stafCounter}\n')

if __name__ == '__main__':
    main()