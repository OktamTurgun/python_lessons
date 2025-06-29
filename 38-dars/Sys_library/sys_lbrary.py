"""
05-dars: Python sys kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda sys kutubxonasi yordamida Python interpreteri, chiqishlar, argumentlar va modul yo'llari bilan ishlashni o'rganamiz:
 - argv (komanda qatori argumentlari)
 - exit()
 - stdout, stderr
 - path (modullar yo'li)
"""

import sys

# Komanda qatori argumentlari
print("Argumentlar (argv):", sys.argv)  # [fayl_nomi.py, arg1, arg2, ...]

# Python versiyasi
print("Python versiyasi:", sys.version)

# Standart chiqish va xatolik
sys.stdout.write("stdout: Salom, bu oddiy chiqish.\n")
sys.stderr.write("stderr: Bu xatolik chiqishi!\n")

# Interpreterni tugatish (exit)
# sys.exit("Dasturni yakunlayapmiz")  # (izoh uchun izohlangan)

# Modul yo‘llari - Python qayerdan modullarni qidiradi?
print("Modul yo‘llari:")
for path in sys.path:
    print(" -", path)

# Amaliy mashq: argument orqali salomlashish


def salom_ber():
    if len(sys.argv) > 1:
        ism = sys.argv[1]
        print(f"Salom, {ism}!")
    else:
        print("Foydalanuvchi ismi berilmadi.")


salom_ber()

# Amaliy mashq: modul yo'lini qo'shish


def modul_yol_qoshish(yol):
    if yol not in sys.path:
        sys.path.append(yol)

        print(f"{yol} modul yo'li qo'shildi.")
    else:
        print(f"{yol} modul yo'li allaqachon mavjud.")


modul_yol_qoshish("/my/custom/modules")

# Amaliy mashq: modul yo'lini chiqarish


def modul_yol_chiqarish():
    print("Modul yo'llari:")
    for path in sys.path:
        print(" -", path)


modul_yol_chiqarish()

# Amaliy mashq: modul yo'lini o'chirish


def modul_yol_ochirish(yol):
    if yol in sys.path:
        sys.path.remove(yol)
        print(f"{yol} modul yo'li o'chirildi.")
    else:
        print(f"{yol} modul yo'li topilmadi.")


modul_yol_ochirish("/my/custom/modules")
