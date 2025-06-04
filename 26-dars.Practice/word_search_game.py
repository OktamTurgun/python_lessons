"""
So'z topish o'yini (Hangman) - O'zbek tilidagi so'zlardan iborat interaktiv o'yin.

Ushbu dastur foydalanuvchidan harflarni kiritishni so'raydi va foydalanuvchi
tasodifiy tanlangan so'zni topishga harakat qiladi. Foydalanuvchining har bir
urinishlari soni hisoblanadi va maksimal 10 martagacha ruxsat beriladi.

Fayl tarkibi:
- get_words(): So'zlar ro'yxatini uzwords_latin.py faylidan olish.
- play_game(): Asosiy o'yin funksiyasi. Foydalanuvchi bilan o'zaro aloqani boshqaradi.

Eslatma:
`uzwords.py` faylida `words` degan o'zbek so'zlarining ro'yxati bo'lishi kerak.

Muallif: [Uktam Turgunov]
Sana: [2025-06-04]
"""

import random
from uzwords import words


def get_words():
    """
    So'zlar ro'yxatini uzwords_latin modulidan olishga harakat qiladi.

    Returns:
        list: Agar modul topilsa, so'zlar ro'yxati qaytariladi.
              Aks holda, bo'sh ro'yxat [] qaytariladi va ogohlantirish chiqariladi.
    """
    try:
        from uzwords import words

        return words
    except ImportError:
        print(
            "uzwords.py fayli topilmadi! Iltimos, faylni dastur bilan bir papkaga joylang."
        )
        return []


def play_game():
    """
    So'z topish o'yinini boshlaydi.

    O'yin jarayonida:
    - Tasodifiy so'z tanlanadi.
    - Foydalanuvchi harflarni birma-bir kiritadi.
    - Harf to'g'ri bo'lsa, ochiladi; aks holda urinishlar soni oshadi.
    - O'yin foydalanuvchi to'g'ri topgunga qadar yoki maksimal urinish (20) tugaguncha davom etadi.
    - O'yin tugagach, foydalanuvchidan yana o'ynashni xohlaysizmi deb so'raladi.
    """
    words = get_words()
    if not words:
        return

    # Tasodifiy so'z tanlaymiz
    secret_word = random.choice(words).upper()
    guessed_letters = set()  # Foydalanuvchi kiritgan harflar
    correct_letters = set()  # To'g'ri topilgan harflar
    attempts = 0
    max_attempts = 20

    print("So'z topish o'yiniga xush kelibsiz!")
    print(f"Men {len(secret_word)} harfli so'z o'yladim. Topishga harakat qiling!")

    while True:
        # So'zni yashirin shaklda ko'rsatamiz
        display_word = ""
        for letter in secret_word:
            if letter in correct_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\n" + display_word.strip())

        # Agar barcha harflar topilgan bo'lsa
        if all(letter in correct_letters for letter in secret_word):
            print(f"\nTabriklayman! Siz so'zni topdingiz: {secret_word}")
            print(f"Urinishlar soni: {attempts}")
            break

        # Agar urinishlar tugasa
        if attempts >= max_attempts:
            print(f"\nAfsuski yutqazdingiz. To'g'ri so'z: {secret_word}")
            break

        # Foydalanuvchi kiritgan harflarni ko'rsatamiz
        if guessed_letters:
            print("Siz kiritgan harflar:", ", ".join(sorted(guessed_letters)))

        # Foydalanuvchidan harf soraymiz
        guess = input("Harif kiriting: ").upper()

        # Kiritilgan ma'lumotni tekshiramiz
        if len(guess) != 1 or not guess.isalpha():
            print("Iltimos, faqat bitta harf kiriting!")
            continue

        # Agar bu harf avval kiritilgan bo'lsa, ogohlantiradi
        if guess in guessed_letters:
            print(f"Siz '{guess}' harfini oldin kiritgansiz!")
            continue

        guessed_letters.add(guess)
        attempts += 1

        # Harf so'zda bormi?
        if guess in secret_word:
            correct_letters.add(guess)
            print(f"To'g'ri! '{guess}' harfi so'zda bor.")
        else:
            print(f"Afsuski, '{guess}' harfi so'zda yo'q.")

    # Yana o'ynashni so'raymiz
    play_again = input("\nYana o'ynashni xohlaysizmi? (ha/yo'q): ").lower()
    if play_again == "ha":
        play_game()
    else:
        print("O'yin uchun rahmat!")


if __name__ == "__main__":
    play_game()
