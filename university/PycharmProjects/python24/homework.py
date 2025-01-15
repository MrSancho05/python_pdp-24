def intNumber():
    num = int(input('Son kiriting: '))
    return num

def floatNumber():
    num = float(input('Son kiriting: '))
    return num

# 1
# def PowerA3(num):
#     return num ** 3

# a = floatNumber()
# b = floatNumber()
# c = floatNumber()
# d = intNumber()
# e = intNumber()

# print(PowerA3(a))
# print(PowerA3(b))
# print(PowerA3(c))
# print(PowerA3(d))
# print(PowerA3(e))

# 2 vazifa
# def PowerA234(num):
#     return num ** 2, num ** 3, num ** 4

# a = floatNumber()
# b = floatNumber()
# c = floatNumber()
# print(PowerA234(a))
# print(PowerA234(b))
# print(PowerA234(c))

# 3
# def Mean(a,b):
#     return (a + b) / 2, pow(a*b, 1/3)

# a = floatNumber()
# b = floatNumber()
# c = floatNumber()
# d = floatNumber()
# print(Mean(a,b), Mean(a,c), Mean(a,d))

# 4 
# def Triangle(a,b,c):
#     return a + b + c, (a + b) / 2
# a = floatNumber() 
# b = floatNumber() 
# c = floatNumber() 
# print(Triangle(a,b,c))

# 5
# def RectPS(a,b):
#     return 2 * (a + b), a * b
# a, b = intNumber(), intNumber()
# print(RectPS(a,b))

# 6
# x = intNumber()
# # boshlang'ich fn hammasi shu yerdade)
# def DigitCountSum(x):
#     text = str(x)
#     counter = sum = 0
#     for i in text:
#         print(i)
#         counter += 1
#         sum += int(i)
#     return f'Summa: {sum}, Sonlar miqdori: {counter}'
# res = DigitCountSum(x)
# print(res)

# 7
# def intNumber2():
#     num = (input('Son kiriting: '))
#     return num
# x = intNumber2()
# def invertDigit(num):
#     text = ''
#     for i in num:
#         text = i + text
#     return text
# res = invertDigit(x)
# print(res)
# a,b,c = str(intNumber()), str(intNumber()), str(intNumber())
# print(invertDigit(a))
# print(invertDigit(b))
# print(invertDigit(c))

# 8
# a = str(intNumber())
# aNum = input('Raqam kiriting: ')
# b = str(intNumber())
# bNum = input('Raqam kiriting: ')
# c = str(intNumber())
# cNum = input('Raqam kiriting: ')
# def addRightDigit(son,raqam):
#     if 1 <= int(raqam) <= 9:
#         return son + raqam
#     else: return 'Son bir xonali va 0 dan katta bo\'lishi lozim!'
# a = str(intNumber())
# aNum = input('Raqam kiriting: ')
# print(addRightDigit(a, aNum))
# print(addRightDigit(b, bNum))
# print(addRightDigit(c, cNum))

# 9
# def addLeftDigit(a,b):
#         if 1 <= int(b) <= 9:
#             return b + a
#         else: return 'Son bir xonali va 0 dan katta bo\'lishi lozim!'
# a = str(intNumber())
# b = input('Raqam kiriting: ')
# print(addLeftDigit(a, b))

# 10
# def Swap(a,b):
#     helper = a
#     a = b
#     b = helper
#     return a, b

# a = intNumber()
# b = intNumber()
# print(Swap(a,b))

# 11
# def minMax(a, b):
#     if a > b:
#         return f'max : {a}, min : {b}'
#     else:
#         return f'max : {b}, min : {a}'

# x = intNumber()
# y = intNumber()
# x2 = intNumber()
# y2 = intNumber()
# print(minMax(x,y))
# print(minMax(x2,y2))

# 12 13
# def sortInc3(a,b,c):
#     sum = a + b + c
    # min = a
    # max = a
    # if min > b:
    #     min = b
    # if min > c:
    #     min = c
    # if max < b:
    #     max = b
    # if max < c:
    #     max = c
#     minN = min(a,b,c)
#     maxN = max(a,b,c)
#     middle = sum - (minN + maxN)
#     return f'min: {minN}, middle: {middle}, max: {maxN}', f'min: {maxN}, middle: {middle}, max: {minN}'

# a = intNumber()
# b = intNumber()
# c = intNumber()
# print(sortInc3(a,b,c))

# 14
# def shiftRight3(a,b,c):
#     # 1 2 3
#     # 3 1 2
#     sum = a + b + c
#     a = sum - (a + b)
#     b = sum - (a + b)
#     c = sum - (a + b)
#     return a,b,c
# a = intNumber()
# b = intNumber()
# c = intNumber()
# print(shiftRight3(a,b,c))

# 15
# def shiftRight3(a,b,c):
#     # 1 2 3
#     # 2 3 1
#     sum = a + b + c
#     c = sum - (b + c)
#     b = sum - (b + c)
#     a = sum - (b + c)
#     return a,b,c
# a = intNumber()
# b = intNumber()
# c = intNumber()
# print(shiftRight3(a,b,c))

# 16
# def ishora(a):
#     if a > 0:
#         return 1
#     elif a == 0:
#         return 0
#     else: return -1
# a = floatNumber()
# print(ishora(a))
    
# 17
# def kvd(a,b,c,x):
#     res = a * x**2 + b * x + c
#     if res > 0:
#         return 2
#     elif res == 0:
#         return 1
#     else:
#         return 0
# a = intNumber()
# b = intNumber()
# c = intNumber()
# x = intNumber()
# print(kvd(a,b,c,x))

# 18
# def doiraYuz(R):
#     pi = 3.14
#     return pi * R**2

# r = intNumber()
# print(doiraYuz(r))

# # 19
# def doiraYuz(r, r2):
#     pi = 3.14
#     R = pi * (r ** 2)
#     R2 = pi * (r2 ** 2)
#     return abs(R - R2)

# r = intNumber()
# r2 = intNumber()
# print(doiraYuz(r, r2))


# 20
# import math
# def triangleP(a,b):
#     c = round(math.sqrt(a**2 + b**2))
#     return a + b + c
# a = intNumber()
# b = intNumber()
# print(triangleP(a,b))