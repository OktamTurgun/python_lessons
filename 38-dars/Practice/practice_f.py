"""
Mavzu: Python re kutubxonasi bilan amaliyot
Muallif: Uktam Turgunov
Sana: 2025-06-30
Mashq: 
-Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
"""

import re


def extract_urls_from_file(filename):
    """Berilgan fayldan veb sahifa manzillarini (URL) ajratib oladi"""

    # Takomillashtirilgan URL pattern
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w .\-~!$&\'()*+,;=:@%?]*'

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # URLlarni topish va oxiridagi nuqta/vergullarni olib tashlash
            urls = [url.rstrip('.,;') for url in re.findall(url_pattern, text)]
            return list(set(urls))  # Takrorlanishlarni olib tashlash
    except FileNotFoundError:
        print(f"Xato: {filename} fayli topilmadi")
        return []
    except UnicodeDecodeError:
        print(f"Xato: {filename} faylini o'qib bo'lmadi (kodlash muammosi)")
        return []
    except Exception as e:
        print(f"Kutilmagan xato: {str(e)}")
        return []


# Test qilish
if __name__ == "__main__":
    urls = extract_urls_from_file('text.txt')
    print("Topilgan URLlar:")
    for i, url in enumerate(urls, 1):
        print(f"{i}. {url}")
