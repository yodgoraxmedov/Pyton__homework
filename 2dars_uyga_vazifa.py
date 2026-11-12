# capitalize() 3Birichi harf katta harf bilan yoziladi
print("PYTHON".capitalize())
a="Hello World"
print(a.capitalize())

#casefold() Satrni kichik harfga o'tkazadi
print("PYTHON".casefold())
print("AXMEDOV YODGOR".casefold())

#center() satrni berilgan kenglik ichida markazga joylashtiradi, ikki yonini to’ldiruvchi belgi bilan (odatda probel) to’ldiradi.
print("Assalomu alaykum".center(45))
a="O'zbekiston poytaxti Toshkent shaxri"
print(a.center(45))

#count() satr ichida berilgan qism satr (yoki belgi) necha marta uchrashini sanaydi va butun son qaytaradi.
a="Urganch go'zal shahar"
print(a.count("a"))
print(a.count("shahar"))
print(a.count("h"))
print(a.count("m"))

#encode() satrni baytlarga (bytes turiga) aylantiradi. Kompyuter xotirasi, fayl va internet bilan ishlashda matn aynan baytlar ko’rinishida saqlanadi va uzatiladi.
a="Hello"
b=a.encode()
print(b)
print(list(b))

d="Axmedov Yodgor"
e=d.encode()
print(e)
print(list(e))

#endswith() satr berilgan qism bilan tugaydimi yoki yo’qligini tekshiradi. Natija True yoki False bo’ladi.
a="Urganch go'zal shahar"
print(a.endswith("Urhanch"))
print(a.endswith("r"))
print(a.endswith("shahar"))

b="O'zbekiston poytaxti Toshkent shaxri"
print(b.endswith("poytaxti"))
print(b.endswith("Toshkent"))
print(b.endswith("shahri"))

#expandtabs() satrdagi tabulyatsiya belgilarini (\t) probellarga almashtiradi. Standart bo’yicha tab kengligi 8 ga teng.
a="u\tr\tg\ta\tn\tc\th"
print(a.expandtabs(2))

b="A\tX\tM\tE\tD\tO\tV"
print(b.expandtabs(2))
print(b.expandtabs(3))
print(b.expandtabs())

#find() satr ichida qism satrni (yoki belgini) qidiradi va birinchi topilgan joyning indeksini qaytaradi. Topilmasa -1 qaytaradi.
a="Urganch go'zal shahar"
print(a.find("u"))
print(a.find("g"))
print(a.find("shahar"))

#format() satr ichidagi {} joylariga qiymatlarni qo’yib beradi. Matn va o’zgaruvchilarni chiroyli birlashtirish uchun ishlatiladi
ism="Yodgor"
yosh=20
print("Mening ismim {}, yoshim {}".format(ism,yosh))
#1
#indeks bilan
print("{0} va {1}".format("olma", "anor"))
#2
#nom bilan
print("ism: {}, yosh: {}".format("Yodgor", "20"))
#3
#sonlarni formatlash
print("{:.3f}".format(13/8))
#4
#kenglik
print("{:>20}".format("Axmedov"))
print("{:<20}|".format("Axmedov"))
print("|{:^20}|".format("Axmedov"))
print("{:>5}".format("Axmedov"))
print("{:*^20}".format("Axmedov"))

#format_map
shaxs = {"ism": "Yodgor", "yosh": 20}
print("Mening ismim {ism}, yoshim {yosh} da".format_map(shaxs))

narx={"nomi": "Cobalt", "rangi": "Oq", "narxi": "165.448.779"}
print("Avtomobilning nomi:{nomi}, \nRangi:{rangi}, \nNarxi:{narxi} so'm".format_map(narx))

#index satr ichida qism satrni qidiradi va birinchi topilgan joyning indeksini qaytaradi. find() bilan deyarli bir xil, lekin topilmasa xato (ValueError) chiqaradi.
a="Hello World"
print(a.index("Hello"))
print(a.index("W"))
print(a.index("l"))

#isalnum() satrdagi hamma belgilar harf yoki raqam ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("python3".isalnum())
print("python_3".isalnum())

#isalpha() satrdagi hamma belgilar harf ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("python".isalpha())
print("python_3".isalpha())

#isascii satrdagi hamma belgilar ASCII jadvaliga kirishini tekshiradi, ya’ni har bir belgining raqami 0 dan 127 gacha bo’lishi kerak. Natija True yoki False bo’ladi.
print("Axmedov".isascii())
print("Hello😀".isascii())

#isdemical satrdagi hamma belgilar o’nlik raqam (0-9) ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("12500".isdecimal())
print("12,5".isdecimal())

#isdigit satrdagi hamma belgilar raqam ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("12345".isdigit())
print("12,345".isdigit())

#isidentifier() satr Python’da to’g’ri nom (identifikator) bo’la oladimi, ya’ni o’zgaruvchi, funksiya yoki klass nomi sifatida ishlatsa bo’ladimi, shuni tekshiradi. Natija True yoki False bo’ladi.
print("2nom".isidentifier())
print("nom".isidentifier())

#islower() satrdagi hamma harflar kichik ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("matn".islower())
print("Matn".islower())

#isnumeric() satrdagi hamma belgilar son manosini beruvchi belgi ekanligini tekshiradi. Natija True yoki False bo’ladi. Bu uch metod (isdecimal, isdigit, isnumeric) ichida eng keng qamrovlisi.
print("777".isnumeric())
print("-777".isnumeric())

#isprintable() satrdagi hamma belgilar chop etiladigan (ekranda ko’rinadigan) ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("Hello World".isprintable())
print("Hello \nWorld".isprintable())

#isspace() satrdagi hamma belgilar bo’shliq (probel kabi) ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("123456".isspace())
print("\n".isspace())
print(" ".isspace())

#istitle() satr sarlavha (title) shaklida ekanligini tekshiradi, ya’ni har bir so’z katta harf bilan boshlanib, qolgan harflari kichik bo’lishi kerak. Natija True yoki False bo’ladi.
print("Axmedov".istitle())
print("axmedov".istitle())

#isupper() satrdagi hamma harflar katta ekanligini tekshiradi. Natija True yoki False bo’ladi.
print("AXMEDOV".isupper())
print("axmedov".isupper())

#join() ro’yxat (yoki boshqa ketma-ketlik) ichidagi satrlarni bitta satrga birlashtiradi, ular orasiga o’zi chaqirilgan satrni qo’yadi.
a=["Winter", "is", "coming"]
print(" ".join(a))
print("-".join(a))
print("_".join(a))

#ljust() satrni berilgan kenglikka chapga yopishtirib joylashtiradi, o’ng tomonini probel (yoki siz bergan belgi) bilan to’ldiradi.
b="Axmedov"
print(b.ljust(15) + "|")
print(b.ljust(15,  "-") + "|")

#lstrip() satrning boshidagi (chap tomonidagi) bo’shliqlarni (yoki berilgan belgilarni) olib tashlaydi. Yangi satr qaytaradi, asl satr o’zgarmaydi. (l = left, ya’ni chap.)
a = "   Axmedov   "
print(a.lstrip() + "|")
b="\n\tHello World   "
print(b.lstrip() + "|")

#maketrans() belgilarni almashtirish uchun jadval (lug’at) yasaydi. Bu jadval translate() metodiga beriladi, u esa satrdagi belgilarni jadval bo’yicha almashtiradi. Ya’ni ikkalasi doim birga ishlatiladi.
jadval = str.maketrans("qwe", "123")
print("qqwwee".translate(jadval))

#partition() satrni berilgan ajratgich bo’yicha birinchi uchragan joyidan uch qismga bo’ladi va kortej (tuple) qaytaradi: ajratgichdan oldingi qism, ajratgichning o’zi, undan keyingi qism.
a = "Winter-is-Coming"
print(a. partition("-"))
print(a.partition("_"))

#replace() satr ichidagi qism satrni boshqasiga almashtiradi. Yangi satr qaytaradi, asl satr o’zgarmaydi.
a = "avtomabil"
print(a.replace("a","o"))
print(a.replace("a","o",1))

#rfind() satr ichida qism satrni qidiradi va oxirgi topilgan joyning indeksini qaytaradi. Topilmasa -1 qaytaradi. (r = right, ya’ni o’ngdan qidiradi.)
c = "salom dunyo"
print(c.rfind("y"))
d = "shahar"
print(d.rfind("a"))

#rindex() ham rfind() kabi oxirgi topilgan joyning indeksini beradi (o’ngdan qidiradi). Farqi faqat bitta: topilmasa xato chiqaradi.
v = "mahalla"
print(v.rindex("a"))







#LIST(RO'YHAT) usullari
#append() – bu list (ro’yxat) metodi (string metodi emas). U ro’yxatning oxiriga bitta element qo’shadi. Yangi ro’yxat yaratmaydi, mavjud ro’yxatni o’zgartiradi va None qaytaradi.
a = ["malibu", "cobalt"]
a.append("tahoe")
print(a)

#copy() ro’yxatning nusxasini (ko’chirmasini) yasaydi. Yangi, mustaqil ro’yxat qaytaradi, shuning uchun nusxani o’zgartirsangiz, asl ro’yxat o’zgarmaydi.
a = [1,2,3,4]
b = a.copy()
print(b)

#count() berilgan qiymat ro’yxatda necha marta uchrashini sanaydi va butun son qaytaradi. Satrdagi count() bilan deyarli bir xil, faqat bu yerda belgi emas, element sanaladi.
n = [9,4,7,8,9]
print(n.count(4))
print(n.count(9))

#extend() boshqa ro’yxatning (yoki istalgan ketma-ketlikning) hamma elementlarini joriy ro’yxatning oxiriga qo’shadi. Asl ro’yxatning o’zi o’zgaradi.
s = ["nu"]
s.extend("salom")
print(s)

#index() berilgan qiymatning birinchi uchragan joyining indeksini qaytaradi. Satrdagi index() bilan deyarli bir xil, faqat bu yerda qism satr emas, element qidiriladi.
avtomobillar = ["cobalt", "lacetti", "malibu"]
print(avtomobillar.index("cobalt"))
print(avtomobillar.index("malibu"))

#insert() ro’yxatning istalgan o’rniga element qo’shadi. append() doim oxiriga qo’shardi, insert() esa qaysi indeksga qo’yishni o’zingiz tanlaysiz. Qolgan elementlar o’ngga siljiydi.
a = ["a","b","c","d"]
a.insert(2,"u")
print(a)

#pop() ro’yxatdan ko’rsatilgan indeksdagi elementni o’chiradi va uni qaytaradi. Indeks berilmasa, oxirgi elementni o’chiradi.
m = ["olma", "uzum", "anor"]
c = m.pop(2)
print(c)
print(m)

#remove() ro’yxatdan berilgan qiymatni topib o’chiradi. pop() indeks bo’yicha o’chirardi, remove() esa qiymat bo’yicha o’chiradi.
m = ["olma", "uzum", "anor"]
m.remove("olma")
print(m)

#reverse() ro’yxatdagi elementlar tartibini teskari qiladi: birinchi element oxirga, oxirgisi boshiga o’tadi. Asl ro’yxatning o’zi o’zgaradi.
m = ["olma", "uzum", "anor"]
m.reverse()
print(m)

#sort() ro’yxatdagi elementlarni tartiblaydi (saralaydi). Standart bo’yicha o’sish tartibida: sonlar kichikdan kattaga, satrlar alifbo bo’yicha. Asl ro’yxatning o’zi o’zgaradi.
sonlar = [2,1,3,4]
sonlar.sort()
print(sonlar)