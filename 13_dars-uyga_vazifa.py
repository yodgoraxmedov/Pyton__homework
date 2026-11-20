#1
class Avto:
    """Avto nomli klass yaratamiz"""
    def __init__(self, model, rang, karobka, narh, km=0):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = km

    def get_info(self):
        """Avto haqida to'liq ma'lumot"""
        return f"Modeli: {self.model}, Rangi: {self.rang}, Karobka: {self.karobka}, Narh: {self.narh}, Km: {self.km}"

    def update_km(self, km):
        """Yurilgan masofani qo'shib boradi"""
        if km >= 0:
            self.km += km
        else:
            print("Km manfiy bo'lishi mumkin emas")

    def update_narh(self, narh):  # <- shu yerga ko'chirildi
        """Avtomobil narxini yangilash"""
        if narh > 18000:
            self.narh = narh - (narh * 5) / 100  # 5% chegirma
        else:
            self.narh = narh
        print(self.get_info())


avto1 = Avto("Cobalt", "Oq", "Avtomat", 12000, 3460)
avto2 = Avto("Malibu", "Qora", "Avtomat", 25000, 9300)
avto3 = Avto("Kia", "Ko'k", "Avtomat", 30000, 8700)

print(avto1.get_info())
print(avto2.get_info())
print(avto3.get_info())

print("-----------------------Masofalar yangilandi---------------------")

avto1.update_km(300)
avto2.update_km(500)
avto3.update_km(1000)

print(avto1.get_info())
print(avto2.get_info())
print(avto3.get_info())

print("--------------Avtomobil narhlari yangilandi-------------------------")
avto2.update_narh(25000)
avto3.update_narh(30000)
print("-----------------------------Avtosalon---------------------------")
#2
class Avtosalon:
    def __init__(self, salon_nomi, manzili, xodimlar_soni = 0):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtomobillar = []
        self.xodimlar_soni = xodimlar_soni

    def avto_qoshish(self, avto):
        """Yangi avtomobillar qo'shish"""
        self.sotuvdagi_avtomobillar.append(avto)
        print(f"{avto.model} qo'shildi")

    def avtolar_haqida(self):
        """Salondagi avtomobillar haqida ma'lumot"""
        print(f"{self.salon_nomi} ({self.manzili}), "
              f"avtomobillar soni: {len(self.sotuvdagi_avtomobillar)}")
        for avto in self.sotuvdagi_avtomobillar:
            print(avto.get_info())


salon = Avtosalon("Avto Hamkor", "Urganch", xodimlar_soni=7)
salon.avto_qoshish(avto1)
salon.avto_qoshish(avto2)
salon.avto_qoshish(avto3)
salon.avto_qoshish(Avto("BMW", "Oq", "Avtomat", 18000, 9560))
salon.avtolar_haqida()

print("--------------------------------Methodlar---------------------------")
print(dir(Avtosalon))
print(dir(Avto))

print("-------------------------Obyektning xususiyatlari------------------")
print(Avtosalon.__dict__)
print(Avto.__dict__)





