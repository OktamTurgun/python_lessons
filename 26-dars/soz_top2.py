import random
from uzwords import words


def get_random_word():
    """So‘zlar bazasidan tasodifiy so‘z olish."""
    return random.choice(words).upper()


def show_hint(secret_word, correct_letters):
    """Yashirin so‘zni ko‘rsatish."""
    return " ".join(
        [letter if letter in correct_letters else "_" for letter in secret_word]
    )


def is_game_won(secret_word, correct_letters):
    """G‘alaba shartini tekshirish."""
    return all(letter in correct_letters for letter in secret_word)


def get_user_guess(guessed_letters):
    """Foydalanuvchidan to‘g‘ri harf olish."""
    while True:
        guess = input("Harif kiriting: ").upper()

        if len(guess) != 1:
            print("Iltimos, faqat **1 ta harf** kiriting!")
            continue

        if not guess.isalpha():
            print("Faqat harflardan foydalaning!")
            continue

        if guess in guessed_letters:
            print(f"Siz '{guess}' ni oldin kiritgansiz!")
            continue

        return guess


def play_game():
    """Asosiy o‘yin funksiyasi."""
    secret_word = get_random_word()
    game = {
        "secret_word": secret_word,
        "guessed_letters": set(),
        "correct_letters": set(),
        "attempts": 0,
        "max_attempts": 20,
    }

    print("So‘z topish o‘yiniga xush kelibsiz!")
    print(f"Men {len(secret_word)} harfli so‘z o‘yladim. Topa olasizmi?")

    while True:
        print("\n" + show_hint(game["secret_word"], game["correct_letters"]))
        print(f"Urinishlar: {game['attempts']}/{game['max_attempts']}")

        # FOYDALANUVCHI KIRITGAN HARFLARNI KO'RSATISH
        if game["guessed_letters"]:
            print("\nKiritilgan harflar:", ", ".join(sorted(game["guessed_letters"])))

        if is_game_won(game["secret_word"], game["correct_letters"]):
            print(
                f"\n🎉 Tabriklayman! Siz {game['secret_word']} so‘zini {game['attempts']} urinishda topdingiz!"
            )
            break

        if game["attempts"] >= game["max_attempts"]:
            print(f"\n😢 Afsus! To‘g‘ri javob: {game['secret_word']}")
            break

        guess = get_user_guess(game["guessed_letters"])
        game["guessed_letters"].add(guess)
        game["attempts"] += 1

        if guess in game["secret_word"]:
            game["correct_letters"].add(guess)
            print(f"✅ '{guess}' to‘g‘ri!")
        else:
            print(f"❌ '{guess}' xato!")

    play_again = input("\nYana o‘ynashni xohlaysizmi? (ha/yo‘q): ").lower()
    if play_again == "ha":
        play_game()
    else:
        print("O‘yin uchun rahmat!")


if __name__ == "__main__":
    play_game()
