import random
from hangman.uzwords import words

def clean_words(word_list):
    """So'zlar ro'yxatini tozalaydi: bo'sh joyli yoki noto'g'ri belgilarni olib tashlaydi."""
    return [w.upper() for w in word_list if " " not in w and "_" not in w and w.isalpha()]

def get_random_word(cleaned_words):
    """Tozalangan ro'yxatdan bitta tasodifiy so'z tanlaydi."""
    return random.choice(cleaned_words)

def display_word(word, guessed_letters):
    """Kiritilgan harflarga ko'ra so'z holatini ko'rsatadi."""
    return ' '.join([l if l in guessed_letters else '_' for l in word])

def play_game(max_attempts=10):
    """O'yin jarayonini boshlovchi funksiya."""
    valid_words = clean_words(words)
    if not valid_words:
        print("So'zlar ro'yxatida yaroqli so'zlar topilmadi.")
        return

    word = get_random_word(valid_words)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 0

    print(f"Men {len(word)} xonali so'z o'yladim. Uni topa olasizmi? Sizda {max_attempts} urinish bor!")

    while word_letters and attempts < max_attempts:
        print("\nSo'z: ", display_word(word, guessed_letters))
        print("Kiritilgan harflar: ", ", ".join(sorted(guessed_letters)))

        guess = input("Harf kiriting: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Faqat 1 dona harf kiriting.")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' harfini allaqachon kiritgansiz.")
            continue

        guessed_letters.add(guess)
        attempts += 1

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"✅ To‘g‘ri! '{guess}' harfi mavjud.")
        else:
            print(f"❌ Afsus! '{guess}' harfi mavjud emas.")

    if not word_letters:
        print(f"\n🎉 Tabriklaymiz! Siz '{word}' so'zini {attempts} urinishda topdingiz!")
    else:
        print(f"\n😞 Yutqazdingiz! Bu so'z: '{word}'")
