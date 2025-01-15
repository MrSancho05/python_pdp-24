# Bahrombekov Sanjarbek Otabek og'li 24-205
from colorama import Fore, Style
mainMenu = ["Yangi kontakt qo'shish", "Kontaktni yangilash", "Kontaktni o'chirish", "Kontaktni qidirish", "Barcha kontaktlarni ko'rsatish", "Chiqish"]

contacts = [
    {'name': 'Abdulloh', 
    'number': '1604460',
    'email': 'exaple@mail.com',
    'adress': 'Tashkent',
    },
    {'name': 'Ali', 
    'number': '1404450',
    'email': 'exaple2@mail.com',
    'adress': 'Samarkand',
    },
    {'name': 'Vali', 
    'number': '5801582',
    'email': 'exaple3@mail.com',
    'adress': 'Andijan',
    }
]

# def showMainMenu():
#     print(f"\n{Fore.BLUE}{Style.BRIGHT}Asosiy menyu 📞{Style.RESET_ALL}")
#     for i in range(len(mainMenu)):
#         print(f"{Style.BRIGHT}{i+1}. {mainMenu[i]}{Style.RESET_ALL}")
#     a = input(f"\n{Fore.BLUE}{Style.BRIGHT}Tanlovingiz: {Style.RESET_ALL}")
#     if a == '1':
#         addContact()
#     elif a == '2':
#         updateContact()
#     elif a == '3':
#         deleteContact()
#     elif a == '4':
#         searchContact()
#     elif a == '5':
#         contactInfo()
#     elif a == '6':
#         print(f'{Style.BRIGHT}{Fore.GREEN}Dasturdan muvaffaqiyatli chiqildi ✅{Style.RESET_ALL}')
#         exit()
#     else:
#         print('Noto\'g\'ri tanlov qildingiz qaytatdan kiriting 🤦‍♂️')
#         showMainMenu()

def showMainMenu():
    print(f"Asosiy menu")
    for i in range(len(mainMenu)):
        print(f"{i+1}. {mainMenu[i]}")
    a = input('Tanlov :')
    if a == '1':
        addContact()
    elif a == '2':
        updateContact()
    elif a == '3':
        deleteContact()
    elif a == '4':
        searchContact()
    elif a == '5':
        contactInfo()
    elif a == '6':
        print('Poka!')
        exit()
    else:
        print("Error(")
        showMainMenu()

# def addContact():
#     global contacts
#     dic = {}
#     print(f"\n{Fore.CYAN}{Style.BRIGHT}Yangi kontakt qo'shish bo'limi ➕{Style.RESET_ALL}")
#     name = input('Kontaktni ismi: ')
#     number = input('Telefon raqami: ')
#     email = input('Emaili: ')
#     adress = input('Manzili: ')
#     dic['name'] = name
#     dic['number'] = number
#     dic['email'] = email + "@mail.com"
#     dic['adress'] = adress
#     contacts.append(dic)
#     print(f"\n{Fore.GREEN}{Style.BRIGHT}Kontakt muvaffaqiyatli qo'shildi {name} ✅{Style.RESET_ALL}")
#     showMainMenu()

def addContact():
    print('Kontaktlarni qo\'shish bo\'limi')
    name = input('name: ')
    number = input('number: ')
    emauil = input('email: ')
    adress = input('adress: ')
    dic = {
        'name': name,
        'number': number,
        'email': emauil,
        'adress': adress
    }
    contacts.append(dic)
    print('SUCCESS!')
    showMainMenu()

# def updateContact():
#     if len(contacts) != 0:
#         print(f"{Fore.CYAN}{Style.BRIGHT}Kontaktlarni yangilash bo'limi 📝{Style.RESET_ALL}")
#         uContact = input(f"{Style.BRIGHT}Yangilash uchun kontakt ismini | telefon raqamini kiriting: {Style.RESET_ALL}")
#         nLst = []
#         for i in range(len(contacts)):
#             if uContact.lower() in contacts[i]['name'].lower() or uContact in contacts[i]['number']:
#                 nLst.append(contacts[i])
#         if len(nLst) > 0:
#             print(f"\n{Fore.GREEN}{Style.BRIGHT}So'rov bo'yucha {len(nLst)} ta kontakt topildi:{Style.RESET_ALL}")
#             for i in range(len(nLst)):
#                 print(f"{Style.BRIGHT}{i + 1} chi kontakt ma'lumotlari: {nLst[i]}{Style.RESET_ALL}" )
#             a = int(input(f"\n{Style.BRIGHT}Yangilash uchun kontakt tartib raqamini kiriting: {Style.RESET_ALL}"))
#             if a <= len(nLst):
#                 newName = input('kontaktning yangi ismi: ')
#                 newNumber = input('yangi telefon raqami: ')
#                 newEmail = input('yangi emaili: ')
#                 newAdress = input('yangi manzili: ')
#                 contacts.remove(nLst[a-1])
#                 dic = {}
#                 dic['name'] = newName
#                 dic['number'] = newNumber
#                 dic['email'] = newEmail + '@mail.com'
#                 dic['adress'] = newAdress
#                 contacts.append(dic)
#                 print(f"\n{Fore.GREEN}{Style.BRIGHT}Kontakt muvaffaqiyatli yangilandi ✅{Style.RESET_ALL}")
#                 a = input(f"\n{Fore.BLUE}{Style.BRIGHT}Orqaga qaytish uchun 1 ni bosing: {Style.RESET_ALL}")
#                 if a == '1':
#                     showMainMenu()
#                 else:
#                     print('Noto\'g\'ri tanlov qildingiz qaytatdan kriting 🤦‍♂️')
#                     updateContact()
#             else :
#                 print(f"{Fore.RED}{Style.BRIGHT}Noto\'g\'ri tanlov qildingiz qaytatdan kriting 🤦‍♂️{Style.RESET_ALL}")
#                 updateContact()
#         else:
#             print(f"{Fore.RED}{Style.BRIGHT}Hech qanday kontakt topilmadi qaytadan kriting!{Style.RESET_ALL}")
#             updateContact()
#     else:
#         print(f"\n{Fore.RED}{Style.BRIGHT}Hozircha hech qanday kontaktlar mavjud emas!{Style.RESET_ALL}")
#     showMainMenu()

def updateContact():
    print('Yangilash bo\'limi')
    if len(contacts) != 0:
        nLst = []
        uContact = input('name | number: ')
        for i in range(len(contacts)):
            if uContact.lower() in contacts[i]['name'].lower() or uContact in contacts[i]['number']:
                nLst.append(contacts[i])
        if len(nLst) > 0:
            print(f"{len(nLst)} ta kontakt topildi!")
            for i in range(len(nLst)):
                print(f"{i+1} chi kontakt ma'lumotlari: {nLst[i]}")
            a = int(input('Tanlov: '))
            if a <= len(nLst):
                nName = input('Ynagi ismi: ')
                nNumber = input('Yangi raqami: ')
                nEmail = input('Yangi emaili: ')
                nAdress = input('Yangi manzili: ')
                nLst[a-1]['name'] = nName
                nLst[a-1]['number'] = nNumber
                nLst[a-1]['email'] = nEmail
                nLst[a-1]['adress'] = nAdress
                # contacts.remove(nLst[a-1])
                # dic = {
                #     'name': nName,
                #     'number': nNumber,
                #     'email': nEmail,
                #     'adress': nAdress
                # }
                # contacts.append(dic)
                print('SUCCESS UPDATE!')
            else:
                print('Error')
                updateContact()
        a = input('qaytish uchun 1: ')
        if a == '1':
            showMainMenu()
        else: 
            print('Error')
            updateContact()
    else:
        print('no contacts!')


def deleteContact():
    print(f"{Fore.CYAN}{Style.BRIGHT}Kontaktlarni o'chirish bo'limi 🪓{Style.RESET_ALL}")
    if len(contacts) != 0:
        uContact = input(f"{Style.BRIGHT}O'chirish uchun kontakt ismini | telefon raqamini kiriting: {Style.RESET_ALL}")
        nLst = []
        for i in range(len(contacts)):
            if uContact.lower() in contacts[i]['name'].lower() or uContact in contacts[i]['number']:
                nLst.append(contacts[i])
        if len(nLst) > 0:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}So'rov bo'yucha {len(nLst)} ta kontakt topildi:{Style.RESET_ALL}")
            for i in range(len(nLst)):
                print(f"{Style.BRIGHT}{i + 1} chi kontakt ma'lumotlari: {nLst[i]}{Style.RESET_ALL}" )
            a = int(input(f"\n{Style.BRIGHT}O'chirish uchun kontakt tartib raqamini kiriting: {Style.RESET_ALL}"))
            if a <= len(nLst):
                contacts.remove(nLst[a-1])
                print(f"\n{Fore.GREEN}{Style.BRIGHT}{nLst[a-1]['name']} kontakti muvaffaqiyatli chopildi 🪓{Style.RESET_ALL}")
                a = input(f"\n{Fore.BLUE}{Style.BRIGHT}Orqaga qaytish uchun 1 ni bosing: {Style.RESET_ALL}")
                if a == '1':
                    showMainMenu()
                else:
                    print('Noto\'g\'ri tanlov qilindi qaytatdan kriting!')
                    deleteContact()
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Noto\'g\'ri tanlov qilindi qaytatdan kriting!{Style.RESET_ALL}")
                deleteContact()
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}Hozircha hech qanday kontaktlar mavjud emas!{Style.RESET_ALL}")
    showMainMenu()

def searchContact():
    if len(contacts) != 0:
        print(f"{Fore.CYAN}{Style.BRIGHT}Kontaktlarni qidirish bo'limi 🔍{Style.RESET_ALL}")
        uContact = input(f"{Style.BRIGHT}Qidirilayotgan kontakt ismini | telefon raqamini kiriting: {Style.RESET_ALL}")
        nLst = []
        for i in range(len(contacts)):
            if uContact.lower() in contacts[i]['name'].lower() or uContact in contacts[i]['number']:
                nLst.append(contacts[i])
        if len(nLst) > 0:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}So'rov bo'yucha {len(nLst)} ta kontakt topildi:{Style.RESET_ALL}")
            for i in range(len(nLst)):
                print(f"{Style.BRIGHT}{i + 1} chi kontakt ma'lumotlari: {nLst[i]}{Style.RESET_ALL}" )
            a = input(f"\n{Fore.BLUE}{Style.BRIGHT}Orqaga qaytish uchun 1 ni bosing: {Style.RESET_ALL}")
            if a == '1':
                showMainMenu()
            else:
                print('Noto\'g\'ri tanlov qilindi qaytatdan kriting!')
                searchContact()
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Hech qanday kontakt topilmadi qaytadan kriting!{Style.RESET_ALL}")
            searchContact()
    else:
        print(f"\n{Fore.RED}{Style.BRIGHT}Hozircha hech qanday kontaktlar mavjud emas!{Style.RESET_ALL}")
    showMainMenu()

def contactInfo():
    if len(contacts) == 0:
        print(f"\n{Fore.RED}{Style.BRIGHT}Hozircha hech qanday kontaktlar mavjud emas!{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}{Style.BRIGHT}Kontaktingizda {len(contacts)} ta kontakt mavjud:{Style.RESET_ALL}")
    for i in range(len(contacts)):
        print(f"\n{Style.BRIGHT}{i+1} chi kontakt ma'lumotlari:{Style.RESET_ALL}" )
        for j in contacts[i].items():
            print(f"{j[0]}: {j[1]}")
    a = input(f"\n{Fore.BLUE}{Style.BRIGHT}Orqaga qaytish uchun 1 ni bosing: {Style.RESET_ALL}")
    if a == '1':
        showMainMenu()
    else:
        print('Noto\'g\'ri tanlov qilindi qaytatdan kriting!')
        contactInfo()
    
    
showMainMenu()
