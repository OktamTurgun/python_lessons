"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 

Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring

Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing

Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring

Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:

"""


from datetime import datetime, date, time, timedelta
import datetime as dt


def chiqar_sanalar():
    bugun = dt.datetime.now().date()
    print("Bugungi sana:", bugun.strftime("%d-%m-%Y"))
    print("Keyingi 10 ta sana (2 xafta farq bilan):")

    for i in range(1, 11):
        sana = bugun + timedelta(weeks=2*i)
        print(f"{i}. {sana.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
    chiqar_sanalar()
