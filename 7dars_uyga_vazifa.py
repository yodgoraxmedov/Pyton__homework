#1
rang = input("Svetafor qaysi rangda? (qizil, sariq yoki yashil): ")

while rang != "qizil" and rang != "sariq" and rang != "yashil":
    print("Bu xato rang")
    rang = input("Svetafor qaysi rangda? (qizil, sariq yoki yashil): ")

print("rahmat, to'g'ri keladi")


print()
print("-------------------------------------------------------------")


#3
ismlar = []
n = 1

while True:
    ism = input(f"{n}-do'stingizning ismini kiriting (tugatish uchun 'stop'): ")
    if ism == "stop":
        break
    ismlar.append(ism)
    n += 1

print("Do'stlar ro'yxati:")
for ism in ismlar:
    print(ism)


print()
print("-------------------------------------------------------------")


#4
KURS = 12600  # 1 USD = 12 600 so'm

while True:
    matn = input("So'm miqdorini kiriting (chiqish uchun 'exit'): ")

    if matn.lower() == "exit":
        print("Dastur to'xtadi. Xayr!")
        break

    try:
        som = float(matn)
    except ValueError:
        print("Iltimos, son kiriting yoki 'exit' deb yozing!")
        continue

    if som < 0:
        print("Summa manfiy bo'lishi mumkin emas!")
        continue

    dollar = som / KURS
    print(f"{som:,.0f} so'm = {dollar:.2f} USD")


