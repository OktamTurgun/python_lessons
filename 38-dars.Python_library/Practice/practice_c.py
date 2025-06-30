"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import datetime as dt


def hisobla_kun():
    """
    Hisobla_kun funksiyasi foydalanuvchining tug'ilgan sanasidan boshlab bugungi kungacha qancha yil, oy va kun o'tganini hisoblaydi va natijani ekranga chiqaradi.
    Foydalanilgan kutubxonalar:
    - datetime: Sana va vaqt bilan ishlash uchun.
    - dateutil.relativedelta: Sana farqini yil, oy va kunlarda hisoblash uchun.
    Natija:
    - Bugungi sana va tug'ilgan sana ekranga chiqariladi.
    - Tug'ilgan kundan boshlab o'tgan yil, oy va kunlar soni ko'rsatiladi.
    - Agar tug'ilgan sana kelajakda bo'lsa, mos xabar chiqariladi.
    """
    t_kun = dt.datetime.strptime("13.03.1990", "%d.%m.%Y").date()
    bugun = datetime.now().date()
    otgan_vaqt = (bugun - t_kun).days

    print(f"Bugungi sana: {bugun.strftime("%d.%m.%Y")}")
    print(f"Tug'ilgan kunim: {t_kun.strftime("%d.%m.%Y")}")

    if otgan_vaqt > 0:
        farq = relativedelta(bugun, t_kun)
        print(
            f"Tug'ilgan kuningizdan shu kungacha: {farq.years} yil, {farq.months} oy, {farq.days} kun o'tdi")
    else:
        print("Tug'ilgan kuningiz kelajakda!")


if __name__ == "__main__":
    hisobla_kun()
