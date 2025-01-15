from bank import *
def main():
    temurbek = Bank('Temurbek', 10000)
    temurbek.describe()

    print(temurbek.foiz)

    ismoiljon = Bank('Ismoiljon', 150000)
    # ismoiljon.foiz = 15.7
    Bank.foiz = 15.7
    ismoiljon.describe()

    print(temurbek.foiz)

    dilmurod = Bank('Dilmurod', 200000)
    # ismoiljon.foiz = 15.7
    Bank.foiz = 17.9
    ismoiljon.describe()
    print(temurbek.foiz)
    print(ismoiljon.foiz)
    print(dilmurod.foiz)

if __name__ == '__main__':
    main()
