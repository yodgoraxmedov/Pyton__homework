#1 Shaxs - ota (asosiy) klass
class Shaxs:
    def __init__(self, ism, familiya, yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.yosh} yosh"


#2 Fan klassi
class Fan:
    def __init__(self, nomi, kredit, oqituvchi):
        self.nomi = nomi
        self.kredit = kredit
        self.oqituvchi = oqituvchi

    def get_info(self):
        return f"{self.nomi} ({self.kredit} kredit, o'qituvchi: {self.oqituvchi})"


#3 Talaba - Shaxs dan voris klass
class Talaba(Shaxs):
    def __init__(self, ism, familiya, yosh, universitet, kurs):
        super().__init__(ism, familiya, yosh)
        self.universitet = universitet
        self.kurs = kurs
        self.fanlar = []

    def fanga_yozil(self, fan):
        """Fan obyektini qabul qilib, fanlar ro'yxatiga qo'shadi"""
        if fan in self.fanlar:
            print(f"Siz {fan.nomi} faniga allaqachon yozilgansiz")
        else:
            self.fanlar.append(fan)
            print(f"{self.ism} {fan.nomi} faniga yozildi")

    def remove_fan(self, fan):
        """Fanni ro'yxatdan o'chiradi"""
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return f"{fan.nomi} fani o'chirildi"
        return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        fanlar = ", ".join(fan.nomi for fan in self.fanlar) or "yo'q"
        return (f"Talaba: {super().get_info()}, {self.universitet}, "
                f"{self.kurs}-kurs. Fanlari: {fanlar}")


#4 Professor - Shaxs dan voris klass
class Professor(Shaxs):
    def __init__(self, ism, familiya, yosh, kafedra, unvon="dotsent"):
        super().__init__(ism, familiya, yosh)
        self.kafedra = kafedra
        self.unvon = unvon
        self.darslar = []

    def dars_qoshish(self, fan):
        self.darslar.append(fan)
        print(f"Prof. {self.familiya} endi {fan.nomi} fanidan dars beradi")

    def get_info(self):
        return (f"Professor: {super().get_info()}, kafedra: {self.kafedra}, "
                f"unvoni: {self.unvon}, darslari soni: {len(self.darslar)}")


#5 Foydalanuvchi - Shaxs dan voris klass
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, login, email):
        super().__init__(ism, familiya, yosh)
        self.login = login
        self.email = email
        self.faol = True

    def parol_ozgartir(self, yangi_parol):
        if len(yangi_parol) < 6:
            print("Parol kamida 6 ta belgidan iborat bo'lishi kerak")
        else:
            print(f"{self.login} paroli o'zgartirildi")

    def get_info(self):
        holat = "faol" if self.faol else "bloklangan"
        return (f"Foydalanuvchi: {super().get_info()}, login: {self.login}, "
                f"email: {self.email}, holati: {holat}")


#6 Sotuvchi - Shaxs dan voris klass
class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, dokon, maosh=0):
        super().__init__(ism, familiya, yosh)
        self.dokon = dokon
        self.maosh = maosh
        self.sotuvlar = 0

    def sotish(self, summa):
        self.sotuvlar += summa
        print(f"{self.ism} {summa} so'mlik mahsulot sotdi")

    def get_info(self):
        return (f"Sotuvchi: {super().get_info()}, do'kon: {self.dokon}, "
                f"jami sotuv: {self.sotuvlar} so'm")


#7 Mijoz - Shaxs dan voris klass
class Mijoz(Shaxs):
    def __init__(self, ism, familiya, yosh, telefon):
        super().__init__(ism, familiya, yosh)
        self.telefon = telefon
        self.xaridlar = []

    def xarid_qil(self, mahsulot):
        self.xaridlar.append(mahsulot)
        print(f"{self.ism} {mahsulot} sotib oldi")

    def get_info(self):
        return (f"Mijoz: {super().get_info()}, tel: {self.telefon}, "
                f"xaridlar soni: {len(self.xaridlar)}")


#8 Admin - Foydalanuvchi dan voris klass (Shaxs ning "nevarasi")
class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, yosh, login, email):
        super().__init__(ism, familiya, yosh, login, email)
        self.huquqlar = ["ban_user", "unban_user", "foydalanuvchilarni_korish"]

    def ban_user(self, foydalanuvchi):
        """Foydalanuvchida yo'q, faqat Admin da bor metod"""
        foydalanuvchi.faol = False
        print("Foydalanuvchi bloklandi")

    def unban_user(self, foydalanuvchi):
        foydalanuvchi.faol = True
        print("Foydalanuvchi blokdan chiqarildi")

    def get_info(self):
        return f"ADMIN | {super().get_info()}, huquqlari: {', '.join(self.huquqlar)}"


# ======================= Sinov =======================
print("------------------- Fanlar va talaba -------------------")
matematika = Fan("Matematika", 6, "Karimov")
fizika = Fan("Fizika", 5, "Rahimov")
python = Fan("Python dasturlash", 4, "Yusupov")
tarix = Fan("Tarix", 3, "Saidova")

talaba = Talaba("Yodgor", "Axmedov", 20, "UrDU", 3)
talaba.fanga_yozil(matematika)
talaba.fanga_yozil(python)
talaba.fanga_yozil(fizika)
talaba.fanga_yozil(python)
print(talaba.get_info())

print(talaba.remove_fan(fizika))
print(talaba.remove_fan(tarix))
print(talaba.get_info())

print("------------------- Voris klasslar -------------------")
prof = Professor("Alisher", "Karimov", 52, "Oliy matematika", "professor")
prof.dars_qoshish(matematika)

user = Foydalanuvchi("Latif", "Olimov", 20, "latif_01", "latif@mail.uz")
user.parol_ozgartir("123")
user.parol_ozgartir("kuchli_parol")

sotuvchi = Sotuvchi("Temur", "Qodirov", 30, "Texnomart", 4000000)
sotuvchi.sotish(1500000)

mijoz = Mijoz("Asad", "Rasulov", 25, "+998 90 123 45 67")
mijoz.xarid_qil("Telefon")

print("------------------- Admin -------------------")
admin = Admin("Vohid", "Ergashev", 28, "admin", "admin@site.uz")
admin.ban_user(user)

print("------------------- Barcha get_info() -------------------")
for odam in [talaba, prof, user, sotuvchi, mijoz, admin]:
    print(odam.get_info())





#1 Shaxs klassi
class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, familiya, yosh):
        self.__ism = ism
        self.__familiya = familiya
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def get_familiya(self):
        return self.__familiya

    def get_yosh(self):
        return self.__yosh

    def set_ism(self, yangi_ism):
        if yangi_ism.isalpha():
            self.__ism = yangi_ism
        else:
            print("Ism faqat harflardan iborat bo'lishi kerak")

    def set_familiya(self, yangi_familiya):
        self.__familiya = yangi_familiya

    def set_yosh(self, yangi_yosh):
        if 0 < yangi_yosh < 120:
            self.__yosh = yangi_yosh
        else:
            print("Yosh noto'g'ri kiritildi")

    def get_info(self):
        return f"{self.__ism} {self.__familiya}, {self.__yosh} yosh"

    @classmethod
    def get_odamlar_soni(cls):
        return f"Jami odamlar soni: {cls.odamlar_soni}"


#2 Talaba klassi - Shaxs dan voris
class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familiya, yosh, universitet, kurs):
        super().__init__(ism, familiya, yosh)   # odamlar_soni ham oshadi
        self.__universitet = universitet
        self.__kurs = kurs
        Talaba.talabalar_soni += 1

    def get_universitet(self):
        return self.__universitet

    def get_kurs(self):
        return self.__kurs

    def set_universitet(self, yangi_universitet):
        self.__universitet = yangi_universitet

    def set_kurs(self, yangi_kurs):
        if 1 <= yangi_kurs <= 4:
            self.__kurs = yangi_kurs
        else:
            print("Kurs 1 dan 4 gacha bo'lishi kerak")

    def get_info(self):
        return f"Talaba: {super().get_info()}, {self.__universitet}, {self.__kurs}-kurs"

    # Klass metodlari
    @classmethod
    def get_talabalar_soni(cls):
        return f"Jami talabalar soni: {cls.talabalar_soni}"

    @classmethod
    def from_string(cls, matn):
        """Matndan talaba yaratadi: 'Ism,Familiya,yosh,universitet,kurs'"""
        ism, familiya, yosh, universitet, kurs = matn.split(",")
        return cls(ism, familiya, int(yosh), universitet, int(kurs))


# ======================= Sinov =======================
shaxs1 = Shaxs("Latif", "Olimov", 20)
talaba1 = Talaba("Yodgor", "Axmedov", 19, "UrDU", 2)
talaba2 = Talaba("Asad", "Rasulov", 18, "TATU", 1)
talaba3 = Talaba.from_string("Temur,Qodirov,21,UrDU,3")   # classmethod orqali

print(talaba1.get_info())
print(talaba3.get_info())

print("---------------- Getter va setter ----------------")
print("Ismi:", talaba1.get_ism())
print("Kursi:", talaba1.get_kurs())

talaba1.set_kurs(3)
talaba1.set_yosh(20)
talaba1.set_kurs(7)              # noto'g'ri qiymat
talaba1.set_ism("Yodgor123")     # noto'g'ri qiymat
print(talaba1.get_info())

print("---------------- Yopiq xususiyat ----------------")
try:
    print(talaba1.__ism)
except AttributeError:
    print("talaba1.__ism ga to'g'ridan-to'g'ri murojaat qilib bo'lmaydi!")

print("---------------- Klass xususiyatlari ----------------")
print(Shaxs.get_odamlar_soni())       # 1 shaxs + 3 talaba = 4
print(Talaba.get_talabalar_soni())    # 3
