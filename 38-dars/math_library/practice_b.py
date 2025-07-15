"""
18-dars: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
Burchak berilganda uning `sin`, `cos`, `tan` qiymatlarini chiqaring.
"""
import math
from termcolor import colored


def trigonometrik_hisobla():
    try:
        # Foydalanuvchidan burchakni olish (gradusda)
        burchak = float(
            input(colored("Burchakni gradusda kiriting (0-360): ", "yellow")))

        # Gradusni radianga aylantirish
        radian = math.radians(burchak)

        # Trigonometrik funksiyalarni hisoblash
        sinus = math.sin(radian)
        kosinus = math.cos(radian)
        tangens = math.tan(radian)

        # Natijalarni chiqarish
        print(colored(f"\n{burchak}° burchak uchun:", "cyan"))
        print(colored(f"sin({burchak}°) = {sinus:.4f}", "green"))
        print(colored(f"cos({burchak}°) = {kosinus:.4f}", "blue"))
        print(colored(f"tan({burchak}°) = {tangens:.4f}", "magenta"))

        # 90° ga karrali burchaklar uchun maxsus xabar
        if burchak % 90 == 0 and burchak % 180 != 0:
            print(
                colored("\nEslatma: 90° va 270° burchaklar uchun tangens aniqlanmagan!", "red"))

    except ValueError:
        print(colored("Xato! Iltimos, son kiriting.", "red"))


def main():
    print(colored("Trigonometrik funksiyalarni hisoblash dasturi",
          "green", attrs=["bold"]))
    print(colored("=" * 50, "blue"))

    while True:
        trigonometrik_hisobla()

        # Dasturni davom ettirish yoki to'xtatish
        davom = input(
            colored("\nYana hisoblashni xohlaysizmi? (ha/yo'q): ", "yellow")).lower()
        if davom != 'ha':
            print(colored("Dastur to'xtatildi. Rahmat!", "red"))
            break


if __name__ == "__main__":
    main()
