# num = int(input('Enter number: '))
# qoldiq = ''

# while num >= 1:
#     qoldiq = str(num % 2) + qoldiq
#     num //= 2
# print(qoldiq)

num = int(input('num: '))
summa = ''
while num >= 1:
    qoldiq = num % 16
    if qoldiq > 9:
        qoldiq += 55
        qoldiq = chr(qoldiq)
    summa = str(qoldiq) + summa
    num //= 16
print(summa)

