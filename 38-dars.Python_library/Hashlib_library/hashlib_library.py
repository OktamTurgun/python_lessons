"""
13-dars: Python hashlib kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda hashlib kutubxonasi yordamida:
 - Ma’lumotlarni xeshlash (MD5, SHA256)
 - Parollarni xavfsiz saqlash
 - Faylni xeshlash
 - Xesh qiymatlarini taqqoslash
"""

import hashlib
import os

# Matnni md5 bilan xeshlash
matn = "salom123"
md5_xesh = hashlib.md5(matn.encode()).hexdigest()
print("MD5:", md5_xesh)

# Matnni sha256 bilan xeshlash
sha256_xesh = hashlib.sha256(matn.encode()).hexdigest()
print("SHA256:", sha256_xesh)

# Xesh qiymatlari uzunligi
print("MD5 uzunligi:", len(md5_xesh))      # 32
print("SHA256 uzunligi:", len(sha256_xesh))  # 64

# Parol tekshiruvchi funksiya
saqlangan_xesh = hashlib.sha256("admin123".encode()).hexdigest()

kiritilgan = input("Parolni kiriting: ")
kiritilgan_xesh = hashlib.sha256(kiritilgan.encode()).hexdigest()

if kiritilgan_xesh == saqlangan_xesh:
    print("✅ Parol to‘g‘ri")
else:
    print("❌ Noto‘g‘ri parol")

# Diqqat: xesh funksiyalari matnni qaytarib tiklay olmaydi!

# 1. Faylni xeshlash (SHA256)


def fayl_xesh_yasash(fayl_nomi):
    sha256 = hashlib.sha256()
    with open(fayl_nomi, "rb") as f:
        for qism in iter(lambda: f.read(4096), b""):
            sha256.update(qism)
    return sha256.hexdigest()

# 2. Xeshlarni taqqoslash (fayl o'zgarganini aniqlash)
# misol uchun: fayl_xesh_yasash("test.txt") == fayl_xesh_yasash("test_kopiya.txt")

# 3. Parollar uchun "salt" bilan xeshlash


def parol_xesh_salt(parol):
    salt = os.urandom(16)
    xesh = hashlib.pbkdf2_hmac('sha256', parol.encode(), salt, 100000)
    return salt.hex() + xesh.hex()


# 4. Xesh algoritmlarini ko‘rish
print("Hashlib algoritmlari:", hashlib.algorithms_available)

# 5. Foydalanuvchi kiritgan matnni tanlangan algoritm bilan xeshlash


def xeshla(matn, algoritm):
    h = hashlib.new(algoritm)
    h.update(matn.encode())
    return h.hexdigest()

# Misol: print(xeshla("salom", "sha1"))
