class User:
    def __init__(self, full_name, username, email, followers=0):
        self.full_name = full_name
        self.username = username
        self.email = email
        self.followers = followers

    def get_info(self):
        """Foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli formatda qaytaradi"""
        return f"Foydalanuvchi: {self.username}, ismi: {self.full_name}, email: {self.email}"

    def get_followers_count(self):
        """Obunachilar sonini ko'rsatuvchi qo'shimcha metod"""
        return f"@{self.username} ning obunachilari soni: {self.followers} ta"

    def follow(self):
        """Obuna bo'lish tugmasi vazifasini bajaruvchi metod"""
        self.followers += 1
        return f"Siz @{self.username} ga obuna bo'ldingiz! Hozirgi obunachilar: {self.followers}"


user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com", 120)
user2 = User("Madina Karimova", "madina_k", "madina_k@mail.ru", 340)
user3 = User("Jasurbek Toshmatov", "jasur_t", "jasur@gmail.com", 55)

print("--- Obyekt xususiyatlari ---")
print(f"1-foydalanuvchi ismi: {user1.full_name}")
print(f"2-foydalanuvchi logini: {user2.username}")
print(f"3-foydalanuvchi emaili: {user3.email}\n")

print("--- get_info() metodi natijalari ---")
print(user1.get_info())
print(user2.get_info())
print(user3.get_info())
print()

print("--- Boshqa metodlar va amallar ---")
print(user1.get_followers_count())
print(user1.follow())