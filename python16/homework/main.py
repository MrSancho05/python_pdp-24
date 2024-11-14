# 13/11/2024 Programming - Homework
# task 1
# k sonini n marta
# n = int(input("Enter n : "))
# k = int(input("Enter k : "))
#
# for i in range(n):
#     print(k)
from sys import flags

# task 2
# a va b sonlari orasidagi hamma sonlarni miqdori va o'zinni  chiqaruvchi programma
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# counter = 0
# for a in range(a, b + 1):
#     print(a)
#     counter += 1
# print(f"a va b sonlar orasidagi sonlar miqdori {counter}")

# task 3
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# counter = 0
# reversedList = []
# for a in range(a + 1, b):
#     print(a, end=" ")
#     reversedList.append(a)
#     counter += 1
#
# reversedList.reverse()
# print()
# for i in reversedList:
#     print(i, end=' ')
#     counter += 1
# print()
# print(f"Jami sonlar miqdori: {counter}")

# task 4
# kgPrice = float(input('Enter price of sweet: '))
#
# for i in range(1,11):
#     print(f'{i} kg: {kgPrice * i}')

# task 5
# kgPrice = float(input('Enter price of sweet: '))
# for i in range(1, 11):
#     print(f'{i / 10} kg sweet price : {kgPrice * (i / 10)}')

# task 6
# kgPrice = float(input('Enter price of sweet: '))
# for i in range(1, 11):
#         print(f'{(i / 10) + 1} kg sweet price : {kgPrice * (i / 10 + 1)}')

# task 7
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# summa = 0
# for a in range(a,b+1):
#     # print(a)
#     summa += a
# print(summa)

# task 8
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# multiply = 1
# for a in range(a, b+1):
#     # print(a)
#     multiply *= a
# print(multiply)

# task 9
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# multiply = 0
# for a in range(a, b+1):
#     multiply += pow(a, 2)
#     # multiply += a*a
# print(multiply)

# task 10
# n = int(input('Enter n: '))
# summa = 0
# for i in range(1, n+1):
#     summa += 1/i
# print(summa)

# task 11
# n = int(input("n sonini kiriting (n > 0): "))
# S = 0
#
# for i in range(n, 2 * n + 1):
#     S += i ** 2
#
# print("Yig'indi S =", S)

# task 12
# n = float(input('n sonini kiriting (n > 0): '))
# s = 1
# if n > 1.1:
#     for x in range(11, int(n * 10) + 1):
#         s *= x / 10
#     print(s)
# else:
#     print('0 dan katta son kiriting')

# task 13
# n = int(input("n sonini kiriting (n > 0): "))
# s = 0
#
# for x in range(11, (n * 10) + 1):
#     if x % 2 != 0:
#         s += x / 10
#     else: s -= x / 10
#     print(x / 10)
# print(f'Javob: {s}')

# task 14
# ???

# task 15
# a = float(input("a sonini kiriting : "))
# n = int(input("a sonining darajasini kiriting: "))
# m = 1
# for x in range(n):
#     m *= a
#     print(a)
# print(m)

# task 16
a = float(input("a sonini kiriting : "))
n = int(input("a sonining darajasini kiriting: "))
m = 1
for x in range(n):
    m *= a
    print(int(m))
