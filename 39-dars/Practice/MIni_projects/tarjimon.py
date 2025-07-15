"""
Mavzu: Inglizcha-O'zbekcha lug'at dasturi
Muallif: Uktam Turgunov
Sana: 2025-07-10
"""

import json
import os

DEFAULT_SOZLAR = {
    "apple": "olma",
    "book": "kitob",
    "car": "mashina",
    "dog": "it"
}


def load_sozlar(filename="sozlar.json"):
    """Lug'atni JSON fayldan yoki standart qiymatlardan yuklaydi"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_SOZLAR.copy()


def save_sozlar(sozlar, filename="sozlar.json"):
    """Lug'atni JSON faylga saqlaydi"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(sozlar, f, ensure_ascii=False, indent=2)


def lugat():
    """Asosiy lug'at dasturi"""
    sozlar = load_sozlar()

    print("📖 Inglizcha-O'zbekcha lug'at dasturi")
    print("-------------------------------------")

    while True:
        word = input("So'z kiriting (chiqish uchun 'exit'): ").strip().lower()

        if word in ('exit', 'quit', 'stop'):
            print("Dastur to'xtatildi!")
            break

        if not word:
            print("⚠️ Iltimos, so'z kiriting!")
            continue

        if word in sozlar:
            print(f"✅ {word} → {sozlar[word]}")
        else:
            print("🚫 Bu so'z lug'atda yo'q")
            if input("Lug'atga qo'shilsinmi? (ha/yo'q): ").lower() == 'ha':
                tarjima = input(f"{word} ning tarjimasini kiriting: ")
                sozlar[word] = tarjima
                save_sozlar(sozlar)
                print(f"➕ '{word}' lug'atga qo'shildi")


if __name__ == "__main__":
    lugat()
