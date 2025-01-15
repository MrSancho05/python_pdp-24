s = int(input("Boradigan masofangizni (km) o'lchovida kiriting: "))
myMoney = float(input("Pulingiz miqdorini kiriting (so'm): "))
busCount  = int(input("Nechta avtobus orqali manzilga yetib bormoqchisiz? ")) 
payForKm = float(input("1 Km uchun to'lov: "))
payForBus = float(input("1 ta Avtobus uchun to'lov: "))

kmPay = payForKm * s
busPay = payForBus * busCount

print(f"Mashinada yetib bora olasiz {kmPay <= myMoney} va sizda {myMoney - kmPay}00 so'm qoladi (agar minusda javob bo'lsa shuncha so'm yetmaydi)")
print(f"Avtobusda yetib bora olasiz {busPay <= myMoney} va sizda {myMoney - busPay}00 so'm qoladi (agar minusda javob bo'lsa shuncha so'm yetmaydi)")


# if byTaxi & byBus :
#     print("Iltimos berilgan xizmatlardan faqat 1 tasini tanlang!")
#     byTaxi = int(input("Manzilga taxi orqali yetib bormoqchimisiz (0 | 1)? "))
#     byBus = int(input("Manzilga avtobus orqali yetib bormoqchimisiz (0 | 1)? ")) 
# elif not byTaxi and not byBus :
#     print("Manzilga piyoda yetib borishni istayabsiz shakilli, oq yo'l:)")

# if byBus :
#     busCount  = int(input("Nechta avtobus orqali manzilga yetib bormoqchisiz? ")) 


# print(f"{s} {myMoney} {bool(byTaxi)} {bool(byBus)}")