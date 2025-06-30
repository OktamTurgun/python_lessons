"""
18-dars: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-28
Mashq: 
1. Foydalanuvchidan son olib uning ildizi, kvadrati va faktorialini hisoblang.
2. Burchak berilganda uning `sin`, `cos`, `tan` qiymatlarini chiqaring.
3. Quyidagi ifodani hisoblang:
   **z = √(a² + b²)**  (a va b foydalanuvchidan olinadi)
"""
import math
from termcolor import colored


def calculate_all(number):
    """Sonning ildizi, kvadrati va faktorialini hisoblaydi"""
    try:
        # Sonning ildizi
        sqrt_num = math.sqrt(number)

        # Sonning kvadrati
        square_num = number ** 2

        # Sonning faktoriali (faqat musbat butun sonlar uchun)
        if number >= 0 and isinstance(number, int):
            factorial_num = math.factorial(number)
        else:
            factorial_num = "Faktorial faqat manfiy bo'lmagan butun sonlar uchun"

        return sqrt_num, square_num, factorial_num

    except ValueError:
        return None


def main():
    print(colored("Sonning ildizi, kvadrati va faktorialini hisoblash dasturi", "green"))
    print(colored("=" * 50, "blue"))

    while True:
        try:
            num = int(input(colored(
                "Iltimos, biror butun son kiriting (chiqish uchun '0' ni bosing): ", "yellow")))

            if num == 0:
                print(colored("Dastur to'xtatildi.", "red"))
                break

            sqrt, square, factorial = calculate_all(num)

            print(colored("\nNatijalar:", "magenta"))
            print(colored(f"Kiritilgan son: {num}", "cyan"))
            print(colored(f"Sonning ildizi: {sqrt:.4f}", "yellow"))
            print(colored(f"Sonning kvadrati: {square}", "green"))
            print(colored(f"Sonning faktoriali: {factorial}", "blue"))
            print(colored("=" * 50, "blue"))

        except ValueError:
            print(colored("Xato! Iltimos, faqat butun son kiriting.", "red"))


if __name__ == "__main__":
    main()
