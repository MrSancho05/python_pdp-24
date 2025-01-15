# def defaultParam(name = "my friend"):
#     print(f'Hello {name}:)')

# defaultParam()
# defaultParam('Bob')

# def infoPerson(name, age):
#     print(f'Name: {name}')
#     print(f'Age: {age}')

# infoPerson(age = 18, name = 'Bob')


# def elementMax(toplam):
#     katta = toplam[0]
#     for i in toplam:
#         if katta < i:
#             katta = i
#     return katta

# l = [1,2,5,8,9,12,5,63,69,36]
# print(elementMax(l))


# def yigindi(*x):
#     summa = 0
#     print(type(x))
#     for i in x:
#         summa += i
#     return summa
# print(yigindi(1,2,3,4,5))


# def nums(**x):
#     print(x['three'])
#     print(type(x))
#     print(x)
# nums(one = 1, two = 2, three = 3)


def infoPerson(**info):
    for key, value in info.items():
        print(f'{key}: {value}')

infoPerson(name = 'Eshmat', surname = 'Toshmatov', age = 25, job = 'Manager', isMarried = False, adress = 'Tashkent', phone = '+(998)-95-908-91-99', email = 'clay@gmail.com')
