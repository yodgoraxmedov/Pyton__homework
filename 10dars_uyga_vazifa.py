#1
sonlar = [2, 5, 8, 9, 11, 15, 18, 20, 25, 27]

uchga_bolinadigan = list(filter(lambda sonlar: sonlar%3 == 0, sonlar ))
beshga_bolinadigan = list(filter(lambda sonlar: sonlar%5 == 0, sonlar))

print(uchga_bolinadigan)
print(beshga_bolinadigan)

#2
sonlar = [-1, 2, 4, -5, -2, 8, 9, -5]

manfiy_sonlar = list(filter(lambda sonlar: sonlar < 0, sonlar ))
qolgan_sonlar = list(filter(lambda sonlar: sonlar > 0, sonlar ))
kvadratlar = list(map(lambda sonlar: sonlar**2 , qolgan_sonlar))

print(manfiy_sonlar)
print(qolgan_sonlar)
print(kvadratlar)

#3
matnlar = ["olma", "anor", "banan", "uzum", "nok", "gilos", "shaftoli", "limon", "ot", "it"]

natija = sorted(matnlar, key=lambda s: (len(s), s))
print(natija)

#4
talabalar = [
    {"ism": "Ali",    "yosh": 20, "baholar": [90, 85, 95]},
    {"ism": "Vali",   "yosh": 21, "baholar": [70, 75, 80]},
    {"ism": "Laylo",  "yosh": 19, "baholar": [88, 92, 84]},
    {"ism": "Zarina", "yosh": 20, "baholar": [100, 95, 98]},
    {"ism": "Sardor", "yosh": 22, "baholar": [60, 65, 70]},
    {"ism": "Madina", "yosh": 21, "baholar": [80, 80, 80]},
]

yuqori = list(filter(lambda t: sum(t["baholar"]) / len(t["baholar"]) > 80, talabalar))

natija = sorted(yuqori, key=lambda t: sum(t["baholar"]) / len(t["baholar"]), reverse=True)

for t in natija:
    print(["ism"], t["yosh"], round(sum(t["baholar"]) / len(t["baholar"]), 1))


#5
mahsulotlar = [
    {"nomi": "Telefon", "narxi": 400, "chegirma_foizi": 10},
    {"nomi": "PC)", "narxi": 700, "chegirma_foizi": 12},
    {"nomi": "Quloqchin", "narxi": 20, "chegirma_foizi": 5},
    {"nomi": "Klaviatura", "narxi": 22, "chegirma_foizi": 7},
    {"nomi": "Sichqoncha", "narxi": 10, "chegirma_foizi": 5},
    {"nomi": "Noutbuk", "narxi": 700, "chegirma_foizi": 11},
]

hisoblangan = list(map
   (lambda m: {
    "nomi": m["nomi"],
    "eski_narx": m["narxi"],
    "yangi_narx": m["narxi"] * (100 - m["chegirma_foizi"]) / 100,
   },
    mahsulotlar
))

natija = sorted(hisoblangan, key=lambda m: m["yangi_narx"])

for m in natija:
    print(f"{m['nomi']}: eski narxi {m['eski_narx']}, yangi narxi {m['yangi_narx']:.2f}")
