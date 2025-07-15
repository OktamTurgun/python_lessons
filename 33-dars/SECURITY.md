🛡️ Pickle bilan ishlashda xavfsizlik bo‘yicha yo‘riqnoma

🎯 Maqsad

Ushbu hujjat Python'da pickle moduli yordamida obyektlarni faylga saqlash va o‘qish jarayonida yuzaga keladigan xavflar (xususan, "arbitrary code execution")dan qanday himoyalanish kerakligini tushuntiradi.

⚠️ Xavf: Arbitrary Code Execution

pickle.load() fayldan obyektni "deserializatsiya" qiladi. Agar bu fayl yomon niyatli kodni o‘z ichiga olsa, kompyuteringizda avtomatik tarzda zararli kod ishlashi mumkin.

❌ Misol: Zararli kodni pickle ichiga yashirish

import os
class Hacker:
    def __reduce__(self):
        return (os.system, ('echo HACKED!',))

Yuqoridagi klass pickle.load() orqali ishga tushirilsa, foydalanuvchi bilmagan holda echo HACKED! bajartiriladi.

✅ Xavfsizlik bo‘yicha qoidalar

1. Faqat ishonchli manbadan pickle fayl oching

O‘zingiz yaratgan fayllar ✅

Jamoa a’zolari bilan almashilgan, ishonchli fayllar ✅

Internetdan yuklangan, noma’lum fayllar ❌

2. Fayl nomini va mavjudligini tekshiring

import os
if not os.path.exists(filename):
    raise FileNotFoundError("Fayl mavjud emas.")

3. json, csv, yoki sqlite3 kabi xavfsiz alternativalardan foydalaning

import json
with open("data.json", "w") as f:
    json.dump({"ism": "Uktam", "yosh": 34}, f)

4. Maxsus funksiya orqali pickle o‘qishni cheklang

def safe_pickle_load(filename):
    if not filename.endswith(".pkl"):
        raise ValueError("Noto‘g‘ri fayl turi!")
    with open(filename, "rb") as f:
        return pickle.load(f)

5. Fayllarni alohida katalogda saqlang

data/ yoki storage/ kabi papkalar oching

Har doim shu joyga yozing va o‘qing

6. Kerak bo‘lsa — cryptography moduli bilan shifrlang

from cryptography.fernet import Fernet
import pickle

key = Fernet.generate_key()
f = Fernet(key)

# Saqlash
with open("xavfsiz.pkl", "wb") as file:
    encrypted = f.encrypt(pickle.dumps(obj))
    file.write(encrypted)

# O‘qish
with open("xavfsiz.pkl", "rb") as file:
    data = file.read()
    obj = pickle.loads(f.decrypt(data))

🔚 Yakuniy tavsiyalar

Amaliyot

Tavsiya

Internetdan kelgan .pkl faylni load() qilish

❌ Yo‘q

O‘zingiz yozgan .pkl faylni load() qilish

✅ Ha

Faqat ma’lumot saqlash kerak bo‘lsa

json yoki csv ishlating

Kompyuter xavfsizligini ta’minlash kerak bo‘lsa

cryptography bilan shifrlang