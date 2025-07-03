"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-03
Mavzu: Googletrans moduli
"""
from googletrans import Translator

tarjimon = Translator()

msg = "Tarjima uchun so'z kiriting (chiqish uuchun 'q' deb yozing): "
while True:
    text = input(msg)
    if text == "q":
        print("Dastur tugadi!")
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)

'''
msg = 'Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)
'''
