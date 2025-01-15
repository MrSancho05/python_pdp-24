# def getNums(text):
#     b = ''
#     for i in text:
#         if '0' <= i <= '9':
#             # print(i)
#             b += i
#     return b
# a = input('Enter text: ')
# print(getNums(a))

# ####################################
# 2
# def maxElement(lst):
#     s = lst[0]
#     # for i in lst:
#     #     if s < i:
#     #         s = i
#     i = 0
#     while i < range():
#         print(i)
#         if s < i:
#             s = i
#         i += 1
#     return s
lst = [1,5,15,52,1,91,3]
# print(maxElement(lst))

# def reverceUz(lst):
#     rLst = []
#     s = len(lst) - 1
#     while s >= 0:
#         rLst.append(lst[s])
#         s -= 1

#     # for i in range(len(lst) -1,-1,-1):
#     #     rLst.append(lst[i])
#     return rLst

# print(reverceUz(lst))


oylik = int(input('Oylik: '))

def daromadS(oylik):
    s = 0
    if 1_000_000 <= oylik <= 5_000_000:
        s =  oylik
    elif 5_000_000 < oylik <= 10_000_000:
        s = oylik * (3.5 / 100)
    elif 11_000_000 < oylik <= 15_000_000:
        s = oylik * (7.5 / 100)
    elif 15_000_000 < oylik <= 20_000_000:
        s = oylik * (12 / 100)
    elif oylik > 20_000_000:
        s = oylik * (17 / 100)
    return s

def toliqDaromad(oylik):
    return oylik - daromadS(oylik)
print(daromadS(oylik))
print(toliqDaromad(oylik))
