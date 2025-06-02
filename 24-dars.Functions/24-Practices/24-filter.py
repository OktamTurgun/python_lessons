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


bosh_harf = filter_bosh_harf(fruits, "a")
print(
    "Harf 'a' bilan boshlanadigan mevalar:", bosh_harf
)  # ['apple', 'banana', 'date', 'elderberry', 'grape', 'lemon', 'mango']
