# #1
# import math
#
# birinchi_son = int(input("Birinchi sonni kiriting: "))
# ikkinchi_son = int(input("Ikkinchi sonni kiriting: "))
# uchinchi_son = int(input("Uchinchi sonni kiriting: "))
#
# print("Birinchi sonning kvadrat ildizi: ", math.sqrt(birinchi_son))
# print("Ikkichi sonning kvadrat ildizi: ", math.sqrt(ikkinchi_son))
# print("Uchinchi sonning kvadrat ildizi: ", math.sqrt(uchinchi_son))

# #2
# from math import pi
#
# aylana_radiusi = float(input("Aylananing radiusini kiriting: "))
# aylana_yuzasi = pi * aylana_radiusi ** 2
# aylana_uzunligi = pi * aylana_radiusi ** 2
#
# print("Aylana yuzasi: ", round(aylana_yuzasi, 2))
# print("Aylan uzunligi: ", round(aylana_uzunligi, 2))

# #3
# import math
# sonlar = [
#     float(input("Birinchi sonni kiriting: ")),
#     float(input("Ikkinchi sonni kiriting: ")),
#     float(input("Uchinchi sonni kiriting: ")),
#     float(input("Tortinchi sonni kiriting: ")),
#     float(input("Beshinchi sonni kiriting: ")),
# ]
#
# for son in sonlar:
#     print("Ceil: ", math.ceil(son))
#     print("Floor: ", math.floor(son))
#     print("--------------")

# #4
# import math
#
# n = int(input("N natural sonni kiriting: "))
#
# yigindi = sum(math.factorial(i) for i in range(1,n+1))
#
# print("Faktoriallar yigindisi: ", yigindi)

# #5
# import math
#
# birinchi_son = int(input("Birinchi sonni kiriting: "))
# ikkinchi_son = int(input("Ikkinchi sonni kiriting: "))
# uchinchi_son = int(input("Uchinchi sonni kiriting: "))
#
# natija = math.gcd(birinchi_son, ikkinchi_son, uchinchi_son)
# print(f"{birinchi_son}, {ikkinchi_son} va {uchinchi_son} ning eng katta umumiy bo'luvchisi: {natija}")
# print("----------------------------------")
#
# print(birinchi_son // natija)
# print(ikkinchi_son // natija)
# print(uchinchi_son // natija)

# #6
# import random as r
#
# sonlar = [r.randint(1,100) for i in range(20)]
#
# juft_sonlar_soni = 0
# toq_sonlar_soni = 0
#
# for son in sonlar:
#     if son % 2 == 0:
#         juft_sonlar_soni += 1
#     else:
#         toq_sonlar_soni += 1
#
# eng_katta = max(sonlar)
# eng_kichik = min(sonlar)
#
# print("Hosil bo'lgan sonlar: ", sonlar)
# print(f"Juft sonlar soni: {juft_sonlar_soni}")
# print(f"Toq sonlar soni: {toq_sonlar_soni}")
# print(f"Eng katta son: {eng_katta}")
# print(f"Eng kichik son: {eng_kichik}")

# #7
# import random as r
# parol_uzunligi = int(input("Parol uzunligini kiriting: "))
#
# if parol_uzunligi < 3:
#     print("Parol uzunligi kamida 3 ta belgidan iborat bo'lishi kerak!")
# else:

# #8
# import random as r
#
# print("Yashirin sonni topish uchun 5 ta imkoniyatingiz bor!")
#
# yashirin_son = r.randint(1,6)
#
# for imkoniyat in range(1,50):
#     son1 = int(input(f"{imkoniyat}-urunish. Sonni kiriting: "))
#
#     if son1 == yashirin_son:
#         print("Tabriklaymiz, siz sonni topdingiz👏")
#         break
#     elif son1 > yashirin_son:
#         print("Kiritilgan son yashirin sondan katta. Kichikroq son kiriting")
#     else:
#         print("Kiritilgan son yashirin sondan kichik. Kattaroq son kiriting")
# else:
#     print(f"Afsuski imkoniyatlar tugadi. Yashirin son {yashirin_son} ga teng edi")


# #9
# import random
#
# oquvchilar = []
# for i in range(1,11):
#     ism = input(f"{i}-o'quvchining ismini kiriting: ")
#     oquvchilar.append(ism)
#
# random.shuffle(oquvchilar)
#
# guruh1 = oquvchilar[:5]
# guruh2 = oquvchilar[5:]
#
# print("1-guruh", guruh1)
# print("2-guruh", guruh2)

# #10
# import random
#
# a = random.randint(1, 10)
# print(a)
# b = random.randint(1, 10)
# print(b)

