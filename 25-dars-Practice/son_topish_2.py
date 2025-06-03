"""
Yaxshilangan jihatlar:

Kod qayta ishlatilishi mumkin bo'ldi

Har bir funksiya aniq bir vazifani bajaradi

Xato holatlari yaxshiroq qo'llab-quvvatlanadi

Binary search algoritmi bilan tezroq topish

Kod tuzilishi aniqroq va tushunarli bo'ldi

Konstanta qiymatlar alohida belgilandi
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def get_valid_input(prompt, input_type=int, valid_range=None):
    """Foydalanuvchi kiritishini tekshiradi
    Args:
        prompt (str): Foydalanuvchidan kiritishni so'rash matni
        input_type (type): Kiritish turini belgilaydi (int, str va h.k.)
        valid_range (tuple): Ixtiyoriy, kiritiladigan sonning ruxsat etilgan oralig'i
    Returns:
        user_input (int/str): Foydalanuvchi kiritgan to'g'ri formatdagi qiymat
    """
    while True:
        try:
            user_input = input_type(input(prompt))  # Foydalanuvchi kiritishini olish
            if valid_range and (
                user_input < valid_range[0] or user_input > valid_range[1]
            ):  # Kiritilgan qiymatni tekshirish
                print(
                    f"Iltimos {valid_range[0]}-{valid_range[1]} oralig'ida son kiriting."
                )
                continue
            return user_input
        except ValueError:
            print("Noto'g'ri kiritish! Iltimos to'g'ri formatda kiriting.")


def user_guess():
    """Foydalanuvchi kompyuter sonini topadi
    Returns:
        attempts (int): Foydalanuvchining sonni topish uchun sarflagan urinishlari soni
    """
    komp_son = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    print(
        f"\nKompyuter {MIN_NUMBER}-{MAX_NUMBER} oralig'ida son o'yladi. Topishga harakat qiling!"
    )

    while True:
        attempts += 1
        user_input = get_valid_input(
            f"{attempts}-urinish. Taxminingiz: ", valid_range=(MIN_NUMBER, MAX_NUMBER)
        )

        if user_input == komp_son:
            print(f"Tabriklayman! Siz {attempts} urunishda topdingiz!")
            return attempts
        print(
            f"Xato! Men o'ylagan son {'kattaroq' if user_input < komp_son else 'kichikroq'}."
        )


def comp_guess():
    """Kompyuter foydalanuvchi sonini topadi
    Returns:
        attempts (int): Kompyuterning sonni topish uchun sarflagan urinishlari soni
    """
    print(f"\nEndi siz {MIN_NUMBER}-{MAX_NUMBER} oralig'ida son o'ylang (kiritmang).")
    input("O'ylab bo'lganingizdan so'ng Enter ni bosing...")
    attempts = 0
    low, high = MIN_NUMBER, MAX_NUMBER

    while True:
        attempts += 1
        guess = (
            low + high
        ) // 2  # Binary search algoritmi, o'rtadagi sonni taxmin qilish va tezroq topish
        print(f"\n{attempts}-urinish. Kompyuter taxmini: {guess}")

        response = get_valid_input(
            "To'g'ri (t), kattaroq (k), kichikroq (kich)? ",
            input_type=str,
            valid_range=None,
        ).lower()

        if response == "t":
            print(f"Kompyuter {attempts} urunishda topdi!")
            return attempts
        elif response == "k":
            low = guess + 1
        else:
            high = guess - 1


def play_round():
    """Bitta o'yin raundini o'ynaydi
    Returns:
        winner (str): Raund g'olibi ('user', 'comp' yoki 'draw')
    """
    print("\n=== YANGI RAUND ===")

    print("\n[Foydalanuvchi topish bosqichi]")
    user_attempt = user_guess()

    print("\n[Kompyuter topish bosqichi]")
    comp_attempt = comp_guess()

    if user_attempt < comp_attempt:
        result = ("Siz yutdingiz!", "user")
    elif comp_attempt < user_attempt:
        result = ("Kompyuter yutdi!", "comp")
    else:
        result = ("Durrang!", "draw")

    print(f"\n{result[0]} (Siz: {user_attempt}, Kompyuter: {comp_attempt})")
    return result[1]


def play_game():
    """Asosiy o'yin funksiyasi
    Bu funksiya foydalanuvchi va kompyuter o'rtasida bir nechta raundlarni o'ynaydi
    """
    scores = {"user": 0, "comp": 0, "draw": 0}

    print(
        f"""
    Son topish o'yiniga xush kelibsiz!
    Har bir raundda:
    1. Kompyuter {MIN_NUMBER}-{MAX_NUMBER} oralig'ida son o'ylaydi, siz topasiz
    2. Siz son o'ylaysiz, kompyuter topadi
    """
    )

    while True:
        winner = play_round()
        scores[winner] += 1

        if (
            get_valid_input(
                "\nYana o'ynashni xohlaysizmi? (ha/yo'q): ", input_type=str
            ).lower()
            != "ha"
        ):
            break

    print(
        f"""
    \n=== O'YIN YAKUNLANDI ===
    Sizning g'alabalar: {scores['user']}
    Kompyuter g'alabalar: {scores['comp']}
    Durranglar: {scores['draw']}
    """
    )

    if scores["user"] > scores["comp"]:
        print("Yakuniy natija: Siz yutdingiz! 🎉")
    elif scores["comp"] > scores["user"]:
        print("Yakuniy natija: Kompyuter yutdi! 💻")
    else:
        print("Yakuniy natija: Durrang! 🤝")


if __name__ == "__main__":
    play_game()
