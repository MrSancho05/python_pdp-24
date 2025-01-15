from car import Car
def main():
    """Main started"""
    # print(main.__doc__)
    car1 = Car('Mustang', 'red', 2022, 150000, False)
    car2 = Car('Ford', 'black', 2015, 130000, True)
    car3 = Car('Mers', 'gray', 2024, 300000, True)

    car1.description()
    car2.description()
    car3.description()
    pass

if __name__ == "__main__":
    main()