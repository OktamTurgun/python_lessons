"""
09-dars: Python pathlib kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda pathlib kutubxonasi yordamida zamonaviy fayl va papka yo‘llari bilan ishlashni o‘rganamiz:
 - Path obyektlari yaratish
 - Fayl va papka mavjudligini tekshirish
 - Faylni o‘qish/yozish
 - Fayl nomi, kengaytmasi, ota katalogi bilan ishlash
"""

from pathlib import Path

# Path obyekt yaratish (nisbiy va to‘liq yo‘l)
path1 = Path("example.txt")
path2 = Path.home() / "Documents" / "data.txt"
print("Nisbiy path:", path1)
print("To‘liq path:", path2)

# Fayl va papkani tekshirish
print("Faylmi?", path1.is_file())
print("Papkami?", path1.is_dir())

# Fayl yaratish (agar mavjud bo‘lmasa)
if not path1.exists():
    path1.write_text("Salom, bu pathlib darsidir!")

# Faylni o‘qish
if path1.exists():
    matn = path1.read_text()
    print("Fayl mazmuni:", matn)
else:
    print(f"{path1} mavjud emas, o‘qib bo‘lmadi.")

# Fayl nomi, kengaytmasi, ota papkasi
print("Fayl nomi:", path1.name)
print("Kengaytmasi:", path1.suffix)
print("Ota papka:", path1.parent)

# Amaliy mashq: papka ichidagi barcha .txt fayllarni topish
docs = Path(".")
print(".txt fayllar:")
for fayl in docs.glob("*.txt"):
    print(fayl.name)

# Amaliy mashq: papka ichidagi barcha papkalarni topish
print("Papkalar:")
for papka in docs.iterdir():
    if papka.is_dir():
        print(papka.name)

# Amaliy mashq: fayl hajmini baytlarda chiqarish
if path1.exists():
    print("Fayl hajmi (baytlarda):", path1.stat().st_size)
else:
    print(f"{path1} mavjud emas, hajmi aniqlanmadi.")

# Amaliy mashq: faylni boshqa nom bilan ko‘chirish
yangi_path = Path("example_copy.txt")
if not yangi_path.exists():
    path1.replace(yangi_path)
    print(f"{path1.name} -> {yangi_path.name} ga ko‘chirildi")

# Amaliy mashq: papka ichidagi barcha fayllarni va papkalarni rekursiv chiqarish
print("Barcha fayl va papkalar (rekursiv):")
for p in docs.rglob("*"):
    print(p)
