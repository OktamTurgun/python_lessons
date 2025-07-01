"""
Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π
soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 

Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki 
yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, 
tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 
ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.
"""
# with open("pi_million_digits.txt") as file:
#   pi_string = file.read().replace("\n", "").replace(" ", "")
#   def check_birthday_in_pi(birthday):
#     """
#     Tug'ilgan kuningizni π soni tarkibida tekshiruvchi funksiya.

#     :param birthday: Tug'ilgan kuningiz (masalan, "25022000" - 25 Fevral, 2000-yil)
#     :return: True agar tug'ilgan kun π sonida mavjud bo'lsa, aks holda False
#     """
#     return birthday in pi_string

# # Tug'ilgan kuningizni kiriting
# birthday = "13031990" # 13 Mart, 1990-yil
# if check_birthday_in_pi(birthday):
#     print(f"Tug'ilgan kuningiz ({birthday}) π sonida mavjud.")
# else:
#     print(f"Tug'ilgan kuningiz ({birthday}) π sonida mavjud emas.")

# Exercise: 2
with open("pi_million_digits.txt") as file:
    pi_string = file.read().replace("\n", "").replace(" ", "")
    pi_digits = pi_string[2:]  # "3." dan keyingi qismini olamiz


def check_birthday_in_pi(birthday):
    """
    Tug'ilgan kuningizni π soni tarkibida tekshiruvchi funksiya.

    :param birthday: Tug'ilgan kuningiz string ko'rinishida (masalan, "25022000" - 25 Fevral, 2000-yil)
    :type birthday: str
    :return: True agar tug'ilgan kun π sonida mavjud bo'lsa, aks holda False
    :rtype: bool
    :raises ValueError: Agar birthday faqat raqamlardan iborat bo'lmasa
    """
    if not birthday.isdigit():
        raise ValueError(
            "Tug'ilgan kun faqat raqamlardan iborat bo'lishi kerak")
    return birthday in pi_digits


# Tug'ilgan kuningizni kiriting
birthday = "17122012"  # 13 Mart, 1990-yil
try:
    if check_birthday_in_pi(birthday):
        print(f"Tug'ilgan kuningiz ({birthday}) π sonida mavjud.")
    else:
        print(f"Tug'ilgan kuningiz ({birthday}) π sonida mavjud emas.")
except ValueError as e:
    print(f"Xato: {e}")
