"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-01
Mavzu: fuzzywuzzy moduli

"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words
import difflib

# ikki so'z 'ortasida o'xshashlik foizini topish
print(fuzz.ratio("salom", 'assalom'))
print(fuzz.ratio("salom", "salim"))

# Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
text = "salom"
matches = process.extract(text, words, limit=3)
print(matches)

# # Matnlar orasidan eng o'xshashini topish
text = "talba"
match = process.extractOne(text, words)
print(match)

# 1. Oddiy matnlarni solishtirish
print(fuzz.ratio("salom", "Salom"))              # 83 (case farqi bor)
print(fuzz.ratio("salom", "salomlar"))          # 86
print(fuzz.partial_ratio("salom", "salomlar"))  # 100 (qisman moslik)

# 2. Tartibsiz matnlarni solishtirish

fuzz.token_sort_ratio("salom dunyo", "dunyo salom")
# 100 (tartibni e’tiborga olmaydi)

# 3. Qisman moslik

fuzz.partial_ratio("hello world", "hello")

# 4. Eng yaqin moslikni topish

names = ["Ali", "Vali", "Sami", "Salim"]
result = process.extractOne("Sali", names)
print(result)   # ('Salim', 80)

# 5. Foydalanuvchi kiritgan ismni bazadagi ismlar bilan solishtirish
user_input = "Valy"
closest_match = process.extractOne(user_input, names)
print(
    f"Foydalanuvchi kiritgan ism: {user_input}, eng yaqin moslik: {closest_match}")

# 6. Duplikatlarni aniqlash
duplicates = process.extract("Ali", ["Ali", "Ali", "Vali", "Sami"], limit=2)
print(f"Duplikatlar: {duplicates}")

# 7. Fuzzy qidiruv: matndan so'zlarni topish
search_word = "dunoy"
sentence = ["salom", "dunyo", "hayr", "olam"]
best_match = process.extractOne(search_word, sentence)
print(f"Qidiruv natijasi: {best_match}")

# 8. Standart kutubxona bilan solishtirish (difflib)
similar = difflib.get_close_matches("salom", words, n=3)
print(f"difflib natijasi: {similar}")
'''
✅ extractOne() — eng yaqin bitta moslikni qaytaradi.
✅ extract() — bir nechta eng yaqinlarini topib beradi.

📌 Qachon kerak bo‘ladi?
Imlosi xato bo‘lishi mumkin bo‘lgan matnlarni solishtirishda

Foydalanuvchi kiritgan ismni bazadagi ismlar bilan solishtirishda

Yozuvlarda duplikatlarni aniqlashda

Qidiruv tizimlarida “fuzzy” qidiruvda

🪄 Maslahat
python-Levenshtein kutubxonasini ham o‘rnatsangiz, FuzzyWuzzy 10 barobar tezroq ishlaydi.

🔗 Alternativalar
rapidfuzz — juda tez va zamonaviy alternativ.

difflib (standart kutubxona)
'''
