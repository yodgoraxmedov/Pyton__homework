# #2
# dokon = {
#     'Kiyim': [
#         {'nom': "Ko'ylak", 'narx': 20, 'ombor': 50, 'sotilgan': 80},
#         {'nom': 'Shim',    'narx': 35, 'ombor': 4,  'sotilgan': 60},
#     ],
#     'Elektronika': [
#         {'nom': 'Telefon',   'narx': 300, 'ombor': 12, 'sotilgan': 40},
#         {'nom': 'Quloqchin', 'narx': 25,  'ombor': 3,  'sotilgan': 120},
#     ],
#     'Oziq-ovqat': [
#         {'nom': 'Choy', 'narx': 5, 'ombor': 100, 'sotilgan': 300},
#     ],
# }
#
# #barcha kategoriyadagi mahsulotlar
# print("Barcha maxsulotlar: ")
# for kategoriya, mahsulotlar in dokon.items():
#     print(kategoriya)
#     for m in mahsulotlar:
#         print(" ", m['nom'], m['narx'], "$")
#
# print()
# print("-------------------------------------")


# #omborda 5 tadan kam mahsuloti qolgan mahsulotlar
# print("Omborda 5 tadan kam qolgan mahsulotlar")
# for kategoriya, mahsulotlar in dokon.items():
#     for m in mahsulotlar:
#         if m['ombor'] < 5:
#             print(" ", m['nom'], "-", m['ombor'], "ta qoldi")
#
# print()
# print("-------------------------------------")
#
#
# #har bir mahsulotdan qancha daromad olingani
# print("Har bir mahsulotdan qancha daromad olingan")
# for kategoriya, mahsulotlar in dokon.items():
#     for m in mahsulotlar:
#         daromad = m['sotilgan'] * m['narx']
#         print(" ", m['nom'], "-", daromad, "$")
#
# print()
# print("-------------------------------------")
#
#
# #Eng ko‘p sotilgan mahsulotni
# print("Eng ko'p sotilgan mahsulot:")
# eng_nom = ''
# eng_soni = 0
# for kategoriya, mahsulotlar in dokon.items():
#     for m in mahsulotlar:
#         if m['sotilgan'] > eng_soni:
#             eng_soni = m['sotilgan']
#             eng_nom = m['nom']
# print("  ", eng_nom, "-", eng_soni, "ta sotilgan")
#
# print()
# print("-------------------------------------")
#
#
# #har bir kategoriya bo‘yicha umumiy daromad
# print(" Kategoriya bo'yicha umumiy daromad:")
# for kategoriya, mahsulotlar in dokon.items():
#     jami = 0
#     for m in mahsulotlar:
#         jami = jami + m['narx'] * m['sotilgan']
#     print("  ", kategoriya, "-", jami, "$")
#
#     print()
# print("-------------------------------------")
# print("-------------------------------------")
#
#
#
#
# #3
# kutubxona = {
#     'Roman': [
#         {'nom': "O'tkan kunlar", 'muallif': 'Abdulla Qodiriy', 'yil': 1925, 'umumiy': 10, 'ijarada': 4},
#         {'nom': 'Sariq devni minib', 'muallif': 'Xudoyberdi Toshbolatov', 'yil': 1980, 'umumiy': 8, 'ijarada': 8},
#     ],
#     'Fantastika': [
#         {'nom': 'Garri Potter', 'muallif': 'J. Rouling', 'yil': 2001, 'umumiy': 6, 'ijarada': 5},
#         {'nom': 'Dune', 'muallif': 'F. Gerbert', 'yil': 1965, 'umumiy': 5, 'ijarada': 1},
#     ],
#     'Ilmiy': [
#         {'nom': 'Qisqa tarix', 'muallif': 'S. Xoking', 'yil': 2010, 'umumiy': 7, 'ijarada': 2},
#     ],
# }
#
# #Barcha kitoblarni janrlar bo'yicha chiqarish
# print("Barcha kitoblar:")
# for janr, kitoblar in kutubxona.items():
#     print(janr)
#     for k in kitoblar:
#         print("  ", k['nom'], "-", k['muallif'], ",", k['yil'])
#
# #Hozirda mavjud kitoblar soni (umumiy - ijarada)
# print("Hozirda mavjud kitoblar soni:")
# mavjud = 0
# for janr, kitoblar in kutubxona.items():
#     for k in kitoblar:
#         mavjud = mavjud + (k['umumiy'] - k['ijarada'])
# print("  ", mavjud, "ta")
#
# #2000-yildan keyin nashr etilgan kitoblar
# print("2000-yildan keyin nashr etilganlar:")
# for janr, kitoblar in kutubxona.items():
#     for k in kitoblar:
#         if k['yil'] > 2000:
#             print("  ", k['nom'], "-", k['yil'])
#
# #Eng ko'p ijaraga berilgan kitob
# print("Eng ko'p ijaraga berilgan kitob:")
# eng_nom = ''
# eng_soni = 0
# for janr, kitoblar in kutubxona.items():
#     for k in kitoblar:
#         if k['ijarada'] > eng_soni:
#             eng_soni = k['ijarada']
#             eng_nom = k['nom']
# print("  ", eng_nom, "-", eng_soni, "ta ijarada")
#
# #Har bir janr bo'yicha jami mavjud nusxalar
# print("Janr bo'yicha mavjud nusxalar:")
# for janr, kitoblar in kutubxona.items():
#     jami = 0
#     for k in kitoblar:
#         jami = jami + (k['umumiy'] - k['ijarada'])
#     print("  ", janr, "-", jami, "ta")
#
#
# print()
# print("-------------------------------------")
# print("-------------------------------------")

#1
universitet = {
    'Komyuter inginiringi':[
        {'nom': '913-24', 'talaba_ismi': 'Ali', 'talaba_yoshi': 20, 'talabaning_baholar': (4,5,5,4,5)},
        {'nom': '912-24', 'talaba_ismi': 'Vali', 'talaba_yoshi': 19, 'talabaning_baholar': (5,5,3,4,4)},
        {'nom': '911-24', 'talaba_ismi': 'Karim', 'talaba_yoshi': 20, 'talabaning_baholar': (3,5,3,5,5)},
        ],

    'Axborot xavfsizligi':[
        {'nom': '511', 'talaba_ismi': 'Sarvar', 'talaba_yoshi': 20, 'talabaning_baholar': (4,3,4,4,5)},
        {'nom': '512', 'talaba_ismi': 'Sardor', 'talaba_yoshi': 21, 'talabaning_baholar': (5,5,4,5,5)},
        {'nom': '511', 'talaba_ismi': 'Doston', 'talaba_yoshi': 20, 'talabaning_baholar': (4,3,4,5,5)},
        ],
    'Dasturiy inginiringi':[
        {'nom': '711', 'talaba_ismi': 'Qahramon', 'talaba_yoshi': 20, 'talabaning_baholar': (3,3,4,5,5)},
        {'nom': '712', 'talaba_ismi': 'Siroj', 'talaba_yoshi': 23, 'talabaning_baholar': (4,5,5,4,4)},
        {'nom': '713', 'talaba_ismi': 'Jamshid', 'talaba_yoshi': 21, 'talabaning_baholar': (4,5,4,3,5)},
        ],
}

#Barcha fakultet, guruh va talabalarni ekranga chiqaring.
print("Barcha fakultet, guruh va talabalarni chiqarish.")
for fakultet, talabalar in universitet.items():
    print("Fakultet:", fakultet)
    for t in talabalar:
        print("   Guruh:", t['nom'],
              "| Talaba:", t['talaba_ismi'],
              "| Yoshi:", t['talaba_yoshi'],
              "| Baholari:", t['talabaning_baholar'])

print()
print('---------------------------------------------------------')

#Har bir talabaning o‘rtacha bahosini hisoblang.
print("Har bir talabaning o‘rtacha bahosi.")
for fakultet, talabalar in universitet.items():
    print("Fakultet:", fakultet)
    for t in talabalar:
        baholar = t['talabaning_baholar']
        ortacha = sum(baholar)/len(baholar)
        print(f"  {t['talaba_ismi']} - {ortacha:.2f}")


print()
print('---------------------------------------------------------')


#O‘rtacha bahosi 4.5 dan yuqori talabalarni aniqlang.
print("O‘rtacha bahosi 4.5 dan yuqori talabalar.")
for fakultet, talabalar in universitet.items():
    print("Fakultet:", fakultet)
    for t in talabalar:
        baholar = t['talabaning_baholar']
        ortacha = sum(baholar)/len(baholar)
        if ortacha > 4.5:
            print(" ", t['talaba_ismi'], "-", ortacha, "| Fakultet:", fakultet, "| Guruh:", t['nom'])

print()
print('---------------------------------------------------------')


#Eng yuqori o‘rtacha bahoga ega talabani toping.
eng_yuqori = 0
eng_yaxshi_talaba = " "

for fakultet, talabalar in universitet.items():
    print("Fakultet:", fakultet)
    for t in talabalar:
        baholar = t['talabaning_baholar']
        ortacha = sum(baholar)/len(baholar)
        if ortacha > eng_yuqori:
            eng_yuqori = ortacha
            eng_yaxshi_talaba = t['talaba_ismi']
print("Eng yaxshi o'rtacha bahoga ega talaba:", eng_yaxshi_talaba, "-", eng_yuqori)


print()
print('---------------------------------------------------------')

#Har bir guruhdagi talabalar sonini hisoblang.
print("Har bir guruhdagi talabalar soni")
guruhlar_soni = {}
for fakultet, talabalar in universitet.items():
    print("Fakultet:", fakultet)
    for t in talabalar:
        guruh = t['nom']
        if guruh in guruhlar_soni:
            guruhlar_soni[guruh] = guruhlar_soni[guruh] + 1
        else:
            guruhlar_soni[guruh] = 1

for guruh, soni in guruhlar_soni.items():
    print("  Guruh:", guruh, "- talabalar soni:", soni)


print()
print('---------------------------------------------------------')
print('---------------------------------------------------------')

#4
maktab = {
    '11-sinf': [
        {'ism': 'Asror', 'baholar': {'Matematika': 5, 'Informatika': 4, 'Fizika': 5}},
        {'ism': 'Axror', 'baholar': {'Matematika': 4, 'Informatika': 4, 'Fizika': 3}},
    ],
    '10-sinf': [
        {'ism': 'Kamron', 'baholar': {'Matematika': 5, 'Informatika': 5, 'Fizika': 5}},
        {'ism': 'Sarvar', 'baholar': {'Matematika': 4, 'Informatika': 3, 'Fizika': 4}},
    ],
    '9-sinf': [
        {'ism': 'Laziz', 'baholar': {'Matematika': 4, 'Informatika': 4, 'Fizika': 5}},
        {'ism': 'Dilshod', 'baholar': {'Matematika': 3, 'Informatika': 4, 'Fizika': 4}},
    ],
}

#Har bir sinfdagi o'quvchilarni va ularning baholarini chiqaring.
print("1. Har bir sinfdagi o'quvchilar va baholari:")
for sinf, oquvchilar in maktab.items():
    print("Sinf:", sinf)
    for o in oquvchilar:
        print("   ", o['ism'], "-", o['baholar'])

print()
print('---------------------------------------------------------')

#Har bir o'quvchining o'rtacha bahosini hisoblang.
print("\n2. Har bir o'quvchining o'rtacha bahosi:")
for sinf, oquvchilar in maktab.items():
    for o in oquvchilar:
        baholar = list(o['baholar'].values())
        ortacha = sum(baholar) / len(baholar)
        print("   ", o['ism'], "-", ortacha)

print()
print('---------------------------------------------------------')

#Barcha fanlardan 4 yoki undan yuqori baho olgan o'quvchilarni aniqlang.
print("Barcha fanlardan 4 va undan yuqori baho olganlar:")
for sinf, oquvchilar in maktab.items():
    for o in oquvchilar:
        hammasi_4_dan_yuqori = True
        for fan, baho in o['baholar'].items():
            if baho < 4:
                hammasi_4_dan_yuqori = False
        if hammasi_4_dan_yuqori:
            print("   ", o['ism'], "-", sinf)

print()
print('---------------------------------------------------------')

#Har bir sinfning umumiy o'rtacha natijasini hisoblang.
print("Har bir sinfning umumiy o'rtachasi:")
sinf_ortachalari = {}
for sinf, oquvchilar in maktab.items():
    yigindi = 0
    soni = 0
    for o in oquvchilar:
        for fan, baho in o['baholar'].items():
            yigindi = yigindi + baho
            soni = soni + 1
    sinf_ortachalari[sinf] = yigindi / soni
    print("   ", sinf, "-", sinf_ortachalari[sinf])

print()
print('---------------------------------------------------------')

#Eng yaxshi natija ko'rsatgan sinfni aniqlang.
print("Eng yaxshi sinf:")
eng_yuqori = 0
eng_yaxshi_sinf = ""
for sinf, ortacha in sinf_ortachalari.items():
    if ortacha > eng_yuqori:
        eng_yuqori = ortacha
        eng_yaxshi_sinf = sinf
print("   ", eng_yaxshi_sinf, "-", eng_yuqori)

print()
print('---------------------------------------------------------')

#Har bir fan bo'yicha eng yuqori baho olgan o'quvchini toping.
print("Har bir fan bo'yicha eng yuqori baho olgan o'quvchi:")
fan_eng_yuqori = {}
fan_oquvchi = {}
for sinf, oquvchilar in maktab.items():
    for o in oquvchilar:
        for fan, baho in o['baholar'].items():
            if fan not in fan_eng_yuqori or baho > fan_eng_yuqori[fan]:
                fan_eng_yuqori[fan] = baho
                fan_oquvchi[fan] = o['ism']
for fan in fan_eng_yuqori:
    print("   ", fan, "-", fan_oquvchi[fan], "-", fan_eng_yuqori[fan])


print()
print('---------------------------------------------------------')
print('---------------------------------------------------------')

#5
hotel = {
    '1-qavat': [
        {'raqam': 101, 'turi': 'Standart', 'narxi': 300000, 'holati': 'band', 'mijoz': 'Ali'},
        {'raqam': 102, 'turi': 'Standart', 'narxi': 300000, 'holati': 'bosh', 'mijoz': None},
        {'raqam': 103, 'turi': 'Lyuks', 'narxi': 600000, 'holati': 'band', 'mijoz': 'Vali'},
    ],
    '2-qavat': [
        {'raqam': 201, 'turi': 'Standart', 'narxi': 300000, 'holati': 'band', 'mijoz': 'Karim'},
        {'raqam': 202, 'turi': 'Lyuks', 'narxi': 600000, 'holati': 'bosh', 'mijoz': None},
        {'raqam': 203, 'turi': 'Prezident', 'narxi': 1200000, 'holati': 'band', 'mijoz': 'Sardor'},
    ],
    '3-qavat': [
        {'raqam': 301, 'turi': 'Lyuks', 'narxi': 600000, 'holati': 'band', 'mijoz': 'Doston'},
        {'raqam': 302, 'turi': 'Prezident', 'narxi': 1200000, 'holati': 'bosh', 'mijoz': None},
        {'raqam': 303, 'turi': 'Standart', 'narxi': 300000, 'holati': 'bosh', 'mijoz': None},
    ],
}

# Barcha qavatlar va xonalarni ekranga chiqaring.
print("1. Barcha qavatlar va xonalar:")
for qavat, xonalar in hotel.items():
    print("Qavat:", qavat)
    for x in xonalar:
        print("   Xona:", x['raqam'], "| Turi:", x['turi'],
              "| Narxi:", x['narxi'], "| Holati:", x['holati'],
              "| Mijoz:", x['mijoz'])

print()
print('---------------------------------------------------------')

#Bo'sh xonalarni aniqlang.
print("\n2. Bo'sh xonalar:")
for qavat, xonalar in hotel.items():
    for x in xonalar:
        if x['holati'] == 'bosh':
            print("   ", x['raqam'], "-", x['turi'], "-", qavat)

print()
print('---------------------------------------------------------')

#Har bir qavatdagi band xonalar sonini hisoblang.
print("\n3. Har bir qavatdagi band xonalar soni:")
for qavat, xonalar in hotel.items():
    band_soni = 0
    for x in xonalar:
        if x['holati'] == 'band':
            band_soni = band_soni + 1
    print("   ", qavat, "-", band_soni)

print()
print('---------------------------------------------------------')
#Xona turi bo'yicha umumiy daromadni hisoblang.
print("\n4. Xona turi bo'yicha umumiy daromad:")
daromad = {}
for qavat, xonalar in hotel.items():
    for x in xonalar:
        if x['holati'] == 'band':
            tur = x['turi']
            if tur in daromad:
                daromad[tur] = daromad[tur] + x['narxi']
            else:
                daromad[tur] = x['narxi']
for tur, summa in daromad.items():
    print("   ", tur, "-", summa)

print()
print('---------------------------------------------------------')

#Eng qimmat xonani aniqlang.
print("\n5. Eng qimmat xona:")
eng_qimmat = 0
eng_qimmat_xona = None
for qavat, xonalar in hotel.items():
    for x in xonalar:
        if x['narxi'] > eng_qimmat:
            eng_qimmat = x['narxi']
            eng_qimmat_xona = x
print("   Xona:", eng_qimmat_xona['raqam'], "| Turi:", eng_qimmat_xona['turi'],
      "| Narxi:", eng_qimmat)

