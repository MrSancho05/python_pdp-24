# global va local o'zgaruvchilar
# global
# x = 23
# global o'zgaruvchilar esa hech qanda function yoki class tegishli bo'lmaydi 
# biror class yoki function ichida yaratilgan o'zgaruvchilar local o'zgaruvchilar deyiladi

# def korsat():
#     # local
#     x = 13
#     print(x)

# korsat()
# print(x)


# def PesonInfo(name, bYear, cYear):
#     global ism
#     ism = name
#     return cYear - bYear

# shaxs = PesonInfo('Ali', 1991, 2024)
# print(shaxs, ism)

# parol = "1234"
# Balanc = 10000000

# tillarMenu = ['Uzbekcha', 'Ruscha', 'Inglizcha']

# menuAsosiy = ["Balansni tekshirish", "Naqd pul olish", "To'lovlar", "SMS", "Parol o'zgartirish"]

# menuPulYechish = ["50 ming", "100 ming", "150 ming", "200 ming", "300 ming", "400 ming", "Boshqa summa", "Orqaga"]

# menuTolovlar = ["Komunal", "Soliqlar", "Jarima", "Mobile", "Internet"]

# menuKredit = ["Kredit raqami"]

# menuMobile = ["Uzmobile", "Beeline", "Usell", "UMS", "Perfectum", "Orqaga"]

# menuParol = ["Yangi parolni kiritish", "Orqaga"]

# menuSMS = ["SMS xabarni o'chirish", "SMS xabarni yoqish", "Orqaga"]

# menuKomunal = ["Gaz", "Svet", "Suv", "Issiq suv", "Chiqindi"]


# parolTekshir = lambda parolInput: True if parol == parolInput else False


# def menuKorsat(menu):
#     count = 1
#     for i in menu:
#         print(f"{count}.{i}")
#         count += 1
#     print()

# balancTekshir = lambda balanc: True if Balanc > balanc else False



# def pulYechish(summa, matn):
#     while True:
#         if balancTekshir(summa):
#             global Balanc
#             Balanc -= summa
#             print(f"Siz {summa} {matn}")
#             break
#         else:
#             print(f"Sizda mablag' yetarli emas : {balancKorsat()}")
#             summa = float(inputValue("Boshqa summa"))



# def inputValue(value):
#     x = input(f"{value} kiriting: ")
#     return x

# def balancKorsat():
#     print(f"Sizning hisobingizda {Balanc} so'm bor")
#     return Balanc


# def tanlovSummaInput(index):
#     summa = float(inputValue("Summa"))
#     pulYechish(summa, f"{menuKomunal[index]} ga to'lov qildingiz")


# def tanlovKomunal(tanlov):
#     if tanlov == "1":
#         menuKorsat(menuKomunal)
#         tanlov = inputValue("Tanlov")
#         if tanlov == "1":
#             tanlovSummaInput(0)
#         elif tanlov == "2":
#             tanlovSummaInput(1)
#         elif tanlov == "3":
#             tanlovSummaInput(2)
#         elif tanlov == "4":
#             tanlovSummaInput(3)
#         elif tanlov == "5":
#             tanlovSummaInput(4)


# def start():
#     limit = 3
#     while True:
#         p = inputValue("Parol")
#         limit = limit - 1
#         if parolTekshir(p):
#             print("Xush kelibsiz...\n")
#             menuKorsat(menuAsosiy)
#             tanlov = inputValue("Tanlov")
#             if tanlov == "1":
#                 balancKorsat()
#             elif tanlov == "2":
#                 menuKorsat(menuPulYechish)
#                 tanlovInp = inputValue("Tanlov")
#                 if tanlovInp == "1":
#                     summa = float(inputValue("Summa"))
#                     pulYechish(summa, f"{menuPulYechish[0]} som pul yechib olindi")
#             elif tanlov == "3":
#                 menuKorsat(menuTolovlar)
#                 tanlov = inputValue("Tanlov")
#                 tanlovKomunal(tanlov)


#         else:
#             if limit == 0:
#                 print("Sizda limit tugadi!!! ")
#                 break
#             else:
#                 print(f"Parol xato {limit}")




# start()



# O'zgaruvchilar
balans = 1000000
parol = "1234"
tillarMenu = ['Uzbekcha', 'Ruscha', 'Inglizcha']

menuAsosiy = ["Balansni tekshirish", "Naqd pul olish", "Naqd pul qo'shish", "To'lovlar", "SMS", "Parol o'zgartirish", "Dasturdan chiqish"]

menuPulYechish = ["50 ming", "100 ming", "150 ming", "200 ming", "300 ming", "400 ming", "Boshqa summa", "Orqaga"]

menuTolovlar = ["Komunal", "Soliqlar", "Jarima", "Mobile", "Internet", "Orqaga"]

menuKredit = ["Kredit raqami", "Orqaga"]

menuMobile = ["Uzmobile", "Beeline", "Usell", "UMS", "Perfectum", "Orqaga"]

menuParol = ["Yangi parolni kiritish", "Orqaga"]

menuSMS = ["SMS xabarni o'chirish", "SMS xabarni yoqish", "Orqaga"]

menuKomunal = ["Gaz", "Svet", "Suv", "Issiq suv", "Chiqindi", "Orqaga"]

# PIN kodni tekshirish
def kirish():
    limit = 3
    while limit > 0:
        inpParol = input("PIN kodni kiriting: ")
        if inpParol == parol:
            print("Kirish muvaffaqiyatli!\n")
            return True
        else:
            limit -= 1
            print(f"Noto'g'ri PIN! Qolgan limitlar: {limit}")
    print("Karta bloklandi!")
    return False

# Balansni ko'rsatish
def balansni_tekshir():
    print(f"Sizning hisobingizdagi mablag': {balans} so'm\n")

# Pul yechish funksiyasi
def pul_yechish():
    global balans
    summa = int(input("Qancha pul yechmoqchisiz? "))
    if summa > balans:
        print("Xatolik: Hisobda yetarli mablag' yo'q!\n")
    elif summa <= 0:
        print("Xatolik: Summani to'g'ri kiriting!\n")
    else:
        balans -= summa
        print(f"{summa} so'm yechildi. Qolgan balans: {balans} so'm\n")

def jarima_tolash():
    global balans
    summa = int(input("Jarimaga qancha pul to'lamoqchisiz? "))
    if summa > balans:
        print("Xatolik: Hisobda yetarli mablag' yo'q!\n")
    elif summa <= 0:
        print("Xatolik: Summani to'g'ri kiriting!\n")
    else:
        balans -= summa
        print(f"{summa} so'm yechildi. Qolgan balans: {balans} so'm\n")

# Pul qo'shish funksiyasi
def pul_qoshish():
    global balans
    summa = int(input("Qancha pul qo'shmoqchisiz? "))
    if summa <= 0:
        print("Xatolik: Summani to'g'ri kiriting!\n")
    else:
        balans += summa
        print(f"{summa} so'm qo'shildi. Yangi balans: {balans} so'm\n")

def menuKorsat(menu):
    count = 1
    for i in menu:
        print(f'{count}. {i}')
        count += 1
    print()

def tolov(summa, matn):
    summa = int(f'{matn} qancha tolov qilmoqchisiz? ')
    global balans
    balans -= summa
# Asosiy menyu
def menyu():
    while True:
        menuKorsat(menuAsosiy)
        tanlov = input("Tanlovingizni kiriting: ")

        if tanlov == "1":
            balansni_tekshir()

        elif tanlov == "2":
            pul_yechish()

        elif tanlov == "3":
            pul_qoshish()

        elif tanlov == "4":
            menuKorsat(menuTolovlar)
            tanlov = input("Tanlovingizni kiriting: ")

            if tanlov == "1":
                print("Ko'munal tolovlar")
                menuKorsat(menuKomunal)
                tanlov = input("Tanlovingizni kiriting: ")
                if tanlov == '1':
                    summa = int(input('Gazga qancha tolov qilmoqchisiz? '))
                    tolov(summa, )

            elif tanlov == "2":
                print('Soliqlar')
                # menuKorsat(menuSoliqlar)
            elif tanlov == '3':
                print('Jarimalar')
                jarima_tolash()
            elif tanlov == '4':
                print("Mobile aloqa uchun to'lov")
                menuKorsat(menuMobile)

            elif tanlov == '5':
                print("Internetga to'lov")
            elif tanlov == '6':
                print()
                print('Asosiy menyu:')
                menyu()

        elif tanlov == "7":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Xatolik: Noto'g'ri tanlov. Qaytadan urinib ko'ring!\n")

# Dastur boshlanishi
if kirish():
    menyu()
