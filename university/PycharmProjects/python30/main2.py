mainMenu = ['Yangi kontakt add', 'Update Con', 'Delete Con', 'Search Con', 'Show All Con', 'Exit']
contacts = [
    {'name': 'Ali', 'number': '1234567', 'email': 'example@mail.com', 'adress': 'Toshkent'},
    {'name': 'Vali', 'number': '1781516', 'email': 'example2@mail.com', 'adress': 'Andijan'},
    {'name': 'Komil', 'number': '1604467', 'email': 'example2@mail.com', 'adress': 'Andijan'},
]
def showMainMenu():
    for i in range(len(mainMenu)):
        print(f'{i+1}. {mainMenu[i]}')
    a = input('Tanla: ')
    if a == '1':
        addCon()
    elif a == '2':
        updateCon()
    elif a == '3':
        delCon()
    elif a == '4':
        seachCon()
    elif a == '5':
        showCon()
    elif a == '6':
        exit()
    else:
        print('Wrong input!!!')
        showMainMenu()


def addCon():
    print('Add contact section!')
    name = input('name: ')
    number = input('number: ')
    email = input('email: ')
    adress = input('adress: ')
    contacts.append({'name': name, 'number': number, 'email': email, 'adress': adress})
    print('Contact added successfully!')
    showMainMenu()

def updateCon():
    print('Update contact section!')
    if len(contacts) > 0:
        nLst = []
        uContact = input('Contact name | number: ')
        for i in range(len(contacts)):
            if uContact.lower() in contacts[i]['name'].lower() or uContact in contacts[i]['number']:
                nLst.append(contacts[i])
        if len(nLst) > 0:
            print(f"Founded contacts: {len(nLst)}")
            for i in range(len(nLst)):
                print(f"{i+1}. Con info: {nLst[i]}")
            a = input('Tanla: ')
            if int(a) <= len(nLst):
                nLst[int(a) - 1]['name'] = input('new name:')
                nLst[int(a) - 1]['number'] = input('new number: ')
                nLst[int(a) - 1]['email'] = input('new email: ')
                nLst[int(a) - 1]['adress'] = input('new adress: ')
                print('Contact updated successfully!')
                showMainMenu()
        else: 
            print('Contact not found!')
            updateCon()
    else: 
        print('Contacts not found!')
        showMainMenu()

def delCon():
    print('Delete contact section!')
    if len(contacts) > 0:
        nLst = []
        dContact = input('Contact name | number: ')
        for i in range(len(contacts)):
            if dContact.lower() in contacts[i]['name'].lower() or dContact in contacts[i]['number']:
                nLst.append(contacts[i])
        if len(nLst) > 0:
            print(f"Founded contacts: {len(nLst)}")
            for i in range(len(nLst)):
                print(f"{i+1}. Con info: {nLst[i]}")
            a = input('Tanla: ')
            if int(a) <= len(nLst):
                contacts.remove(nLst[int(a) - 1])
                print('Contact deleted successfully!')
                showMainMenu()
        else: 
            print('Contact not found!')
            delCon()
    else: 
        print('Contacts not found!')
        showMainMenu()

def showCon():
    print('Show all contacts section!')
    if len(contacts) > 0:
        print(f'Contacts count: {len(contacts)}')
        for i in range(len(contacts)):
            print(f"{i+1}. Con info: ")
            for j in contacts[i].items():
                print(f'{j[0]}: {j[1]}')
            print()
        showMainMenu()
    else:
        print('Contacts not found!')
        showMainMenu()

showMainMenu()