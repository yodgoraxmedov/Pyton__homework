#1
def user_data(first_name, last_name, age):
    print(f"Ismi: {first_name.title()}")
    print(f"Familiyasi: {last_name.title()}")
    print(f"Yoshi: {age}")

first_name = input("Ismingizni kiriting: ")
last_name = input("Familiyangizni kiriting: ")
age = input("Yoshingizni kiriting: ")
user_data(first_name, last_name, age)

#2
def find_max(a, b, c):
    if a > b and a > c:
        print(f"Eng katta son - A = {a}")
    elif b > a and b > c:
        print(f"Eng katta son - B = {b}")
    elif c > a and c > b:
        print(f"Eng katta son - C = {c}")
    elif a == b and a > c:
        print(f"Eng katta sonlar - A va B = {a}")
    elif a == c and a > b:
        print(f"Eng katta sonlar - A va C = {a}")
    elif b == c and b > a:
        print(f"Eng katta sonlar - B va C = {b}")
    else:
        print(f"Eng katta sonlar - A va B va C = {a}")


a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))
c = int(input("C sonini kiriting: "))

find_max(a, b, c)

3
def find_letter_count(word, letter):
    count = word.count(letter)
    print(f'"{word}" so\'zida "{letter}" dan {count} ta.')


word = input("So'z kiriting: ")
letter = input("Qidirmoqchi bo'lgan harfni kiriting: ")

find_letter_count(word, letter)

#4
def list_sum(myList):
    print(f"Listning elementlar yig'indisi = {sum(myList)}")
    list_sum([5, 7, 8, 12])


#6
def daraja4(a, b, c, d):
    print(f"{a} ning {b} darajasi = {a ** b}")
    print(f"{a} ning {c} darajasi = {a ** c}")
    print(f"{a} ning {d} darajasi = {a ** d}")

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))
d = int(input("d ni kiriting: "))
daraja4(a,b,c,d)

#7
def digit_count_and_sum(word):
    count = 0
    total = 0
    for belgi in word:
        if belgi.isdigit():
            count += 1
            total += int(belgi)
    print(f"Raqamlar soni: {count} ta")
    print(f"Raqamlar yig'indisi = {total}")

word = input("So'z kiriting: ")
digit_count_and_sum(word)

#8
def add_right(a, b):
    natija = str(a) + str(b)
    print(f"Natija: {natija}")

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))
add_right(a, b)

#9
def add_left(a, b):
    natija = str(a) + str(b)
    print(f"Natija: {natija}")

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))
add_left(a, b)

#10
def work_with_list(a):
    eng_kichik = min(a)
    for i in range(len(a)):
        a[i] = a[i] * eng_kichik
    print(a)

sonlar = [4, 2, 7, 5]
work_with_list(sonlar)

#11
def big_sales(sales):
    eng_katta_oy = ""
    eng_katta_summa = 0
    for oy in sales:
        if sales[oy] > eng_katta_summa:
            eng_katta_summa = sales[oy]
            eng_katta_oy = oy
    return eng_katta_oy
sales = {
    "yanvar": 12000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000,
}
natija = big_sales(sales)
print(natija)

#12
def min_max(numbers, max_num, min_num):
    if max_num == max(numbers):
        print(f"{max_num} - numbers ichida eng katta son: Ha")
    else:
        print(f"{max_num} - numbers ichida eng katta son: Yo'q")

    if min_num == min(numbers):
        print(f"{min_num} - numbers ichida eng kichik son: Ha")
    else:
        print(f"{min_num} - numbers ichida eng kichik son: Yo'q")

sonlar = [3, 5, 8, 2]
min_max(sonlar, 8, 5)
min_max(sonlar, 3, 2)


#13
def expensiveProduct(products):
    eng_qimmat_narx = 0
    eng_qimmat_nom = ""
    for product in products:
        if product["price"] > eng_qimmat_narx:
            eng_qimmat_narx = product["price"]
            eng_qimmat_nom = product["name"]
    print(f"Eng qimmat telefon: {eng_qimmat_nom}")

products = [
    {"name": "Iphone X", "price": 600},
    {"name": "Iphone 12", "price": 1500},
    {"name": "Samsung Note 9", "price": 800},
    {"name": "Samsung S10", "price": 1100},
]

expensiveProduct(products)












