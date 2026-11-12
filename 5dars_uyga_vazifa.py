#1
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3outlook.com"]
for email_manzil in pochtalar:
        if "@" not in email_manzil:
            print("Noto'g'ri email:", email_manzil)

#2
parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
maxsus = "!@#$%^&*"

for parol in parollar:
    raqam_bor = False
    maxsus_bor = False

    for belgi in parol:
        if belgi.isdigit():
            raqam_bor = True
        if belgi in maxsus:
            maxsus_bor = True

    if len(parol) < 8:
        print("Juda qisqa")
    elif raqam_bor == False and maxsus_bor == False:
        print("Kuchsiz parol")
    else:
        print("Kuchli parol")


#3
haroratlar = [20, 22, 19, 24, 25, 23, 21]

for harorat in haroratlar:
    if harorat <= 22:
        print("Salqin kun")
    else:
        print("Iliq kun")


#4
taomlar = ["Osh", "Shashlik", "Manti","Lag’mon"]
buyurtma = input("Buyurtmangizni kiriting: ")
topildi = False

for taom in taomlar:
    if buyurtma == taom:
        topildi = True

if topildi == True:
    print("Buyurtmangiz qabul qilindi")
else:
    print("Kechirasiz bunday taom yo'q")


#5
foydalanuvchilarning_yoshlari = [16 , 21, 17, 30, 25]

for yosh in foydalanuvchilarning_yoshlari:
    if yosh < 18:
        print("Yosh chegarasiga yetmagan")
    else:
        print("Xush kelibsiz")

#6
xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]

for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang")
    else:
        print("-")


#7
fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]

musiqalar = []
rasmlar = []

for fayl in fayllar:
    if fayl.find(".mp3") != -1:
        musiqalar.append(fayl)
    elif fayl.find(".jpg") != -1:
        rasmlar.append(fayl)

print("Musiqalar:", musiqalar)
print("Rasmlar:", rasmlar)
