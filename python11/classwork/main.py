# color = input("Enter color: ")

# if color == "red":
#     print("Stop")
# elif color == "green":
#     print('Gazini bos!')
# elif color == "yellow":
#     print('Ready')
# else:
#     print('Nima kritvosan e!') 

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# z = int(input('Enter z: '))

# max_n = x

# if max_n < y:
#     max_n = y
# if max_n < z:
#     max_n = z

# print(f"Max : {max_n}")

# son = int(input("son:"))
# son2 = int(input("son2:"))

# if son < son2:
#     print(son2)
#     print(son)
# else: 
#     print(son)
#     print(son2)

# son = int(input("son:"))

# if son > -10 and son < 10:
#     print("1 xonali")
# if son > 9 and son < 100 or son >= -99 and son <= -10:
#     print('2 xonali')


# son = int(input('son: '))

# if son > -10 and son < 10 and son % 2 == 0:
#     print('bir xonali juft')
# else:
#     print('bir xonali toq')

# son = int(input('son: '))

# if son >= 0 and son < 10:
#     print(f'{son} - 1 xonali musbat')
# if son < 0 and son > -10:
#     print(f'{son} - 1 xonali manfiy')
# if son > 9 and son < 100:
#     print(f'{son} - 2 xonali musbat')
# if son < -9 and son > -100:
#     print(f'{son} - 2 xonali manfiy')

son = int(input('son: '))

if son < 0:
    son *= -1

b = son % 10
o = son // 10

if b < o:
    print(o, b)
else:
    print(b,o)



