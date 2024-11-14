# task 1
# x = [15, 2, 3, 4, 5, 3]

# kichik = x[0]
# check = True
# for i in range(0, len(x) - 1):
#     print(x[i], end=", ")
#     if x[i] > x[i + 1]:
#         check = False

# print(check)

# TASK 2
# num = int(input('Enter number: '))
# sanoq = 0
# i = 1
# while i <= num:
#     if num % i == 0:
#         sanoq += 1
#     i += 1
# if sanoq == 2: print(True)
# else: print(False)

# for i in range(1, num + 1):
#     print(i)
#     if num % i == 0:
#         sanoq += 1
# if sanoq == 2: print(True)
# else: print(False)


# t = input('Enter text: ')
# t2 = ''
# for i in t:
#     print(i)
#     t2 = i + t2
# if t == t2 : print(True)
# else: print(False)

# soz = input('Soz: ')

# soz = soz.lower()
# palidrom = True
# uzunli = len(soz)

# for i in range(uzunli // 2):
#     if soz[i] != soz[uzunli - 1 - i]:
#         palidrom = False
# print(palidrom)


x = [15, 2, 3, 5, 3]
uzunlik = len(x)
yangi = []
for i in range(uzunlik // 2):
    yangi.append(x[i] + x[uzunlik - 1 - i])
    # if uzunlik % 2 != 0: yangi.append(x[uzunlik - 1 - i])
print(yangi)
