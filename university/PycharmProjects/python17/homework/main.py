# task 1
# k = int(input('Enter k: '))
# n = int(input('Enter n (n > 0): '))
#
# for i in range(n):
#     print(k)
#
# task 2
# a = int(input('Enter a (a < b): '))
# b = int(input('Enter b: '))
# counter = 0
# for a in range(a, b+1):
#     counter += 1
#     print(a)
# print(f'a dan b gacha sonlar miqdori: {counter} ta')
#
# task 3
# a = int(input('Enter a (a < b): '))
# b = int(input('Enter b: '))
# counter = 0
# if a < b:
#     for a in range(b-1, a, -1):
#         print(a)
#         counter += 1
# else:
#     print("a soni b dan katta")
# print(f'b dan a gacha sonlar miqdori: {counter} ta')
#
# task 4
# price = float(input('Enter price: '))
#
# for i in range(1,11):
#     print(f'{i}kg : {i * price} sum')
#
# task 5
# price = float(input('Enter price: '))
#
# for i in range(1, 11):
#     print(f'{i / 10} kg: {i / 10 * price} sum')
#
# task 6
# price = int(input('Enter price: '))
#
# for i in range(1, 10):
#     a = i * 0.1
#     print(a)
#
# for i in range(11, 21):
#     print(f'{i / 10} kg: {i / 10 * price} sum')
#
# task 7, 8
# a = int(input('Enter a (a < b): '))
# b = int(input('Enter b: '))
# sum = 0
# mult = 1
# for i in range(a, b+1):
#     sum += i
#     mult *= i
# print(sum)
# print(mult)
#
# task 9
# a = int(input('Enter a (a < b): '))
# b = int(input('Enter b: '))
# sum = 0
# for i in range(a, b + 1):
#     sum += i * i
# print(sum)
#
# task 10
# n = int(input("Enter n number: "))
# sum = 0
# for i in range(1,n + 1):
#     sum += 1 / i
#     print(i)
# print(sum)
#
# task 11
# n = int(input('Enter n number: '))
# sum = 0
# for i in range(n, 2 * n + 1):
#     sum += i ** 2
#     print(i, sum)
# print(sum)
#
# task 12
# n = int(input('Enter n number: '))
# mult = 1
#
# for i in range(1, n + 1):
#     mult *= 1 + ((i * 10) / 100)
# print(mult)

# task 13
# n = int(input('Enter n number: '))
# a = 1
# S = 0
#
# for i in range(1, n + 1) :
#     # print((1 + i * 10 / 100) * a)
#     S += (1 + i * 10 / 100) * a
#     a = -a
# print(S)

# task 14
# n = int(input('Enter n number: '))
# S = 0
#
# for i in range(1, 2*n):
#     if i % 2 != 0:
#         S += i
#         print(S)
# print(S)

# task 15
# n = int(input('Enter n number (n > 0): '))
# a = int(input('Enter a number: '))
# darajaN = 1
#
# for i in range(1 , n+1):
#     darajaN *= a
# print(darajaN)

# task 16
# n = int(input('Enter n number (n > 0): '))
# a = int(input('Enter a number: '))
# darajaN = 1
#
# for i in range(1, n+1):
#     darajaN *= a
#     print(f'{i} chi daraja = {darajaN}')


