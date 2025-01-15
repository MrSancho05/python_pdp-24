#  1 - masala
#  Bola voyaga yetga yoki yetmaganligni tekshiradiga dastur tuzing
#  agar voyaga yetga bo'lsa "voyaga yetga" ask holda "voyaga yetmagan"
#  so'zini ekranga chiqaring
# ageOfChild = int(input('Enter your age: '))
# if ageOfChild < 18:
#     print('Voyaga yetmagan')
# else :
#     print('Voyaga yetgan')

#  2 - masala
#  Talaba olgan bahosini tekshiring dastur tuzing agr talaba 5 baho olgan bo'lsa
#  a'lo, agar 4 baho olgan bo'lsa yaxshi, agar 3 baho olgan bo'lsa qoniqarli
#  agar 2 baho olgan bo'lsa qoniqarsiz degan so'zlarni ekranga chiqaring

# grade = int(input('Enter your grade: '))
# if grade == 5:
#     print("a'lo")
# elif grade == 4:
#     print('yaxshi')
# elif grade == 3:
#     print('qoniqarli')
# elif grade == 2:
#     print('qoniqarsiz')
# else:
#     print('Error:(')

#  3 - masala
#  Oy raqanimi ekrandan kiritilsa shunga mos fasilni ekranga cjiqaring
#  maslana: 12, 1 yoki 2 raqam kiritilsa Qish fasili deb chiqaring

# countOfMonth = int(input('Enter count of month: '))
# if countOfMonth > 0 and countOfMonth < 3 or countOfMonth == 12:
#     print('winter')
# elif countOfMonth >= 2 and countOfMonth < 6:
#     print('spring')
# elif countOfMonth >= 5 and countOfMonth < 9:
#     print('summer')
# elif countOfMonth >= 8 and countOfMonth < 12:
#     print('autumn')
# else :
#     print('wrong input(')

#  4 - masala
#  Havoning harorati haqiqiy sonda kiritilsa unga mos holda 30 dan katta bo'lsa
#  "havo issiq", agar 30 < 20 > 15 "havo iliq" aks holda 15 dan kichik bolsa "havo sovuq"
#  kabi so'zlarni chiqaring

# airTemperature = float(input('Enter temprature: '))
# if airTemperature > 30:
#     print('havo issiq')
# elif airTemperature <= 30 and airTemperature >= 15:
#     print('havo iliq')
# else:
#     print('havo sovuq')

#  5 - masala
# Hujjatning amal qilish muddati kiritiladi butun sonda agar hujjat amal qilish muddati
# 5 kundan o'tib ketgagn bo'lsa "hujjat amal qilish muddati tugadi" aks holda "hujjat amal qilish muddati tugagan" kabi so'zlarni chiqaring

# documentValidityPeriod = int(input('Enter document validity: '))
# if documentValidityPeriod > 5:
#     print('hujjat amal qilish muddati tugadi')
# elif documentValidityPeriod > 0 and documentValidityPeriod <= 5:
#     print('hujjat amal qilish muddati tugamagan')
# else:
#     print('wrong input:/')

# 6 - masala
# To'lov usuli matn sharkida kiritiladi naqt yoki kartada agar naqt deb kiritilsa
# summa kiritishni so'raydi agar karta deb kiritilsa parol kiriing deb so'rasin

# paymentMethod = input('Enter payment method [naqt | karta]:')
# if paymentMethod == "naqt":
#     summa = int(input('Summani kiriting: '))
#     print('Tolovingiz uchun tashakkur')
# elif paymentMethod == "karta":
#     password = int(input('Parolni kiriting: '))
#     print('Tolovingiz uchun tashakkur')
# else:
#     print('wrong input:/')

# 7 - masala
# Baho baholash: Foydalanuvchidan bahoni so'rang va 90 dan yuqori bo'lsa "A", 80-89 "B", 70-79 "C", 60-69 "D", 60 dan past bo'lsa "F" deb chiqarish.

# grade = int(input('Enter your grade: '))

# if grade > 90:
#     print('A')
# elif grade >= 80 and grade <= 90:
#     print('B')
# elif grade >= 70 and grade <= 79:
#     print('C')
# elif grade >= 60 and grade <= 69:
#     print('D')
# elif grade < 60:
#     print('F')
# else :
#     print('wrong input:/')

# 8 - masala
# Yoshni tekshirish: Foydalanuvchining yoshini so'rang va agar 18 dan katta bo'lsa "Kattalar", aks holda "Bolalar" deb chiqarish.

# age = int(input('age: '))

# if age > 18:
#     print('Kattalar')
# else:
#     print('Bolalar')


# 9 - masala
# Kiyinish qoidalari: Foydalanuvchidan ob-havo haqida so'rab, agar yomg'ir yoki qor bo'lsa, "Ko'ylak kiyma" deb chiqarish.

# clotheForWeather = input('Enter weather type: ')
# if clotheForWeather == "qor" or clotheForWeather == "yomg'ir":
#     print("Ko'ylak kiyma")
# else:
#     print("Ko'ylak kiyvur")


# 10 - masala
# To'lov turini tanlash: Foydalanuvchidan to'lov turini (naqd, kartochka) so'rab, har biriga alohida xabar berish.

# paymentMethod2 = input('Payment method [naqt | karta]: ')
# if paymentMethod2 == "naqt":
#     print('Naqti asal')
# elif paymentMethod2 == "karta":
#     print('bu ham qolishmaydi naqtdan)')
# else:
#     print("nima qilib bolsa ham to'laysan")

# 11 - masala
# Sertifikat olish: Foydalanuvchi 70% dan yuqori baho olsa, "Sertifikat olishingiz mumkin" deb chiqarish.

# percentage = int(input('Enter your percentage: '))
# if percentage > 70:
#     print('Sertifikat olishingiz mumkin')
# else:
#     print('Sertifikat olishingiz mumkin emas')


# 12 - masala
# Yil faslini aniqlash: Foydalanuvchidan oy raqamini so'rang va yil faslini aniqlash (qish, bahor, yoz, kuz).

# monthNum = int(input('Enter month number:'))
# if monthNum > 0 and monthNum < 3 or monthNum == 12:
#     print('qish')
# elif monthNum > 2 and monthNum < 6:
#     print('bahor')
# elif monthNum > 5 and monthNum < 9:
#     print('yoz')
# elif monthNum > 8 and monthNum < 12:
#     print('kuz')
# else:
#     print('error(')

# 13 - masala
# Umumiy o'quv natijasi: Foydalanuvchidan 3 ta bahoni olib, ularning o'rtacha qiymatini hisoblang va "Yaxshi", "O'rtacha", "Yomon" deb baholang.

# fNum = int(input('Enter your first grade: '))
# sNum = int(input('Enter your second grade: '))
# thNum = int(input('Enter your third grade: '))

# fGrade = (fNum + sNum + thNum) / 3

# if fGrade > 4:
#     print('Yaxshi')
# elif fGrade == 4 :
#     print("O'rtacha")
# elif fGrade < 4:
#     print('Yomon')

# 14 - masala
# Qaror qabul qilish: Foydalanuvchiga xohlagan taomni tanlasa, "Tayyorlashga kirishamiz" deb chiqarish.

# palov = "osh"
# suyuq = "shorva"
# fastFood = "lavash"

# userChoice = input(f"Quyidagilardan birini tanlang {palov}, {suyuq}, {fastFood}: ")

# if userChoice == palov or userChoice == fastFood or userChoice == suyuq:
#     print('Tayyorlashga kirishamiz')
# else:
#     print('error(')

# 15 - masala
# Avtomobil yoshi: Foydalanuvchidan avtomobilning yoshi va yurgan masofasini so'rang va agar yoshi 10 dan katta bo'lsa, "Ehtiyot qismlarni tekshiring" deb chiqarish.

# carAge = int(input('Enter car age: '))
# if carAge > 10:
#     print('Ehtiyot qismlarni tekshiring')
# else:
    # print('molodoy avtomobil')

# 16- masala
# Sovg'a tanlash: Foydalanuvchidan yoshi va jinsi (erkak/ayol) so'ralib, unga mos sovg'a tavsiya etish.

# gender = input('Enter your gender [erkak | ayol]: ')
# if gender == "erkak":
#     print('Paypoq')
# elif gender == "ayol":
#     print('Bakal')
# else:
#     print("Senga sovg'a yo'q")

# 17 - masala
# Reyting tizimi: Agar foydalanuvchining balini 100 dan yuqori bo'lsa, "Reytingni yangilang" deb chiqarish.

# userRating = int(input('Enter your rating: '))
# if userRating > 100:
#     print('Reytingni yangilang')
# else:
#     print("O'zing bilasan")

# 18 - masala
# Vaqtni tekshirish: Foydalanuvchidan vaqtni so'rang va agar tun bo'lsa "Xayrli tun", kunduzi bo'lsa "Xayrli kun" deb chiqarish.

# time = input('Enter time now [tun | kun]: ')
# if time == 'kun':
#     print('Xayrli kun')
# elif time == 'tun':
#     print('Xayrli tun')
# else:
#     print('Good bye!')

# 19 - masala
# Parol kuchini tekshirish: Foydalanuvchidan parolni so'rang va agar u 8 ta belgidan kam bo'lsa, "Parolni kuchaytiring" deb chiqarish.

# password = input('Enter password: ')
# if len(password) < 8:
#     print('parolni kuchaytiring')
# else:
#     print('Welcome!')

# 20 - masala
# Kredit tayyorgarligi: Foydalanuvchining daromadi va qarzini so'rab, agar daromadi qarzidan yuqori bo'lsa "Kredit olish mumkin" deb chiqarish.

# income = int(input('Enter your income: '))
# debt = int(input('Enter your debt: '))

# userWallet = income - debt

# if userWallet > 0:
#     print('Kredit olish mumkin')
# else:
#     print("O'zi shuncha qarzing bor!")


# 21 - masala
# Sport turini tanlash: Foydalanuvchidan yoshini so'rab, unga mos sport turini tavsiya etish.

# userAge = int(input('Enter your age: '))
# if userAge > 0 and userAge <= 16:
#     print("futbol bilan shug'ullaning")
# elif userAge > 16 and userAge <= 30:
#     print("kurash bilan shug'ullaning")
# elif userAge > 30 and userAge <= 60:
#     print("badan tarbiya bilan shug'ullaning")
# elif userAge > 60:
#     print("tinchkina uyizda o'tiraqoling")
# else:
#     print('error/:')

# 22 - masala
# Sog'liqni tekshirish: Foydalanuvchidan vazn va bo'yini so'rab, BMI ni hisoblang va sog'liq holatini baholang.

# weight = int(input('Enter your weight: '))
# height = float(input('Enter your height: '))

# BMI = weight / (height * height)

# if BMI > 0 and BMI < 18.5:
#     print("Ozg'in")
# elif BMI >= 18.5 and BMI <= 24.9:
#     print('Normal vazn')
# elif BMI > 24.9 and BMI <= 29.9:
#     print('ortiqcha vazn')
# elif BMI > 30:
#     print('Semizlik')
# else :
#     print('error:/')  
# print(BMI)

# 23 - masala
# Yozgi ta'til rejalari: Foydalanuvchidan yozgi ta'til rejalarini so'rab, agar rejasi bo'lsa "Yozda sayohatga chiqamiz" deb chiqarish.

# userPlans = input("yozgi ta'til rejalaring bormi [ha | yo'q]:? ")

# if userPlans == 'ha':
#     print('Yozda sayohatga chiqamiz')
# elif userPlans == "yo'q":
#     print('Yozda sayohatga chiqmaymiz(')
# else:
#     print('error:/')

# 24 - masala
# Bajarilgan ishlar: Foydalanuvchidan bajarilgan ishlar sonini so'rab, agar 5 tadan ko'p bo'lsa "Yaxshi natija" deb chiqarish.

# actionCount = int(input('Qancha isni bitirdingiz: '))
# if actionCount > 5:
#     print('Yaxshi natija')
# else:
#     print('yomon natija')

# 25 - masala
# Mashhur kitoblar: Foydalanuvchidan kitob nomini so'rab, agar bu kitob mashhur bo'lsa "Buni o'qiganman" deb chiqarish.

# famousBooks = ["Qoran", "Sahih al-Bukhari", "Sahih Muslim"]

# book = input('Enter book name: ')

# if book == famousBooks[0] or book == famousBooks[1] or book == famousBooks[2]:
#     print("Buni o'qiganman")
# else:
#     print("Insha Alloh o'qiyman")


# 26 - masala
# Futbol jamoasini tanlash: Foydalanuvchidan sevimli futbol jamoasini so'rab, agar jamoa yutgan bo'lsa "Tabriklaymiz!" deb chiqarish.

# footballClub = input('Enter your club name: ')

# if footballClub != '':
#     print('Tabriklaymiz!')
# else :
#     print('error/:')

# 27 - masala
# Savdo muvozanati: Foydalanuvchidan xarajat va daromadni so'rab, agar xarajat daromaddan past bo'lsa "Foyda" deb chiqarish.

# daromad = float(input('Daromadingiz?: '))
# xarajat = float(input('Xarajatingiz?: '))

# if daromad - xarajat > 0:
#     print('Foyda')
# else:
#     print('Bankrot')

# 28 - masala
# Ish qidirish: Foydalanuvchidan ish tajribasini so'rab, agar 2 yildan kam bo'lsa "Yosh mutaxassis" deb chiqarish.

# workExperience = int(input('Enter your work experience: '))

# if workExperience > 0 and workExperience < 2:
#     print('Yosh mutaxassis')
# else:
#     print("Pro | don't know")

# 29 - masala
# Ishni baholash: Foydalanuvchidan ish natijasini so'rab, "Qoniqarli", "Yaxshi", "Mukammal" deb baholash.

# full = "ohirgacha"
# average = 'normal'
# notFull = "ohirgacha emas"
# workGrade = input(f'Ishingizni qanchalik yaxshi bitirdingiz [{full}, {average}, {notFull}]?: ')

# if workGrade == full:
#     print('Mukammal')
# elif workGrade == average:
#     print('Yaxshi')
# elif workGrade == notFull:
#     print('Qoniqarli')
# else:
#     print('nimasi bu?')

# 30- masala
# Bojxona qoidalari: Foydalanuvchidan xorijdan olib kelgan mahsulotni so'rab, agar qiymati 100$ dan yuqori bo'lsa, "Boj to'lashingiz kerak" deb chiqarish.

# productPrice = int(input('Product necha dollar?: '))
# if productPrice > 100:
#     print("Boj to'lashingiz kerak")

# 31- masala
# Uchuvchi talablari: Foydalanuvchidan uchish uchun yoshi va vaznini so'rab, agar talablarga mos kelmasa "Uchish mumkin emas" deb chiqarish.

# age = int(input('your age: '))
# weight = int(input('your weight: '))

# if not age > 18 or not weight > 50:
#     print('uchush mumkin emas')

# 32- masala
# Iqlim sharoiti: Foydalanuvchidan haroratni so'rab, agar 0 dan past bo'lsa "Qishda qizish" deb chiqarish.

# temprature = int(input('Enter temprature: '))
# if temprature < 0:
#     print('Qishda qizish')

# 33- masala
# Maktabga tayyorgarlik: Foydalanuvchidan maktabga kirishi uchun tayyorgarlik darajasini so'rab, agar yetarli bo'lmasa "Ko'proq o'qish kerak" deb chiqarish.

# readyToSchool = input("maktabga tayyormisiz [ha | yo'q]: ")

# if readyToSchool == "yo'q":
#     print("Ko'proq o'qish kerak")
# else :
#     print('malades')

# 34- masala
# Savdo so'rovlarini tekshirish: Foydalanuvchidan so'rovlarni so'rab, agar talab yuqori bo'lsa "Savdo muvaffaqiyatli" deb chiqarish.

# request = int(input("So'rovlar miqdori: "))

# if request > 50:
#     print('Savdo muvaffaqiyatli')
# else :
#     print("Bo'midi")

# 35- masala
# Dars tayyorgarligi: Foydalanuvchidan dars tayyorgarligi darajasini so'rab, agar yetarli bo'lmasa "Boshqa darslar oling" deb chiqarish.

# readyToLesson = input('Darsga tayyormisiz [no | yes]?: ')

# if readyToLesson == 'yes':
#     print('malades')
# elif readyToLesson == 'no':
#     print('Boshqa darslar oling')
# else:
#     print('halades')

# 36- masala
# Dostlar ro'yxati: Foydalanuvchidan dostlar sonini so'rab, agar 5 tadan kam bo'lsa "Dostlar orttirishingiz mumkin" deb chiqarish.

# friendsCount = int(input('How many friends do you have? '))
# if friendsCount < 5:
#     print('Dostlar orttirishingiz mumkin')
# else :
#     print('Bravo')

# 37- masala
# Musbat yoki Manfiy Son: Foydalanuvchi kiritgan son musbat yoki manfiy ekanligini aniqlang. Agar nol kiritilsa, “Bu nol” deb yozing.

# number = int(input('Enter number: '))
# if number == 0:
#     print('Bu nol')
# elif number > 0:
#     print('Musbat')
# else:
#     print('Manfiy')

# 38- masala
# Juft yoki Toq Son: Foydalanuvchidan son kiritishni so'rang va bu son juft yoki toq ekanligini aniqlang.

# number = int(input('Enter number: '))

# if number % 2 == 0:
#     print('Juft')
# else :
#     print('toq')

# 39- masala
# Yoshni Guruhlash: Foydalanuvchidan yoshini so'rang va u 0-12 yosh bolalar, 13-19 yoshlar va 20 dan katta kattalar guruhiga kirishini aniqlang.

# age = int(input('Enter your age: '))
# if age > 0 and age <= 12:
#     print('bolalar')
# elif age > 12 and age <= 19:
#     print('yoshlar')
# elif age >= 20 :
#     print('Kattalar')
# else:
    # print('error:/')

# 40- masala
# Bahoni Tekshirish: Foydalanuvchidan bahoni so'rang va bahoni A, B, C, D yoki F ga to'g'ri kelishini aniqlang.

# grade = int(input('Enter grade: '))

# if grade >= 90:
#     print('A')
# elif grade >= 80 and grade < 90:
#     print('B')
# elif grade >= 70 and grade < 80:
#     print('C')
# elif grade >= 60 and grade <= 70:
#     print('D')
# else:
#     print('F')

# 41- masala
# Mavsumni Aniqlash: Foydalanuvchidan oy raqamini so'rang va bu oy qishda, bahorda, yozda yoki kuzda ekanligini aniqlang.

# month = int(input('Enter month num: '))
# if month > 0 and month < 3 or month == 12:
#     print('winter')
# elif month > 2 and month < 6:
#     print('spring')
# elif month > 5 and month < 9:
#     print('summer')
# elif month > 8 and month < 12:
#     print('autumn')
# else:
#     print('error:/')

# 42- masala
# Ikki Sonni Taqqoslash: Foydalanuvchidan ikkita sonni so'rang va ularni qaysi biri katta, kichik yoki tengligini aniqlang.

# fnum = int(input('Enter first number: '))
# snum = int(input('Enter second number: '))

# if fnum > snum:
#     print('first number')
# elif fnum < snum:
#     print('second number')
# else: 
#     print('this numbers are equal')

# 43- masala
# Parolni Tekshirish: Foydalanuvchidan parolni so'rang va parol to'g'ri yoki noto'g'ri ekanligini aniqlang.

# correctPassword = "Sancho05"

# password = input('Enter password: ')
# if password == correctPassword:
#     print('correct')
# else :
#     print('wrong')

# 44- masala
# Harfning Turini Aniqlash: Foydalanuvchidan bir harfni so'rang va bu katta yoki kichik harf ekanligini aniqlang.

# latter = input('Enter lower | upper latter: ')

# if latter.isupper():
#     print('katta harf')
# elif latter.islower():
#     print('Kichik harf')
# else :
#     print('Bu kiritilgan belgilar harf emas')

# 45- masala
# Havo Haroratini Aniqlash: Foydalanuvchidan havo haroratini so'rang va u juda issiq, iliq, sovuq yoki juda sovuq ekanligini aniqlang.

# temprature = int(input('Havo harorati: '))
# if temprature < 15:
#     print('sovuq')
# elif temprature >= 15 and temprature < 30:
#     print('iliq')
# elif temprature >= 30 and temprature <= 50:
#     print('issiq')
# else:
#     print('harorat juda katta kiritilgan')



# 46- masala
# Mamlakatni Aniqlash: Foydalanuvchidan mamlakatini so'rang va agar u O'zbekiston bo'lsa, “Siz O'zbekistondasiz” deb yozing.

# country = input('Enter your country: ')
# if country == "O'zbekiston":
#     print("Siz O'zbekistondansiz")
# else:
#     print(f'{country}dansiz')

# 47- masala
# Balandlikni Aniqlash: Foydalanuvchidan balandligini so'rang va u qisqa, o'rtacha yoki baland ekanligini aniqlang.

# height = float(input('Balandligingizni sm kiriting: '))
# if height < 150:
#     print("Siz qisqa bo'ysiz")
# elif 150 <= height <= 180:
#     print("Siz o'rtacha bo'ysiz")
# else:
#     print("Siz baland bo'ysiz")

# 48- masala
# Kitob Narxini Tekshirish: Foydalanuvchidan kitob narxini so'rang va narxni arzon, o'rtacha yoki qimmat ekanligini aniqlang.

# price = float(input('Kitob narxini kiriting:'))

# if price < 50:
#     print('arzon kitob')
# elif 50 <= price <= 100:
#     print("o'rtacha narxga ega kitob")
# else:
#     print('Bu qimmat kitob')



# 49- masala
# Sport Darajasini Aniqlash: Foydalanuvchidan sport darajasini so'rang va u yangi, o'rta yoki tajribali sportchi ekanligini aniqlang.


# 50- masala
# Sog'liqni Tekshirish: Foydalanuvchidan belgilari haqida ma'lumot oling va sog'liq holatini aniqlang (masalan, isitma, yo'tal).


# 51- masala
# Kreditni Tasdiqlash: Foydalanuvchidan kredit balini so'rang va u kredit olish uchun mos kelishini aniqlang.


# 52- masala
# Kafedagi Buyurtma: Foydalanuvchidan kafeda buyurtma (kofe, choy, sharbat) so'rang va buyurtma tayyorlanishini xabar bering.


# 53- masala
# Tezlikni Aniqlash: Foydalanuvchidan avtomobil tezligini so'rang va u tezlikni oshirdimi yoki normal ekanligini aniqlang.

# 54- masala
# Tatilni Aniqlash: Foydalanuvchidan ta'til vaqtini so'rang va yoz yoki qish ta'tili ekanligini aniqlang.


# 55- masala
# Maktab Bahosi: Foydalanuvchidan maktab bahosini so'rang va u yuqori, o'rtacha yoki past baho ekanligini aniqlang.


# 56- masala
# Raqamni Aniqlash: Foydalanuvchidan raqam kiritishni so'rang va kiritilgan qiymat raqam ekanligini aniqlang.
