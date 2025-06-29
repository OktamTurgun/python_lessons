"""
03-dars: Python random kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda random kutubxonasi yordamida tasodifiy sonlar, elementlar, aralashtirish va tanlash funksiyalari o'rganiladi:
 - randint(), uniform()
 - random(), choice(), shuffle()
 - sample()
"""

import string
import random

# Tasodifiy butun son
# 1 dan 10 gacha butun son
print("random.randint(1, 10):", random.randint(1, 10))

# Tasodifiy haqiqiy son (float)
print("random.uniform(1, 5):", random.uniform(1, 5))    # 1.0 dan 5.0 gacha

# 0.0 dan 1.0 gacha tasodifiy son
print("random.random():", random.random())

# choice() - ro'yxatdan bitta element tanlash
mevalar = ["olma", "anor", "banan", "shaftoli"]
print("random.choice(mevalar):", random.choice(mevalar))

# shuffle() - ro'yxatni aralashtirish
raqamlar = [1, 2, 3, 4, 5]
random.shuffle(raqamlar)
print("Aralashtirilgan ro'yxat:", raqamlar)

# sample() - N ta tasodifiy element tanlash
print("random.sample(range(1, 20), 5):", random.sample(range(1, 20), 5))

# Amaliy mashq: tasodifiy parol generator


def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


print("Parol:", generate_password())

# Amaliy mashq: tasodifiy rang generator


def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


print("Tasodifiy rang:", generate_random_color())

# Amaliy mashq: tasodifiy sanani olish


def generate_random_date(start_year=2000, end_year=2025):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 28 kunli oy
    return f"{year}-{month:02d}-{day:02d}"


print("Tasodifiy sana:", generate_random_date())

# Amaliy mashq: tasodifiy vaqt generator


def generate_random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}:{second:02d}"


print("Tasodifiy vaqt:", generate_random_time())

# Amaliy mashq: tasodifiy IP manzil generator


def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


print("Tasodifiy IP manzil:", generate_random_ip())

# Amaliy mashq: tasodifiy parol generator (max uzunlik)


def generate_password_with_max_length(max_length=12):
    length = random.randint(8, max_length)
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


print("Tasodifiy parol (max uzunlik 12):",
      generate_password_with_max_length(12))

# Amaliy mashq: tasodifiy raqam generator (max qiymat)


def generate_random_number(max_value=100):
    return random.randint(1, max_value)


print("Tasodifiy raqam (max qiymat 100):", generate_random_number(100))
