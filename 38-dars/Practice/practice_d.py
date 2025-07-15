"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
"""
import re
from termcolor import colored


PHONE_PATTERN = r"^[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{2,4}[-\s\.]?[0-9]{2,4}[-\s\.]?[0-9]{2,4}$"


def check_phone_number(number):
    """Telefon raqamning to'g'ri formatda ekanligini tekshiradi"""
    return re.match(PHONE_PATTERN, number) is not None


def format_phone_number(number):
    """Telefon raqamni standart formatga keltiradi"""
    # Faqat raqamlarni qoldiradi
    cleaned = re.sub(r"[^\d]", "", number)
    # Agar + belgisi bo'lmasa, qo'shamiz
    if not number.startswith("+"):
        cleaned = f"+{cleaned}"
    return cleaned


def main():
    print(colored("Telefon raqamni quyidagi formatlarda kiritishingiz mumkin:", "yellow"))
    print(colored("+998901234567, 998901234567, (90)123-45-67, 8-901-234-56-78", "blue"))

    while True:
        number = input("\nTelefon raqamingizni kiriting: ").strip()
        if check_phone_number(number):
            formatted_number = format_phone_number(number)
            print(
                colored(f"✅ Telefon raqam qabul qilindi: {formatted_number}", "green"))
            break
        else:
            print(colored(f"❌ Noto'g'ri format: {number}", "red"))
            print(colored("Iltomos to'g'ri formatda kiriting.", "yellow"))


if __name__ == "__main__":
    main()
