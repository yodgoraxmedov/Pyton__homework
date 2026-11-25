#1
with open("matn.txt", "r") as kirish_fayli:
    matn = kirish_fayli.read()

sozlar = matn.split()

with open("natija.txt", "w") as chiqish_fayli:
    for soz in sozlar:
        if len(soz) > 5:
            chiqish_fayli.write(soz + "\n")

#2
eng_yuqori_ball = -1
eng_yuqori_talaba = ""

with open("talabalar1.txt", "r") as kirish_fayli, \
        open("yuqori.txt", "w") as yuqori_fayl, \
        open("past.txt", "w") as past_fayl:
    for qator in kirish_fayli:
        qismlar = qator.split()
        if not qismlar:
            continue

        ism = qismlar[0]
        ball = int(qismlar[1])
        if ball >= 80:
            yuqori_fayl.write(qator.strip() + "\n")
        else:
            past_fayl.write(qator.strip() + "\n")
        if ball > eng_yuqori_ball:
            eng_yuqori_ball = ball
            eng_yuqori_talaba = ism

print(f"Eng yuqori ball olgan talaba: {eng_yuqori_talaba} ({eng_yuqori_ball} ball)")

#3
with open("matn1.txt", "r") as kirish_fayli:
    matn = kirish_fayli.read()
sozlar = matn.lower().split()

korilgan_sozlar = []
takroriy_sozlar = []

for soz in sozlar:
    if soz in korilgan_sozlar:
        if soz not in takroriy_sozlar:
            takroriy_sozlar.append(soz)
    else:
        korilgan_sozlar.append(soz)

with open("takrorlar.txt", "w") as chiqish_fayli:
    for soz in takroriy_sozlar:
        chiqish_fayli.write(soz + "\n")

#4
qidirilayotgan_kitob = input("Kitob nomini kiriting: ").strip()

topildi = False
qator_raqami = 0

with open("kitoblar.txt", "r") as fayl:
    for qator in fayl:
        qator_raqami += 1
        if qator.strip().lower() == qidirilayotgan_kitob.lower():
            print(f"Kitob {qator_raqami}-qatorda joylashgan.")
            topildi = True
            break

if not topildi:
    print("Kitob topilmadi")

#5
with open("matn1.txt", "r") as kirish_fayli:
    matn = kirish_fayli.read()

yangi_matn = matn.replace("Python", "Dasturlash")

yangi_matn = yangi_matn.upper()

with open("yangi_matn.txt", "w") as chiqish_fayli:
    chiqish_fayli.write(yangi_matn)