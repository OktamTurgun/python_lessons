"""
Mavzu: Practice. String to Integers.
Muallif: Uktam Turgunov
Sana: 2025-07-05
Vazifa:
Convert_add degan funksiya yasang, u orqali kiritilgan stringlar listini ([‘1’, ‘3’, ‘5’])  integerga o’tkazib ([1, 3, 5]), summasi hisoblansin (9).

Bir qatorda ishlashga harakat qiling.
"""


def convert_add(list):
    """
    Stringlardan iborat ro'yxatni butun songa o'zgartirib, ularning yig'indisini qaytaradi.

    Argumentlar:
      list (str ro'yxati): Raqamli stringlardan iborat ro'yxat.

    Natija:
      int: O'zgartirilgan sonlarning yig'indisi.

    Xatoliklar:
      ValueError: Agar ro'yxatdagi biror element butun songa o'zgartirib bo'lmasa.
    """
    return sum(map(int, list))


if __name__ == "__main__":
    list = ['1', '2', '3', '4']
    print(convert_add(list))
