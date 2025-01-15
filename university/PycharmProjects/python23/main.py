rows = 10
cols = 10
number = 1
parking = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
while number != 4:
    print("Menu: ")
    print('1. Avtoni pakovkaga joylash')
    print('2. Avtoni parkovkadan olib tashlash')
    print('3. Parkovkani ko\'rish')
    print('4. Dastruni toxtatish')
    number = int(input('Tanlang [1 | 2  | 3]: '))
    if number == 1:
        row = int(input('Qaysi qatorda: '))
        col = int(input('Qaysi ustunga: '))
        carName = input('Moshina nomi: ')
        print(row)
        print(col)
        print(carName)
        if 1 <= row <= 10 and 1 <= col <= 10:
            if parking[row - 1][col - 1] == 0:
                parking[row - 1][col - 1] = carName
                print('Mavaffaqiyatli qoshildi!')  
            else: 
                print(f'Bu joyda {parking[row - 1][col - 1]} avtomobili bor')
    elif number == 2 :
        row = int(input('Qaysi qatorda: '))
        col = int(input('Qaysi ustunga: '))
        if 1 <= row <= 10 and 1 <= col <= 10:
            if parking[row - 1][col - 1] == carName:
                parking[row - 1][col - 1] = 0
                print('Mavaffaqiyatli olib tashlandi!')  
            else: 
                print(f'Bu yerda avto mavjud emas')
    elif number == 3:
        for i in range(len(parking)):
            for j in range(len(parking)):
                print(parking[i][j], end=' ')
            print()
else: print('Dastur toxtatildi!')
