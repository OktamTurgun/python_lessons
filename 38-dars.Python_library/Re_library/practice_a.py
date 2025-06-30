"""
12-dars: Python re (regular expressions) kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-29

Ushbu darsda re kutubxonasi yordamida quyidagilarni o‘rganamiz:
-moslikni tekshirish (match)
"""
import re
from termcolor import colored  # ixtiyoriy, ranglar uchun

# Kuchli parolni tekshirish uchun regex andoza
PASSWORD_PATTERN = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"

# Parol talablari haqida xabar
PASSWORD_REQUIREMENTS = """
Parol quyidagi talablarga javob berishi kerak:
- Kamida 8 ta belgidan iborat bo'lsin
- Kamida 1 ta lotin bosh harf (A-Z)
- Kamida 1 ta kichik harf (a-z)
- Kamida 1 ta raqam (0-9)
- Kamida 1 ta maxsus belgi (#?!@$ %^&*-)
"""


def validate_password(password):
    """Parolni regex andoza bilan tekshiradi"""
    return re.match(PASSWORD_PATTERN, password)


def main():
    print(colored("Parolni kiriting:", "yellow"))
    print(colored(PASSWORD_REQUIREMENTS, "cyan"))

    while True:
        password = input(">>> ")
        if validate_password(password):
            print(colored("✅ Maxfiy so'z qabul qilindi!", "green"))
            break
        else:
            print(colored("❌ Maxfiy so'z talabga javob bermadi!", "red"))
            print(colored("Iltimos, talablarga mos parol kiriting!", "yellow"))


if __name__ == "__main__":
    main()
