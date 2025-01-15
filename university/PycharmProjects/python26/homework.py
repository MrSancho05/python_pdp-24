# 1
# def modul(son):
#     if son >= 0:
#         return son
#     else:
#         return -son

# natija = int(input("son kiriting: "))

# moduli = modul(natija)

# print(moduli)   

# 2
# def RaqamlikkaTekshir(satr):
#     return satr.isdigit()

# natija = input("son kiriting: ")

# tekshirish = RaqamlikkaTekshir(natija)
# print(tekshirish)  

# #2
# def RaqamlikkaTekshir(satr):
#     for belgi in satr:
#         if belgi.isdigit():
#             return True
#     return False

# natija = input("son kiriting: ")

# tekshirish = RaqamlikkaTekshir(natija)

# print(tekshirish)

# 3
# def findNumber(satr):
#     raqamlar = ''
#     for char in satr:
#         if char.isdigit():
#             raqamlar += char
#     return raqamlar

# satr = input("satr kiriting=> ")

# natija = findNumber(satr)

# print(natija)

# 4
# def findKattaHarf(satr):
#     for harf in satr:
#         if harf.isupper():
#             return True
#     return False

# satr = "bu yerda katta harf bor"
# print(findKattaHarf(satr))  

# 5
# def kattaHarf(satr):
#     katta_harflar = [harf for harf in satr if harf.isupper()]
#     return katta_harflar

# satr = "Bu Satrda Katta Harf Bor"
# print(kattaHarf(satr)) 

# 6
# def belgilikkaTekshir(satr, belgi):
#     belgi_mavjud = [harf for harf in satr if harf == belgi]
#     return belgi_mavjud

# satr = "Bu Satrda Belgi Q Bor"
# belgi = 'Q'
# print(belgilikkaTekshir(satr, belgi))  

# 7
# def yigindi(a, b):
#     return sum(range(a, b+1))

# a = 1
# b = 5
# print(yigindi(a, b))  

# 8
# def teskariSatr(satr):
#     print(satr[::-1])

# satr = "Python"
# teskariSatr(satr) 

# 9
# def o'rtaArifmetik(N):
#     sonlar = [int(input(f"{i+1}-sonni kiriting: ")) for i in range(N)]
#     o'rta_arifmetik = sum(sonlar) / N
#     return o'rta_arifmetik

# N = 3
# print(o'rtaArifmetik(N)) 

# 10
# def yosh(a, b):
#     yosh = b - a
#     return yosh

# a = 1980
# b = 2024
# print(yosh(a, b)) 

# 11
# def sekundlar(N):
#     sekund = N * 60
#     print(f"{N} minutning {sekund} sekundligi")

# N = 5
# sekundlar(N)

# 12
# def engKattaRaqam(N):
#     return max(str(N))

# N = 874593
# print(engKattaRaqam(N))  

# 13
# def engKichikRaqam(N):
#     return min(str(N))

# N = 874593
# print(engKichikRaqam(N))  

# 14
# def unliXarflar(satr):
#     unli_harflar = 'aeiouAEIOU'
#     unli_soni = sum(1 for harf in satr if harf in unli_harflar)
#     return unli_soni

# satr = "Bu Satrda Nechta Unli Harf Borligi Tekshirilishi Kerak"
# print(unliXarflar(satr))  

# 15
# def konvertMetr(N):
#     mertlar = ['mm', 'cm', 'dm', 'm', 'km']
#     faktorlar = [1000, 100, 10, 1, 0.001]
#     birlik = mertlar[faktorlar.index(1)]
    
#     for mert, faktor in zip(mertlar, faktorlar):
#         qiymat = N * faktor
#         print(f"{qiymat} {mert} = {N} {birlik}")

# N = 5
# konvertMetr(N)

# 16
# def qidirish(satr, belgi):
#     if belgi in satr:
#         print("Siz qidirgan belgi bor")
#     else:
#         print("Siz qidirgan belgi yo'q")

# satr = "Bu Satrda Belgi Q Bor"
# belgi = 'Q'
# qidirish(satr, belgi)

# 17
# def ASCCI_kod(satr, belgi):
#     if belgi in satr:
#         kod = ord(belgi)
#         print(f"{belgi} belgisining ASCCI kodi: {kod}")
#     else:
#         print(-1)

# satr = input('satr kiriting: ')
# belgi = input('belgi kiriting: ')
# ASCCI_kod(satr, belgi)


# HOMEWORKS

# FunSimple21
def SumRange(A, B):
    if A > B:
        return 0
    return sum(range(A, B + 1))

# FunSimple22
def Calc(A, B, Op):
    if Op == 1:
        return A + B
    elif Op == 2:
        return A - B
    elif Op == 3:
        return A * B
    elif Op == 4:
        if B != 0:
            return A / B
        return "Error: Division by Zero"
    return "Invalid Operation"

# FunSimple23
def Quarter(X, Y):
    if X > 0 and Y > 0:
        return 1
    elif X < 0 and Y > 0:
        return 2
    elif X < 0 and Y < 0:
        return 3
    elif X > 0 and Y < 0:
        return 4
    return 0  # On axis

# FunSimple24
def Even(K):
    return K % 2 == 0

# FunSimple25
def IsSquare(K):
    from math import sqrt
    root = int(sqrt(K))
    return root * root == K

# FunSimple26
def IsPower5(K):
    while K > 1:
        if K % 5 != 0:
            return False
        K //= 5
    return K == 1

# FunSimple27
def IsPowerN(K, N):
    while K > 1:
        if K % N != 0:
            return False
        K //= N
    return K == 1

# FunSimple28
def IsPrime(N):
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

# FunSimple29
def DigitCount(K):
    return len(str(K))

# FunSimple30
def DigitN(K, N):
    digits = str(K)
    if N > len(digits):
        return -1
    return int(digits[-N])

# FunSimple31
def IsPalindrome(N):
    N = str(N)
    return N == N[::-1]

# FunSimple32
from math import pi
def DegToRad(D):
    return D * pi / 180

# FunSimple33
def RadToDeg(R):
    return R * 180 / pi

# FunSimple34
def Fact(N):
    from math import factorial
    return factorial(N)

# FunSimple35
def Fact2(N):
    product = 1
    for i in range(N, 0, -2):
        product *= i
    return product

# FunSimple36
def Fib(N):
    a, b = 0, 1
    for _ in range(N):
        a, b = b, a + b
    return a

# FunSimple37
def Power1(A, B):
    return A ** B

# FunSimple38
def Power2(A, N):
    result = 1
    if N > 0:
        for _ in range(N):
            result *= A
    elif N < 0:
        for _ in range(-N):
            result /= A
    return result

# FunSimple39
def Power3(A, N):
    if N >= 0:
        return Power2(A, N)
    else:
        return Power2(1 / A, -N)

# FunSimple40
def Exp1(x, e):
    n = 0
    term = 1
    result = 0
    while abs(term) > e:
        result += term
        n += 1
        term = term * x / n
    return result

# FunSimple41
def sin1(x, e):
    term = x
    result = 0
    n = 1
    while abs(term) > e:
        result += term
        term *= -1 * x**2 / ((2*n) * (2*n+1))
        n += 1
    return result

# FunSimple42
def cos1(x, e):
    term = 1
    result = 0
    n = 0
    while abs(term) > e:
        result += term
        term *= -1 * x**2 / ((2*n+1) * (2*n+2))
        n += 1
    return result

# FunSimple43
def Ln1(x, e):
    if not (-1 < x < 1):
        return "Error: |x| must be < 1"
    term = x
    result = 0
    n = 1
    while abs(term) > e:
        result += term
        n += 1
        term = -term * x * (n-1) / n
    return result

# FunSimple44
def Arctg1(x, e):
    if not (-1 <= x <= 1):
        return "Error: |x| must be <= 1"
    term = x
    result = 0
    n = 1
    while abs(term) > e:
        result += term
        term *= -1 * x**2 * (2*n-1) / (2*n+1)
        n += 1
    return result

# FunSimple45
def Power4(x, a, e):
    term = 1
    result = 1
    n = 1
    while abs(term) > e:
        term *= (a - n + 1) * x / n
        result += term
        n += 1
    return result

# FunSimple46
def EKUB(A, B):
    while B:
        A, B = B, A % B
    return A

# FunSimple47
def Frac1(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d
    gcd = EKUB(numerator, denominator)
    return numerator // gcd, denominator // gcd

# FunSimple48
def EKUK(A, B):
    return A * B // EKUB(A, B)

# FunSimple49
def EKUB3(A, B, C):
    return EKUB(EKUB(A, B), C)

# FunSimple50
def TimeToHMS(T):
    H = T // 3600
    M = (T % 3600) // 60
    S = T % 60
    return H, M, S
