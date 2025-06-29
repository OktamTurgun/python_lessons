"""
07-dars: Python collections kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda collections kutubxonasining quyidagi sinflarini o‘rganamiz:
 - Counter
 - defaultdict
 - namedtuple
 - deque
"""

from collections import Counter, defaultdict, namedtuple, deque

# Counter - elementlar sonini hisoblash
fruits = ['olma', 'banan', 'olma', 'anor', 'banan', 'olma']
hisob = Counter(fruits)
print("Counter natija:", hisob)
print("Eng ko‘p so‘z:", hisob.most_common(1))

# defaultdict - standart qiymat bilan lug‘at
yoshlar = defaultdict(lambda: 18)
yoshlar['Ali'] = 20
yoshlar['Vali'] = 22
print("Ali yoshi:", yoshlar['Ali'])
print("Hasan yoshi:", yoshlar['Hasan'])  # mavjud emas, lekin default 18

# namedtuple - oddiy class o‘rnini bosuvchi tuzilma
Talaba = namedtuple('Talaba', ['ism', 'yosh', 'kurs'])
t1 = Talaba(ism='Dilshod', yosh=21, kurs=3)
print("Talaba:", t1)
print("Ismi:", t1.ism)

# deque - ikki taraflama navbat
navbat = deque(['Ali', 'Vali'])
navbat.append('Hasan')         # oxiriga qo‘shish
navbat.appendleft('Sardor')    # boshiga qo‘shish
print("Navbat:", navbat)
navbat.pop()                   # oxiridan chiqarish
navbat.popleft()               # boshidan chiqarish
print("Yangilangan navbat:", navbat)

# Amaliy mashq: Talabalar ro'yxatini yaratish va ularni boshqarish
Talaba = namedtuple('Talaba', ['ism', 'yosh', 'kurs'])
talabalar = deque()


def talabani_qoshish(ism, yosh, kurs):
    talabalar.append(Talaba(ism, yosh, kurs))
    print(f"{ism} talaba qo'shildi.")


def talabani_ochirish():
    if talabalar:
        talaba = talabalar.popleft()
        print(f"{talaba.ism} talaba o'chirildi.")
    else:
        print("Talabalar ro'yxati bo'sh.")


def talabalar_list_print():
    if talabalar:
        print("Talabalar ro'yxati:")
        for talaba in talabalar:
            print(f" - {talaba.ism}, Yosh: {talaba.yosh}, Kurs: {talaba.kurs}")
    else:
        print("Talabalar ro'yxati bo'sh.")


# Amaliy mashq: Talabalar ro'yxatini boshqarish
talabani_qoshish('Dilshod', 21, 3)
talabani_qoshish('Sardor', 22, 2)
talabani_qoshish('Hasan', 20, 1)
talabalar_list_print()
