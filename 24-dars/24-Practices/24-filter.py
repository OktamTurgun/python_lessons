"""
Filter funksiyasi uchun bir nechta amaliy mashqalar
"""

fruits = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "kiwi",
    "lemon",
    "mango",
]


def filter_mevalar(fruits, uzunlik):
    """
    Mevalarni uzunligiga qarab filtrlaydi

    Args:
        mevalar (list): Mevalar ro'yxati
        uzunlik (int): Filtrlash uchun minimal uzunlik

    Returns:
        list: Filtrlangan mevalar ro'yxati
    """
    return list(filter(lambda meva: len(meva) >= uzunlik, fruits))


filtered_fruits = filter_mevalar(fruits, 5)
print(
    "Uzunligi 5 dan katta bo'lgan mevalar:", filtered_fruits
)  # ['banana', 'cherry', 'elderberry', 'grape', 'lemon', 'mango']


# Matnlar ro‘yxatida belgilangan harf bor so‘zlarni ajratib oluvchi filter + lambda.
def filter_bosh_harf(fruits, harf):
    """
    Belgilangan harf bilan boshlanadigan mevalarni filtrlaydi

    Args:

        mevalar (list): Mevalar ro'yxati
        harf (str): Filtrlash uchun belgilangan harf
    Returns:
        list: Filtrlangan mevalar ro'yxati
    """
    return list(filter(lambda meva: meva.startswith(harf), fruits))


bosh_harf = filter_bosh_harf(fruits, "g")
print("Harf 'g' bilan boshlanadigan mevalar:", bosh_harf)


# Tub sonlarni topuvchi funksiya
def tub_sonlar(top_son):
    """
    Berilgan songacha bo'lgan tub sonlarni topadi

    Args:
        top_son (int): Tub sonlarni topish uchun maksimal son

    Returns:
        list: Tub sonlar ro'yxati
    """
    #
    return list(
        filter(
            lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
            range(2, top_son),
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


nums = [24, 10, 38, 13, 5, 42, 0, 16, 29]
tub_sonlar = list(
    filter(lambda x: tubmi(x), nums)
)  # tub sonlarni filter yordamida topish
print("Tub sonlar:", tub_sonlar)  # [13, 5, 29]
print(tub_sonlar)

# dict bilan filterlash
data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
filtered = filter(lambda item: item[1] % 2 == 0, data.items())
filtered_add = filter(lambda item: item[1] % 2 != 0, data.items())
print(dict(filtered))  # {'b': 2, 'd': 4, 'f': 6}
print(dict(filtered_add))  # {'a': 1, 'c': 3, 'e': 5}
