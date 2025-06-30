"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def hisobla():
    """
    Foydalanuvchiga belgilangan tug'ilgan kun sanasigacha (yoki undan o'tgan kunlar) haqida ma'lumot beradi.
    Funksiya quyidagilarni bajaradi:
    - Bugungi sanani va tug'ilgan kun sanasini chiqaradi.
    - Tug'ilgan kunigacha qolgan kunlar sonini hisoblaydi va chiqaradi.
    - Agar tug'ilgan kun hali kelmagan bo'lsa, qolgan oy va kunlarni hisoblab, har bir qolgan kun sanasini ketma-ket chiqaradi.
    - Agar bugun tug'ilgan kun bo'lsa, tabrik xabarini chiqaradi.
    - Agar tug'ilgan kun o'tib ketgan bo'lsa, necha kun oldin bo'lganini chiqaradi.
    Eslatma: Funksiya `datetime` va `timedelta` modullaridan foydalanadi.
    """
    t_kun = datetime.strptime(
        "06.07.2025", "%d.%m.%Y").date()  # 2025-yil 6-iyul
    bugun = datetime.now().date()
    qolgan_kunlar = (t_kun - bugun).days

    print(f"Bugun: {bugun.strftime('%d.%m.%Y')}")
    print(f"Tug'ilgan kuni: {t_kun.strftime('%d.%m.%Y')}")
    print(f"\nTug'ilgan kunigacha qolgan kunlar: {qolgan_kunlar}")

    # Faqat qolgan kunlarni chiqarish
    if qolgan_kunlar > 0:
        print(f"\nBu {qolgan_kunlar//30} oy va {qolgan_kunlar % 30} kun degani")
        print("Qolgan kunlar ketma-ketligi:")
        for i in range(1, qolgan_kunlar + 1):
            sana = bugun + timedelta(days=i)
            print(f"{i}. {sana.strftime('%d.%m.%Y')}")
    elif qolgan_kunlar == 0:
        print("\nBugun Olimning tug'ilgan kuni! 🎉🎉🎉")
    else:
        print(
            f"\nOlimning tug'ilgan kuni {abs(qolgan_kunlar)} kun oldin bo'lgan")


if __name__ == "__main__":
    hisobla()
