# TASK 3
# sanoq = 0
# for i in range(-80, 81):
#     if i < 0 :
#         i *= -1
#     if i % 7 == 0:
#         sanoq += 1
# print(sanoq)

# TASK 4
# mevalar = ['olma', 'banan', 'kiwi', 'olma']
# sanoq = 0
# for meva in mevalar:
#     if meva == 'olma':
#         sanoq += 1     
# print(sanoq)

# TASK 5
# A = int(input('A:'))
# B = int(input('B:'))

# for A in range(B):
#     print(A)
#     A += 1

# TASK 6
# x = [1,2,3,4,5,6,6,7,8,9]
# sanoq = 0
# for i in x:
#     if x[i] % 2 == 0:
#         sanoq += 1
# print(sanoq)

# TASK 7
sanoq = 0
text = input('Enter text: ')

for t in text:
    print(t)
    if int(chr(t)) > 65 and int(chr(t)) < 91:
        sanoq += 1
        print(t)
print(sanoq)