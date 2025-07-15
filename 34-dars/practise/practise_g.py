"""Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python
"""
import json
import os
print("Ishga tushgan katalog:", os.getcwd())
# JSON faylini o'qish
# with open('C:/Users/User/Documents/GitHub/python_lessons/python_lessons/34-dars.JSON/data/python_wikipedia.json', 'r', encoding='utf-8') as file:
#     python_data = json.load(file)

# Fayl yo‘lini dinamik aniqlash (absolyut yo'l yasaymiz)
base_dir = os.path.dirname(__file__)  # practise_g.py joylashgan papka
file_path = os.path.join(base_dir, '..', 'data', 'python_wikipedia.json')
file_path = os.path.abspath(file_path)  # Absolyut yo‘lga aylantiramiz

print("Ochilishi kerak bo‘lgan fayl yo‘li:", file_path)

with open(file_path, 'r', encoding='utf-8') as file:
    python_data = json.load(file)

# Ma'lumotlarni chiqarish (Wikipedia API strukturasi bo'yicha)
pages = python_data['query']['pages']
page_id = list(pages.keys())[0]  # Birinchi sahifa ID sini olamiz
page_data = pages[page_id]

print(f"Sarlavha: {page_data['title']}")
print(f"Info: {page_data['extract']}")
print(page_data)

# Exercise: 2
# with open("C:/Users/User/Documents/GitHub/python_lessons/python_lessons/34-dars.JSON/data/python_wikipedia.json") as f:
#     data = json.load(f)

# print(data["query"]["pages"]["13801"]["title"])
# print(data["query"]["pages"]["13801"]["extract"])
