"""
📌 Mavzu: Python tashqi kutubxonasi - `requests` + `googletrans`
📦 Modullar: requests, googletrans
✍️ Muallif: Uktam Turgunov
📅 Sana: 2025-07-03
🧠 Maqsad: API'dan maslahat (advice) olib, uni o‘zbek tiliga tarjima qilish
"""

import requests
from googletrans import Translator

# 1. API'dan maslahat (advice) olish
try:
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    response.raise_for_status()
    advice = response.json()["slip"]["advice"]
    print("🗣 English Advice:", advice)
except requests.exceptions.RequestException as e:
    print("❌ Maslahat olishda xatolik:", e)
    advice = None

# 2. Tarjima qilish (agar maslahat mavjud bo‘lsa)
if advice:
    try:
        translator = Translator()
        tarjima = translator.translate(advice, dest="uz")
        print("🔁 O‘zbekcha tarjima:", tarjima.text)
    except Exception as e:
        print("❌ Tarjima qilishda xatolik:", e)