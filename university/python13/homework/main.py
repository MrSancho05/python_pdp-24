# task 1
# summa = 0
# rNam = 0
# while type(rNam) != :
#     rNam = (input('Enter number: '))
#     summa += int(rNam)
#     if rNam == 0: break
# print(summa)

# task 2
# a = int(input('a: '))
# b = int(input('b: '))

# summa = 0
# while a < b:
#     summa += a
#     print(a)
#     a += 1
# print(summa)

# task 3
# nums = [1,2,3]
# n = int(input('Enter n: '))

# i = 1
# while i <= n:
#     num = int(input('Enter num: '))
#     nums.append(num)
#     i += 1
# print(nums)

# task 4
# x = [1, 2, 3, 14, 5, 6, 6, 7] 
# i = 0
# max = x[0]

# while i < len(x):
#     if max < x[i] : max = x[i]
#     i += 1
# print(max)

# task 5
# x = [1, 2, 3, 14, 5, 6, 6, 7]
# i = 0
# max = x[0]
# maxI = 0

# while i < len(x):
#     if max < x[i] : 
#         max = x[i]
#         maxI = i
#     i += 1
# print(maxI)

# task 6
# num = int(input('Enter number: '))
# sanoq = 0
# while num > 0:
#     num //= 10
#     sanoq += 1
# print(sanoq)  

# task 7 
# x = [1, 2, 0, 14, 5, -6] 
# max = x[0]
# min = x[0]

# i = 0
# while i < len(x):
#     if max < x[i]: max = x[i] 
#     if min > x[i]: min = x[i] 
#     i += 1
# print(max)
# print(min)

# task 8
x = [-2, 31, 104, 51, 19, 7] 
max = x[0]
min = x[0]
maxI = 0
minI = 0

i = 0
while i < len(x):
    if max < x[i]: 
        max = x[i] 
        maxI = i
    if min > x[i]: 
        min = x[i] 
        minI = i
    i += 1
help = max
x[maxI] = min
x[minI] = help
print(x)

# task 9
# x = [-2, 31, 104, 51, 19, 7]
# num = int(input('num: '))
# i = 0
# counter = 0
# while i < len(x):
#     if num == x[i]:
#         counter += 1 
#     i += 1
# if counter > 0 : print('Element bor')
# else : print('Element yoq')

# task 10
# EKUB
# a = int(input('a: '))
# b = int(input('b: '))

# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(f'EKUB: {a}')

# 11 TASK
# EKUK
# max_num = max(a,b)
# while True:
#     if max_num % a == 0 and max_num % b == 0:
#         ekuk = max_num
#         break
#     max_num += max(a,b)
# print(f'{a} va {b} EKUK: {ekuk}')

# task 12
# a = int(input('a: '))
# b = int(input('b: '))
# sanoq = 0
# while a >= b:
#     sanoq += 1
#     a -= b
#     if a < b: break 

# print(sanoq)
# print(a)

# task 13
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# nums = []

# while a >= b:
#     a -= b
#     nums.append(a)
#     # print(a)
# print(nums[len(nums) - 1])

# task 14
a = int(input('Enter a: '))
b = int(input('Enter b: '))
sanoq = 0
while a >= b:
    a -= b
    sanoq += 1  
print(sanoq)



