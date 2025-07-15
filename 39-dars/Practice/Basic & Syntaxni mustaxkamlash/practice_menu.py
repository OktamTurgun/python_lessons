"""
Mavzu: Practice. Basic & Syntaxni mustaxkamlash
Muallif: Uktam Turgunov
Sana: 2025-07-06
Vazifa:

"""

from datetime import datetime
from colorama import Fore, Style, init

# Colorama ni ishga tushuramiz
init(autoreset=True)


def faylga_yoz(matn):
    """Natijalarni natijalar.txt ga yozadi"""
    with open("natijalar.txt", "a", encoding="utf-8") as f:
        f.write(matn + "\n")


def juft_toq_ajratish():
    n = int(input(Fore.YELLOW + "Istalgan butun sonni kiriting: "))
    juftlar = []
    toqlar = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            juftlar.append(i)
        else:
            toqlar.append(i)

    natija = f"Juft sonlar: {juftlar}\nToq sonlar: {toqlar}"
    print(Fore.GREEN + natija)
    faylga_yoz("[Juft va Toq] " + natija)


def ism_yosh_xabar():
    ism = input(Fore.YELLOW + "Ismingizni kiriting: ")
    yosh = int(input(Fore.YELLOW + "Yoshingizni kiriting: "))

    hozirgi_sana = datetime.now().year
    tugilgan_yil = hozirgi_sana - yosh

    natija = f"Salom, {ism}! Siz {tugilgan_yil}-yilda tug‘ilgansiz"
    print(Fore.CYAN + natija)
    faylga_yoz("[Ism & T-yil] " + natija)


def uch_va_besh():
    sonlar = [str(i) for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
    natija = "3 va 5 ga bo‘linadigan sonlar: " + ", ".join(sonlar)
    print(Fore.MAGENTA + natija)
    faylga_yoz("[3 va 5] " + natija)


def chiqar_menyu():
    menyu = f"""
{Fore.BLUE}✨📋 {Style.BRIGHT}MENYU ✨
{Fore.BLUE}{'=' * 30}
{Fore.WHITE}1️⃣ Juft va toq sonlarni ajratish
2️⃣ Ism va yosh so‘rab xabar chiqarish
3️⃣ 1-100 orasida 3 va 5 ga bo‘linadigan sonlarni chiqarish
4️⃣ 🚪 Chiqish
{Fore.BLUE}{'=' * 30}
"""
    print(menyu)


def menyu():
    while True:
        chiqar_menyu()
        tanlov = input(Fore.YELLOW + "Tanlovingizni kiriting (1-4): ")

        if tanlov == '1':
            juft_toq_ajratish()
        elif tanlov == '2':
            ism_yosh_xabar()
        elif tanlov == '3':
            uch_va_besh()
        elif tanlov == '4':
            print(Fore.RED + "🚪 Dastur tugadi. Xayr!")
            break
        else:
            print(Fore.RED + "❌ Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")


if __name__ == "__main__":
    menyu()
