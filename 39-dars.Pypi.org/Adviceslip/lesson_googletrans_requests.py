"""
📌 Mavzu: Python tashqi kutubxonasi. pypi.org
📦 Modul: requests
✍️ Muallif: Uktam Turgunov
📅 Sana: 2025-07-03

"""
import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()["slip"]["advice"]
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest="uz")
print(tarjima.text)
