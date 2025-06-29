"""
15-dars: Python shutil kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda shutil kutubxonasi yordamida:
 - Faylni nusxalash (copy, copy2)
 - Faylni ko‘chirish (move)
 - Fayl yoki papkani o‘chirish (remove, rmtree)
 - Arxivlash
 - Amaliy mashqlar: backup nusxa olish, faylni arxivlash, faylni ko‘chirib qayta tiklash
"""

import shutil
import os

# Fayl nusxalash (oddiy)
shutil.copy("data.txt", "data_backup.txt")
print("✅ data.txt nusxalandi")

# Faylni to‘liq metadata bilan nusxalash
shutil.copy2("data.txt", "data_full_backup.txt")
print("✅ data.txt metadata bilan nusxalandi")

# Faylni ko‘chirish
shutil.move("data_backup.txt", "backup/data_backup.txt")
print("✅ Fayl backup/ papkaga ko‘chirildi")

# Faylni o‘chirish
if os.path.exists("data_full_backup.txt"):
    os.remove("data_full_backup.txt")
    print("🗑️ data_full_backup.txt o‘chirildi")

# Papkani rekurisv o‘chirish
if os.path.exists("backup"):
    shutil.rmtree("backup")
    print("🗑️ backup/ papkasi to‘liq o‘chirildi")

# Amaliy mashq: Arxiv yaratish
shutil.make_archive("my_backup", "zip", "data_folder")
print("📦 Arxiv yaratildi: my_backup.zip")

# Amaliy mashq 2: Yangi papka yaratib, ichiga fayl ko‘chirish
if not os.path.exists("archive_folder"):
    os.mkdir("archive_folder")
shutil.copy("data.txt", "archive_folder/data_copy.txt")
print("📁 data.txt archive_folder ichiga ko‘chirildi")

# Amaliy mashq 3: Faylni zaxiralab, asl nusxasini o‘chirib, keyin qayta tiklash
shutil.copy("data.txt", "temp_backup.txt")
os.remove("data.txt")
print("🧹 data.txt vaqtincha o‘chirildi")
shutil.copy("temp_backup.txt", "data.txt")
os.remove("temp_backup.txt")
print("♻️ data.txt tiklandi")
