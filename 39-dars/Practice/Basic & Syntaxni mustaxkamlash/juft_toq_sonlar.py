"""
Mavzu: Practice. Basic & Syntaxni mustaxkamlash
Muallif: Uktam Turgunov
Sana: 2025-07-06
Vazifa:
Juft va toq sonlarni ajratish.
Foydalanuvchidan N sonini oling. 1 dan N gacha bo‘lgan sonlarni juft va toq bo‘lib ajrating va ikkala ro‘yxatni chiqarib bering.
"""
n = int(input("Istalgan son kiriting: "))

juft_sonlar = []
toq_sonlar = []

for i in range(1, n+1):
    if i % 2 == 0:
        juft_sonlar.append(i)
    else:
        toq_sonlar.append(i)

print(f"Juft sonlar: {juft_sonlar}")
print(f"Toq sonlar: {toq_sonlar}")
