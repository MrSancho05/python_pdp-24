# # x = 12
# # x = 'Hi'
# # print(x)

# son = 127
# s = 0
# # while son > 0:
# #     q = son % 10
# #     s += q
# #     son = son // 10
# # print(s)

# # def summaN(son):
# #     if son > 0:
# #         return son % 10 + summaN(son // 10)
# #     else:
# #         return 0
    
# # print(summaN(123))


# # son = 123
# # x = 5
# # bormi = False

# # while son > 0:
# #     q = son % 10
# #     if q == x:
# #         bormi = True
# #         break
# #     son //= 10
# # print(bormi)


# # def findNumber(son,x):
# #     if son > 0:
# #         q = son % 10
# #         print(q)
# #         if q == x:
# #             return True
# #         findNumber(son // 10, x)
# #     return False
# # print(findNumber(153,5))


# class Car:
#     def __init__(self, name, yProduction, color, speed):
#         self.name = name
#         self.yProduction = yProduction
#         self.color = color
#         self.speed = speed

#     def __str__(self):
#         return f"name: {self.name}\nyProduction: {self.yProduction}\ncolor: {self.color}\nspeed: {self.speed}"
# # car1 = Car('Malibu', 2010, 'Black', '250')
# # print(car1)
# # print()
# # car2 = Car('Jentra', 2013, 'White', '200')
# # print(car2)
# # print()
# # car3 = Car('Jiguli', 1974, 'Blue', '180')
# # print(car3)
# # print()


# class Pen:
#     def __init__(self, color, price, yProduct, IsGely):
#         self.color = color
#         self.price = price
#         self.yProduct = yProduct
#         self.IsGely = IsGely
    
#     def __str__(self):
#         return f"color: {self.color}\nprice: {self.price}\nyProduct: {self.yProduct}\nIsGely: {self.IsGely}"
    
# pen = Pen('Red', 5000, 2020, True)
# print(pen)
# print()
# pen2 = Pen('Black', 3000, 2019, False)
# print(pen2)
# print()
# pen3 = Pen('Blue', 4000, 2024, True)
# print(pen3)
# print()
# pen4 = Pen('Green', 3500, 2021, False)
# print(pen4)
# print()


# class Book:
#     def __init__(self, yProduct, color, janr, author, price):
#         self.yProduction = yProduct
#         self.color = color
#         self.janr = janr
#         self.author = author
#         self.price = price
#     def __str__(self):
#         return f"yProduction: {self.yProduction}\ncolor: {self.color}\njanr: {self.janr}\nauthor: {self.author}\nprice: {self.price}"
    
# book = Book(2020, 'Red', 'Fantasy', 'Someone', 50000)
# print(book)
# print()
# book2 = Book(2019, 'Black', 'Detective', 'Someone', 75000)
# print(book2)
# print()
# book3 = Book(2021, 'Green', 'History', 'Someone', 100000)
# print(book3)
# print()


# class Staff:
#     def __init__(self, name, age, salary, position):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.position = position
#     def __str__(self):
#         return f"name: {self.name}\nage: {self.age}\nsalary: {self.salary}\nposition: {self.position}"

# staff = Staff('Sanjarbek', 20, 120000, 'Sowtware Engineer')
# print(staff)
# print()
# staff2 = Staff('Dilmurod', 26, 100000, 'Data Scientist')
# print(staff2)
# print()
# staff3 = Staff('Temur', 18, 80000, 'Artificial Intelligence Engineer')
# print(staff3)
# print()


# class University:
#     def __init__(self, name, location, rating, facultysCount, studentsCount):
#         self.name = name
#         self.location = location
#         self.rating = rating
#         self.facultysCount = facultysCount
#         self.studentsCount = studentsCount
#     def __str__(self):
#         return f"Name: {self.name}\nLocation: {self.location}\nRating: {self.rating}\nFacultysCount: {self.facultysCount}\nStudentsCount: {self.studentsCount}"

# university = University('TUIT', 'Tashkent', 3, 10, 10000)
# print(university)
# print()
# university2 = University('PDP', 'Tashkent', 5, 4, 15000)
# print(university2)
# print()
# university3 = University('WIUT', 'Tashkent', 4, 6, 12000)


# class Umbrella:
#     def __init__(self, color, price, isOpen, yProduct, isExpensive):
#         self.color = color
#         self.price = price
#         self.isOpen = isOpen
#         self.yProduct = yProduct
#         self.isExpensive = isExpensive
#     def __str__(self):
#         return f"color: {self.color}\nprice: {self.price}\nisOpen: {self.isOpen}\nyProduct: {self.yProduct}\nisExpensive: {self.isExpensive}"
    
# ubrella = Umbrella('Red', 50000, False, 2020, True)
# print(ubrella)
# print()

# class Teacher:
#     def __init__(self, name, age, salary, subject):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.subject = subject

#     def __str__(self):
#         return f"name: {self.name}\nage: {self.age}\nsalary: {self.salary}\nsubject: {self.subject}"
    
# teacher = Teacher('Muhammadsobir', 30, 150000, 'Programming')
# print(teacher)
# print()

# class Room:
#     def __init__(self, number, floor, isFree, isClean):
#         self.number = number
#         self.floor = floor
#         self.isFree = isFree
#         self.isClean = isClean

# room = Room(219, 2, False, True)
# print(room)
# print()

# class RestLocation:
#     def __init__(self, name, location, rating, price, isBest):
#         self.name = name
#         self.location = location
#         self.rating = rating
#         self.price = price
#         self.isBest = isBest

#     def __str__(self):
#         return f"name: {self.name}\nlocation: {self.location}\nrating: {self.rating}\nprice: {self.price}\nisBest: {self.isBest}"

# restLoc = RestLocation('Ahmad joja', 'Sergeli', 4, 50000, True)   


# class 


# def element_qidir(toplam, element):
#     if element in toplam:
#         return f"{element} to'plamda mavjud."
#     else:
#         return f"{element} to'plamda mavjud emas."

# # Foydalanish:
# toplam = {1, 2, 3, 4, 5}
# element = 3

# natija = element_qidir(toplam, element)
# print(natija)


# checkWord = lambda text: True if text.endswith('@gmail.com') else False
# print(checkWord('bob@gmail.com'))


# def ismKorsat(ism):
#     print(ism)

# name = input('Salom, ismingizni kiriting:')
# ismKorsat(name)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def add(x, l):
#     if not x in lst:
#         l.append(x)
#     else:
#         print('Bu raqam ro\'yxatda mavjud')

# n = int(input('Raqam kiriting: '))
# add(n,lst)
# print(lst)


# count = 0
# def add(x,l):
#     global count
#     for i in l:
#         if x != i:
#             count += 1
#         else:
#             print('Bu raqam ro\'yxatda mavjud')
# n = int(input('Raqam kiriting: '))
# # add(n,lst)
# if count == len(lst):
#     lst.append(n)
# print(lst)


# l = ['olam', 'olma', 'alam']

# def ohirM(l):
#     for i in l:
#         print(i)
        # if l[i].endswith('m'):
        #     print(l[i])
    # return l

# res = ohirM(l)
# print(ohirM(l))


words = ["applem", "bananam", "cherry", "banana"]

def ohM(l):
    for i in range(len(l)):
        print((l[i]))
        # if len(l[i]) - 1 == 'm':
        #     i = 'kelma'
    print(l)
    
ohM(words)