#1
harorat = int(input("Ob-havo haroratini kiriting"))
if harorat < 0:
    print("Sovuq")
elif harorat <=20:
    print("Salqin")
elif harorat <=30:
    print("Iliq")
else:
    print("Isssiq")


#2
xarid = int(input("Xarid summasini kiriting"))
if xarid < 50000:
    print("chegirma yo'q")
elif xarid <= 100000:
    print("Xarid uchun 5% chegirma")
else:
    print("Xarid uchun 10% chegirma")


#3
login = input("Logini kiriting:")
parol = input("Parolni kiriting:")
if login == "admin" and parol =="12345":
    print("Xush kelibsiz, admin")
else:
    print("login va parol xato")


#4
yosh = int(input("Yoshingizni kiriting:"))
if yosh <13:
    print("Sizga ushbu film tavfsiya etilmaydi")
elif yosh <=17:
    print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
else:
    print("Siz filmni tomosha qilishingiz mumkin")


#5
print("Menyu")
print("1-Osh")
print("2-Mastava")
print("3-Shashlik")

tanlov = int(input("Tanlovni kiriting:"))
if tanlov == 1:
    print("Osh narxi: 30000, tayyorlanish vaqti 30 daqiqa")
if tanlov == 2:
    print("Mastava narxi: 25000, tayyorlanish vaqti 27 daqiqa")
if tanlov == 3:
    print("Shashlik narxi: 15000, tayyorlanish vaqti 15 daqiqa")


#6
email = input("Email manzilingizni kiriting: ")
if email.find("@") == -1 or email.find(".") == -1:
    print("Noto'g'ri email manzili")
else:
    print("Email manzili qabul qilindi")


#7
baho = int(input("Balingizni kiriting"))

if baho < 55:
    print("2 baho")
elif baho <=69:
    print("3 baho")
elif baho <=85:
    print("4 baho")
elif baho <=90:
    print("5 baho")


#8
summa1 = int(input("Kartadagi mavjud pul:"))
summa2 = int(input("Kartadan yechmoqchi bo'lgan summa:"))

if summa2>summa1:
    print("Hisobingizda mablag' yetarli emas")
elif 5000>summa2:
    print("Minimal yechish summasi 5000 so'm")
else:
    print("Pul muvaffaqiyatli yechildi")


#9
kun = input("Hafta Kunini kiriting")

if kun == "shanba" or "yakshanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")

#10
trafik = float(input("Oyiga qancha trafik ishlatasiz (GB)"))

if trafik <1:
    print("Sizga 'Mini' tarifi mos keladi")
elif trafik <=5:
    print("Sizga 'Standart' tarifi mos keladi")
else:
    print("Sizga 'Unlimited' tarifi keladi")

