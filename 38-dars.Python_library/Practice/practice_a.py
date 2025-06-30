"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
"""


from datetime import datetime, date, time, timedelta
import datetime as dt


# Exercise: 1


def chiqar_sanalar():
    bugun = dt.datetime.now().date()
    print("Bugungi sana:", bugun.strftime("%d-%m-%Y"))
    print("Keyingi 10 ta sana (2 xafta farq bilan):")

    for i in range(1, 11):
        sana = bugun + timedelta(weeks=2*i)
        print(f"{i}. {sana.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
    chiqar_sanalar()
