import random as r

# randint()
son = r.randint(0,10)
print(son)

# choice()
ismlar = ['olim', 'anvar', 'hasan', 'husan', 'ali']
ism = r.choice(ismlar)
print(ism)

harf = r.choice(ism)
print(harf)

nums = list(range(0, 51, 5))
print(nums)
print(r.choice(nums))

# Misollar random modulidan foydalanish
print(r.randint(1, 10))  # 1 dan 10 gacha tasodifiy butun son
print(r.random())  # 0 dan 1 gacha tasodifiy haqiqiy son
print(r.uniform(1, 10))  # 1 dan 10 gacha tasodifiy haqiqiy son
print(r.choice(['apple', 'banana', 'cherry']))  # Tasodifiy meva tanlash
print(r.sample([1, 2, 3, 4, 5], 3))  # Ro'yxatdan tasodifiy 3 element tanlash

# shuffle()
y = list(range(11))
print(y)
r.shuffle(y)
print(y)

my_list = [1, 2, 3, 4, 5]
r.shuffle(my_list)  # Ro'yxatni tasodifiy tartibda aralashtirish
print(my_list)

# Tasodifiy sonlar generatori
def random_numbers(n, start=1, end=100):
    """n ta tasodifiy sonlarni start va end oralig'ida qaytaradi"""
    return [r.randint(start, end) for _ in range(n)]
  
# Misol: 5 ta tasodifiy son
print(random_numbers(5, 1, 50))  # 5 ta tasodifiy son 1 dan 50 gacha

# Tasodifiy ro'yxat yaratish
def random_list(length, start=1, end=100):
    """Tasodifiy uzunlikdagi ro'yxat yaratadi"""
    return [r.randint(start, end) for _ in range(length)]
# Misol: 10 ta tasodifiy sonlardan iborat ro'yxat
print(random_list(10, 1, 20))  # 10 ta tasodifiy son 1 dan 20 gacha

# Tasodifiy ranglar generatori
def random_colors(n):
    """n ta tasodifiy ranglarni RGB formatida qaytaradi"""
    return [(r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)) for _ in range(n)]
# Misol: 5 ta tasodifiy rang
print(random_colors(5))  # 5 ta tasodifiy rang RGB formatida

# Tasodifiy parol generatori
def random_password(length=8, chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    """Tasodifiy parol yaratadi"""
    return ''.join(r.choice(chars) for _ in range(length))
  
# Misol: 12 ta belgidan iborat tasodifiy parol
print(random_password(12))  # 12 ta belgidan iborat tasodifiy parol

# Tasodifiy so'z generatori
# def random_words(n, word_length=5):
#     """n ta tasodifiy so'zlarni yaratadi"""
#     return [''.join(r.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(word_length)) for _ in range(n)]
# # Misol: 5 ta tasodifiy so'z
# print(random_words(5, 4))  # 5 ta tasodifiy 4 harfli so'z

# Tasodifiy raqamlar bilan o'yin
def guess_the_number():
    """Foydalanuvchi tasodifiy raqamni topishi kerak"""
    number = r.randint(1, 10)
    attempts = 0
    while True:
        guess = int(input("1 dan 10 gacha raqamni taxmin qiling: "))
        attempts += 1
        if guess < number:
            print("Kattaroq raqam kiriting.")
        elif guess > number:
            print("Kichikroq raqam kiriting.")
        else:
            print(f"Tabriklaymiz! Siz {attempts} urinishda to'g'ri topdingiz!")
            break

guess_the_number()  # Foydalanuvchi o'yinni boshlashi uchun funksiyani chaqirish

# Random ichun yana bir misol:
def ism_top():
    """Tasodifiy ism tanlash o'yini"""
    ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Anvar']
    print("Ismni topish o'yini!")
    print("Ismlar: ", ismlar)
    ism = r.choice(ismlar)
    urinishlar = 0
    while True:
        taxmin = input("Ismni taxmin qiling: ")
        urinishlar += 1
        if taxmin == ism:
            print(f"Tabriklaymiz! Siz {urinishlar} urinishda to'g'ri topdingiz!")
            break
        else:
            print("Noto'g'ri, yana urinib ko'ring.")
# Misol: o'yinni boshlash
ism_top()  # Foydalanuvchi o'yinni boshlashi uchun funksiyani chaqirish
