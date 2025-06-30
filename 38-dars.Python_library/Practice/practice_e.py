"""
Mavzu: Python math kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
"""
import re
# Exercise: 5
# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:


def extract_urls_from_file(filename):
    """Berilgan fayldan veb sahifa manzillarini (URL) ajratib oladi"""

    url_pattern = r'https?://[^\s)>\]"\'`]+'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            urls = re.findall(url_pattern, text)
            return urls
    except FileNotFoundError:
        print(f"Fayl topilmadi: {filename}")
        return []


urls = extract_urls_from_file('text.txt')
print("Topilgan URLlar:")
for url in urls:
    print(url)
