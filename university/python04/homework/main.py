import math
# 1. fullName
name = input('Enter your name: ')
lastName = input('Enter your last name: ')
fullName = name + " " + lastName
print(fullName)

# 2. your name, your age
ism = input('Enter your name: ')
yosh = int(input('Enter your age: '))
print(f"Sizning ismingiz {ism}, yoshingiz {yosh}")

# 3. upper, lower, title, capitalize
matn = input('Enter something: ')
print(matn.upper())
print(matn.lower())
print(matn.title())
print(matn.capitalize())

# 4. strip
text = input('Enter text with spaces: ')
print(text.lstrip())
print(text.rstrip())
print(text.strip())

# 5. info
infoN = input('Enter your name: ')
infoA = input('Enter your age: ')
infoC = input('Enter your favorite color: ')
print(f'Salom {infoN}, Siz {infoA} yoshdasiz va sizning sevimli rangingiz {infoC}')

# 6. upeer, capitalize 
smallN = input('ismingizni kichik harflarda kiriting: ')
print(smallN.upper())
print(smallN.capitalize())

# 7.
num = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f"{num} + {num2} = {num + num2}")
print(f"{num} - {num2} = {num - num2}")
print(f"{num} * {num2} = {num * num2}")
print(f"{num} / {num2} = {num / num2}")
print(f"{num} ** {num2} = {pow(num,num2)}")

# 8. 
fnum = float(input('haqiqiy son1: '))
fnum2 = float(input('haqiqiy son2: '))
print(f'{fnum} / {fnum2} = {fnum / fnum2}')
print(f'{pow(fnum, fnum2)}')

# 9.
something = input('Enter something: ')
print(type(something))

# 10.
number = int(input('Enter number: '))
number2 = int(input('Enter number2: '))
print(f'Type int: {number} + {number2} = {number + number2}')
print(f'Type str: {str(number)} + {str(number2)} = {str(number) + str(number2)}')

# 11.
son = int(input('Enter num: '))
if son > 10:
    print(True)
else:
    print(False)

# 12.
num = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
print(f'{float(num)} + {num2} = {int(float(num) + num2)}')

# 13.
num = int(input('Enter num: '))
if num % 2 == 0 :
    print(True)
else:
    print(False) 

# 14.
height = int(input('Enter height of rectangle: '))
weight = int(input('Enter weight of rectangle: '))
print(f'S = {height * weight}')
print(f'P = {2 * (height + weight)}')

# 15.
radius = float(input('Enter radius: '))
pi = 3.14
print(f'L = {2 * pi * radius}')
print(f'S = {pi * radius * radius}')

# 16.
product = float(input('Enter price of product: '))
product2 = float(input('Enter price of product2: '))
if product > product2 :
    print('Ikkinchi mahsulot arzonroq')
else:
    print('Birinchi mahsulot arzonroq')

# 17
num = int(input('Enter num: '))
num2 = int(input('Enter num2: '))
num3 = int(input('Enter num3: '))
print(f'{num} + {num2} + {num3} / 3 = {(num + num2 + num3) / 3}')

# 18
num = int(input('Enter num:'))
print(f'{math.sqrt(num)}')

# 19
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

# 1 2 3
# 2 3 1
c = a + b + c
b = c - (a+b)
a = c - (a+b)
c = c - (a+b)

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')