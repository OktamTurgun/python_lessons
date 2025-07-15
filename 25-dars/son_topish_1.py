"""
Created on Tue Jun 3 11:00:14 2025

25-dars "Son topish o'yini" (Part 1)

@author: uktam
"""

import random


def user_guess():
    """
    Foydalanuvchi 1 dan 10 gacha son o'ylaydi va topishga urunadi.
    Returns:
        attempts (int): Foydalanuvchining sonni topish uchun sarflagan urinishlari soni
    """
    komp_son = random.randint(1, 10)
    attempts = 0
    while True:
        attempts += 1
        try:
            user_input = int(input("1 dan 10 gacha son o'yladim topa olasizmi? "))
            if user_input < 1 or user_input > 10:
                print("Iltimos 1 dan 10 gacha son kiriting.")
                continue

            if user_input == komp_son:
                print(f"Tabriklayman! Siz {attempts} urunishda topdingiz!")
                return attempts
            elif user_input < komp_son:
                print("Xato! Men o'ylagan son kattaroq. Yana urinib ko'ring.")
            else:
                print("Xato! Men o'ylagan son kichikroq. Yana urinib ko'ring.")
        except ValueError:
            print("Iltimos faqat son kiriting! (1-10)")


def comp_guess():
    """
    Kompyuter foydalanuvchi o'ylagan sonni topishga urunadi.
    Returns:
        attempts (int): Kompyuterning sonni topish uchun sarflagan urinishlari soni
    """
    print("\nEndi siz 1 dan 10 oralig'ida son o'ylang (Lekin kiritmang!).")
    input("O'ylab bolganingizdan keyin Enter tugmasini bosing...")
    attempts = 0
    low = 1
    high = 10

    while True:
        attempts += 1
        if low == high:
            guess = low
        else:
            guess = random.randint(low, high)
        print(f"Siz {guess} sonni o'yladingiz:")
        javob = input("To'g'ri (t), kattaroq (k), kichikroq (kich)? ").lower()

        if javob == "t":
            print(f"Computer {attempts} urunishda topdi!")
            return attempts
        elif javob == "k":
            low = guess + 1
        elif javob == "kich":
            high = guess - 1
        else:
            print("Noto'g'ri javob! Iltimos, 't', 'k', 'kich' kiriting.")
            attempts -= 1


def play_game():
    """
    O'yin jarayonini boshqaruvchi funksiya.
    Foydalanuvchi va kompyuter o'rtasida son topish o'yinini o'tkazadi.
    """
    user_wins = 0
    comp_wins = 0
    while True:
        print("\n=== YANGI RAUND! ===")

        print("\nFoydalanuvchi topish bosqichi")
        user_attempt = user_guess()

        print("\nComputer topish bosqichi")
        comp_attempt = comp_guess()

        if user_attempt < comp_attempt:
            print(
                f"Siz bu raundda yutdingiz! (Siz: {user_attempt}, Computer: {comp_attempt})"
            )
            user_wins += 1
        elif comp_attempt < user_attempt:
            print(
                f"Computer bu raundda yutdi! (Siz: {user_attempt}, Computer: {comp_attempt})"
            )
            comp_wins += 1
        else:
            print(
                f"Bu raund durrang! (Ikkalamiz xam {user_attempt} urunishda topdingiz)"
            )

        # Yana o'ynashni so'rash
        while True:
            davom_et = input("\nYana o'ynashni xoxlaysizmi? (ha/yo'q)")
            if davom_et in ["ha", "yo'q", "1", "0"]:
                break
            print("Iltimos, 'ha' yoki 'yo'q' javobini kiriting!")

        if davom_et != "ha":
            break

    # Yakuniy natijalar
    print(
        f"\n=== O'YIN YAKUNLANDI ===" f"\nUser: {user_wins}" f"\nComputer: {comp_wins}"
    )
    if user_wins > comp_wins:
        print("Yakuniy natija: Siz yutdingiz! 🎉")
    elif comp_wins > user_wins:
        print("Yakuniy natija: Computer yutdi! 💻")
    else:
        print("Yakuniy natija: Durrang! 🤝")


# O'yinni boshlash
print(
    "\nSon topish o'yiniga xush kelibsiz!"
    "\nHar bir raundda: \n1-Kompyuter son o'ylaydi siz topasiz"
    "\n2-Siz son o'ylaysiz kompyuter topadi"
)

play_game()
