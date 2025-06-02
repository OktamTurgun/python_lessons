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
