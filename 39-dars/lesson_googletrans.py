"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-01
Mavzu: Googletrans moduli

Ushbu darsda biz Python dasturlash tilida tashqi kutubxonalarni, xususan, matnlarni avtomatik tarjima qilish uchun ishlatiladigan googletrans modulini o‘rganamiz. Googletrans — bu Google Translate API’sidan foydalanib, matnlarni turli tillarga tarjima qilish imkonini beruvchi bepul Python kutubxonasi hisoblanadi. Dars davomida modulni o‘rnatish, undan foydalanish va asosiy funksiyalarini amaliy misollar orqali ko‘rib chiqamiz.

"""
# 1. Googletrans modulini o'rnatish:
# Terminal yoki cmd oynasida quyidagini yozing:
# pip install googletrans==4.0.0-rc1

# 2. Modulni chaqirish va tarjimon obyektini yaratish

# Tarjimon obyektini yaratamiz
from googletrans import Translator

translator = Translator()

# 3. Matnni avtomatik aniqlash va ingliz tiliga tarjima qilish
# Exercise: 1
# matn_uz = "Salom, dunyo!"
# tarjima = translator.translate(matn_uz, dest='en')
# print(f"Original: {matn_uz}")
# print(f"Ingliz tiliga tarjimasi: {tarjima.text}")

# Ecercise: 2
matn_uz1 = "Python - dunyodagi eng mashxur dasturlash tili"
tarjimasi = translator.translate(matn_uz1, dest='en')
print(f"Original: {matn_uz1}")
print(f"Ingliz tiliga tarjimasi: {tarjimasi.text}")
print(f"Matnni asl tilini aniqlash: {tarjimasi.src}")

# 4. Matnni rus tiliga tarjima qilish
# Misol 1: Ingliz tilidan rus tiliga tarjima
matn_en = "How are you?"
tarjima_ru = translator.translate(matn_en, dest='ru')
print(f"Original: {matn_en}")
print(f"Rus tiliga tarjimasi: {tarjima_ru.text}")

# Misol 2: O'zbek tilidan rus tiliga tarjima
tarjima_ru2 = translator.translate(matn_uz1, dest='ru')
print(f"Original: {matn_uz1}")
print(f"Matn rus tilida: {tarjima_ru2.text}")

# 5. Matnning asl tilini aniqlash
aniqlangan_til = translator.detect(matn_uz1)
print(f"'{matn_uz1}' matnining aniqlangan tili: {aniqlangan_til.lang}")

# 6. Bir nechta matnlarni bir vaqtning o'zida tarjima qilish
matnlar = ["Hello", "Good morning", "How are you?"]
tarjimalar = translator.translate(matnlar, dest='uz')
for original, tarjima in zip(matnlar, tarjimalar):
    print(f"{original} -> {tarjima.text}")

# Eslatma: Bu workaround har doim ham to'liq ishlamasligi mumkin, lekin ba'zi hollarda yordam beradi.
# Eslatma: Googletrans bepul va norasmiy API bo'lgani uchun ba'zan ishlamasligi yoki xatoliklar bo'lishi mumkin.

# --- Qo'shimcha misollar ---

# # 7. Tarjima natijasining to'liq ma'lumotlarini ko'rish
# matn = "Python is a great programming language."
# tarjima_info = translator.translate(matn, dest='uz')
# print("To'liq tarjima ma'lumotlari:", tarjima_info)

# # 8. Matnni fransuz tiliga tarjima qilish
# matn2 = "Good luck!"
# tarjima_fr = translator.translate(matn2, dest='fr')
# print(f"{matn2} -> Fransuz tilida: {tarjima_fr.text}")

# # 9. Matnni avtomatik aniqlangan tilga tarjima qilish (dest tilini ko'rsatmasdan)
# matn3 = "Bu bir test matni."
# tarjima_auto = translator.translate(matn3)
# print(f"Avtomatik tarjima: {tarjima_auto.text}")

# # 10. Tarjima natijasidan til kodini va ismini olish
# matn4 = "I love programming."
# tarjima4 = translator.translate(matn4, dest='es')
# print(f"'{matn4}' ispan tilida: {tarjima4.text}, til kodi: {tarjima4.dest}")

# # 11. Tarjima qilishda manba tilini aniq ko'rsatish
# matn5 = "Bonjour tout le monde"
# tarjima5 = translator.translate(matn5, src='fr', dest='uz')
# print(f"Fransuz tilidan o'zbek tiliga: {tarjima5.text}")
