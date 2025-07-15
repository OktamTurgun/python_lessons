from random import sample
from math import sqrt

# Tasodifiy sonlar ro'yxatini yaratish va ularni kvadrat ildizlarini olish
x = list(range(0, 1001))  # 0 dan 1000 gacha bo'lgan sonlar
y = sample(x, k=10)  # Tasodifiy 10 ta son tanlash
print("Tasodifiy sonlar:", y)

# Kvadrat ildizlarini olish

ildizlar = list(map(lambda n: sqrt(n), y))  # Kvadrat ildizlarini olish
print("Kvadrat ildizlar:", ildizlar)

# Juft sonlarni topish
juft_sonlar = list(filter(lambda n: n % 2 == 0, y))
print("Juft sonlar:", juft_sonlar)
# Toq sonlarni topish
toq_sonlar = list(filter(lambda n: n % 2, y))
print("Toq sonlar:", toq_sonlar)


# Tub sonni topish
def tubmi(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


tub_sonlar = list(filter(tubmi, y))
print("Tub sonlar:", tub_sonlar)


# Tub sonlarni topish
def tub_sonlar(son):
    """
    Berilgan songacha bo'lgan tub sonlarni topadi

    Args:
        top_son (int): Tub sonlarni topish uchun maksimal son

    Returns:
        list: Tub sonlar ro'yxati
    """
    return list(
        filter(
            lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
            range(2, son),
        )
    )


tub_sonlar_royxati = tub_sonlar(50)
print(
    "Tub sonlar:", tub_sonlar_royxati
)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# Tub sonlarni topish funksiya bilan
def tubmi(n):
    """
    Berilgan son tub sonmi yoki yo'qligini tekshiradi
    Args:
        n (int): Tekshiriladigan son
    Returns:
        bool: True agar tub son bo'lsa, aks holda False
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


tub_sonlar_royxati = list(filter(tubmi, range(2, 50)))
print("Tub sonlar (funksiya bilan):", tub_sonlar_royxati)
