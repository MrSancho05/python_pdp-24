# task 1
# num = int(input('Enter num:'))
# if num > 0:
#     print(num + 1)
# else :
#     print(num)

# task 2
# num = int(input('Enter num:'))
# if num > 0:
#     print(num + 1)
# else :
#     print(num - 2)

# task 3
# num = int(input('Enter num:'))
# if num > 0:
#     print(num + 1)
# else :
#     print(num - 2)
# if num == 0:
#     num = 10
#     print(num)

# task 4
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))
# counter = 0

# if num > 0:
#     counter += 1
# if num2 > 0:
#     counter += 1
# if num3 > 0:
#     counter += 1
# print(f'Berilgan 3 ta son ichida {counter} ta musbat son mavjud')

# task 5
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))
# counter = 0
# counter2 = 0

# if num > 0:
#     counter += 1
# if num < 0:
#     counter2 += 1

# if num2 > 0:
#     counter += 1
# if num2 < 0:
#     counter2 += 1

# if num3 > 0:
#     counter += 1
# if num3 < 0:
#     counter2 += 1

# print(f'Berilgan 3 ta son ichida {counter} ta musbat va {counter2} ta manfiy son mavjud')

# task 6
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))

# max = num

# if max < num2:
#     max = num2
#     print(f'ikkinchi berilgan {num2} soni kattaroq')
# else:
#     print(f'birinchi berilgan {num} soni kattaroq')

# task 7
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))

# min = num

# if min > num2:
#     min = num2
#     print(f'ikkinchi berilgan {num2} soni kichikroq')
# else:
#     print(f'birinchi berilgan {num} soni kichikroq')

# task 8
# num = int(input('Enter first number:'))
# num2 = int(input('Enter second number:'))

# if num > num2:
#     print(num)
#     print(num2)
# else:
#     print(num2)
#     print(num)

# task 9
# A = float(input('Enter first num:'))
# B = float(input('Enter second num:'))

# if A > B:
#     h = A
#     A = B
#     B = h
#     print(f'A = {A}')
#     print(f'A = {B}')
# else:
#     print(f'A = {A}')
#     print(f'A = {B}')

# task 10
# A = int(input('Enter first num:'))
# B = int(input('Enter second num:'))

# if A != B:
#     A = A + B
#     B = A
#     print(f'A = {A}')
#     print(f'B = {B}')
# else:
#     A = 0
#     B = 0
#     print(f'A = {A}')
#     print(f'B = {B}')

# task 11
# A = int(input('Enter first num:'))
# B = int(input('Enter second num:'))

# max = A

# if max < B:
#     max = B

# if A != B:
#     A = max
#     B = max
#     print(f'A = {A}')
#     print(f'B = {B}')
# else:
#     A = 0
#     B = 0
#     print(A)
#     print(B)

# task 12
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# min = num

# if min > num2:
#     min = num2
# if min > num3:
#     min = num3
# print(f'eng kichik son {min}')

# task 13
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# min = num
# max = num

# if min > num2:
#     min = num2
# if min > num3:
#     min = num3

# if max < num2:
#     max = num2
# if max < num3:
#     max = num3

# middle = (num + num2 + num3) - (min + max)

# print(f'berilgan 3 ta raqam ichidagi ortanchasi {middle}')

# task 14
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# min = num
# max = num

# if min > num2:
#     min = num2
# if min > num3:
#     min = num3

# if max < num2:
#     max = num2
# if max < num3:
#     max = num3

# print(f'kichigi: {min}')
# print(f'kattasi: {max}')

# task 15
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# if num + num2 > num2 + num3:
#     print(num)
#     print(num2)
# if num2 + num3 > num + num2:
#     print(num2)
#     print(num3)
# if num + num3 > num2 + num3:
#     print(num)
#     print(num3)

# task 16
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# if num < num2 and num2 < num3:
#     num*=2
#     num2*=2
#     num3*=2
#     print(num)
#     print(num2)
#     print(num3)
# else:
#     num*=-1
#     num2*=-1
#     num3*=-1
#     print(num)
#     print(num2)
#     print(num3)

# task 17
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# if num < num2 and num2 < num3 or num > num2 and num2 > num3:
#         num*=2
#         num2*=2
#         num3*=2
#         print(num)
#         print(num2)
#         print(num3)
# else:
#         num*=-1
#         num2*=-1
#         num3*=-1
#         print(num)
#         print(num2)
#         print(num3)

# task 18
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))

# if num == num2:
#     print(f'uchinchi son {num3}')
# if num == num3:
#     print(f'ikkinchi son {num2}')
# if num2 == num3:
#     print(f'birinchi son {num}')


# # task 19
# num = int(input('Enter first num:'))
# num2 = int(input('Enter second num:'))
# num3 = int(input('Enter third num:'))
# num4 = int(input('Enter fourth num:'))

# if num == num2 and num2 == num3:
#     print(f'tortinchu son {num4}')
# if num == num3 and num3 == num4:
#     print(f'ikkinchi son {num2}')
# if num2 == num3 and num3 == num4:
#     print(f'birinchi son {num}')
# if num == num2 and num4 == num :
#     print(f'uchinchi son {num3}')

# task 20
# A = int(input('Enter first num:'))
# B = int(input('Enter second num:'))
# C = int(input('Enter third num:'))

# if A + B < C + A:
#     print(f'B nuqta')
#     print(f'{A - B}')
# if A + C < C + B:
#     print(f'C nuqta')
#     print(f'{A - C}')

# task 21