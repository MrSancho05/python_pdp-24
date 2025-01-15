# 1 - masala
# List berilgan listning ichida biz qidirgan element
# bor yoki yoqligni tekshirirng bor bo'lsa True aks
# holda False chiqaring
# el = input('Enter element: ')
# rList = ['hello', "7", "True", "False", "bye"]
# sanoq = 0
# i = 0
# while i < len(rList):
#     if el == rList[i]: sanoq+=1
#     i += 1 
# if sanoq > 0 : print(True)
# else: print(False)

# 2 - masala
# Barcha 3 - xonali sonlar ichida raqamlari yi'gindisi
# 5 dan katta va 8 dan kichik bo'lganlarini ekranga chiqaring
# i = 100
# while i < 1000:
#     b = i % 10
#     o = i // 10 % 10
#     y = i // 100
#     if 5 < b + o + y < 8:
#         print(i)
#     i += 1

# 3 - masala
# Ekrandan son kiritilsa shu son necha xonali ekangini aniqlang
# num = int(input('Enter num: '))
# sanoq = 0
# while num > 0:
#     sanoq += 1
#     num //= 10
# print(sanoq)

# 4 - masala
# Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni
# yig'indisini chiqaring
# i = 0
# sum = 0
# while i < 5:
#     num = int(input(f'Enter {i + 1} number: '))
#     sum += num
#     i += 1
# print(sum)

# 5 - masala
# Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni
# kattasini chiqaring
# i = 0
# l = []
# while i < 5:
#     num = int(input(f'Enter {i + 1} number: '))
#     l.append(num)
#     i += 1

# i2 = 0
# max_num = l[0]
# while i2 < len(l):
#     if max_num < l[i2]: max_num = l[i2]
#     i2 += 1
# print(max_num)

# 6 - masala
# Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni
# kichigini chiqaring
# i = 0
# l = []
# while i < 5:
#     num = int(input(f'Enter {i + 1} number: '))
#     l.append(num)
#     i += 1

# i2 = 0
# min_num = l[0]
# while i2 < len(l):
#     if min_num > l[i2]: min_num = l[i2]
#     i2 += 1
# print(min_num)

# 7 - masala
# List yarating hosil bolgan listning har bir elementiga 2 ni ko'paytirib
# ekranga chiqaring
# i = 0
# nums = [1,2,3,4,5]
# while i < len(nums):
#     nums[i] *= 2
#     i += 1
# print(nums)

# 8 - masala
# Mukammal son yoki Mukammal son elasligini tekshiring mukammal sonlar
# o'zidan tashqari bo'luvchilarini yig'indisi o'ziga teng
# Masalan : 28 -> 1,2,4,7,14 shu sonlarning yigindisi 28 ga teng
# num = int(input('num: '))
# i = 1
# sum = 0
# while i < num:
#     if num % i == 0:
#         print(i)
#         sum += i
#     i += 1
# if sum == num: print(True)
# else: print(False)

# 9 - masala
# Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa darajasi aks
# holda darajasi emas kabi so'zlarni chiqaring
# num = int(input('num: '))
# i = 1
# check = False
# while i <= num:
#     if i == num:
#         check = True
#     i *= 2
# if check: print('2 ning darajasi')
# else: print('2 ning darajasi emas')

# 10 - masala
# Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa nechanchi darajasi ekanligini aks holda darajasi emas kabi so'zlarni chiqaring
num = int(input('num: '))
i = 1
sanoq = -1
check = False
while i <= num:
    if i == num:
        check = True
    sanoq += 1
    i *= 2
if check: print(sanoq)
else: print('2 ning darajasi emas')


# 11 - malasa
# Ekrandan son kiritiladi shu sonning faktorialini chiqaring

# 12 - masala

# List berilgan x = [1,23,10,45,-41,56,78,13] shu listning juft va toq elementlarini 2 ta alohida listga yuklang
# juft = [10,56, 78]
# toq = [1,23,45,-41,13]
# x = [1,23,10,45,-41,56,78,13]
# i = 0
# juft = []
# toq = []
# while i < len(x):
#     if x[i] % 2 == 0:
#         juft.append(x[i])
#     else: toq.append(x[i])
#     i += 1
# print(juft)
# print(toq)

# 13 - masala
# Ekrandan biror son kiritilsa shunga mos holda karra jadvalini chiqaring
# son = 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ........
# num = int(input('Enter num: '))
# i = 1
# while i <= 10:
#     print(f'{num} * {i} = {num * i}')
#     i += 1


# 14 - masala
# List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] berilgan list elementlari ichidan eng uzun so'zni toping va uni ekranga chiqaring

# 15 - malasa

# List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] berilgan list elementlari ichidan a harfi bilan tugaydiganlarni ekranga chiqaring

# Masalan : Tayota, Mazda, Lada


