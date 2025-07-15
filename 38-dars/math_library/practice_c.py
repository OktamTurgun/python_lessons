"""
18-dars: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
Quyidagi ifodani hisoblang:
   **z = √(a² + b²)**  (a va b foydalanuvchidan olinadi)
"""
import math
from termcolor import colored


def hisoblash(a, b):
    """a va b asosida z = √(a² + b²) ni hisoblaydi"""
    return math.sqrt(a**2 + b**2)


def main():
    print(colored("z = √(a² + b²) ifodani hisoblash dasturi",
          "green", attrs=["bold"]))
    print(colored("=" * 50, "blue"))

    while True:
        try:
            a = float(input(colored("a sonini kiriting: ", "yellow")))
            b = float(input(colored("b sonini kiriting: ", "yellow")))

            z = hisoblash(a, b)

            print(colored("\nNatija:", "magenta"))
            print(colored(f"z = √({a}² + {b}²) = {z:.5f}", "cyan"))
            print(colored("=" * 50, "blue"))

            davom = input(
                colored("Yana hisoblashni xohlaysizmi? (ha/yo'q): ", "yellow")).lower()
            if davom != 'ha':
                print(colored("Dastur to'xtatildi. Rahmat!", "red"))
                break

        except ValueError:
            print(colored("Xato! Iltimos, son kiriting.", "red"))


if __name__ == "__main__":
    main()
