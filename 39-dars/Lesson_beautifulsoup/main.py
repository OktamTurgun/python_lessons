"""
📌 Mavzu: Python requests + BeautifulSoup
📦 Kutubxonalar: requests, bs4
✍️ Muallif: Uktam Turgunov
📅 Sana: 2025-07-03
🧠 Maqsad: Veb sahifadan yangilik sarlavhalarini olish, filtrlash, faylga saqlash
HTML fayl yoki veb sahifani o‘qish

Elementlarni izlash

Ma’lumotlarni tozalash va chiqarish

Foydali misollar
"""
# 1. Kutubxonalarni o‘rnatish
'''
Terminalda:

bash

pip install requests beautifulsoup4
'''
# 2. Oddiy HTML faylni o‘qish


import requests
from bs4 import BeautifulSoup

html = """
<html>
<head><title>Test sahifa</title></head>
<body>
<h1>Salom!</h1>
<p>Bu <b>test</b> sahifa.</p>
<a href="https://example.com">Link</a>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.title)         # <title>Test sahifa</title>
print(soup.title.text)    # Test sahifa
print(soup.h1.text)       # Salom!
print(soup.p.text)        # Bu test sahifa.
print(soup.a['href'])     # https://example.com

# 3. Veb sahifani yuklash va o‘qish


url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)  # Example Domain

# 4. Barcha ma’lum bir taglarni topish

# Barcha <p> teglarni chiqarish
for p in soup.find_all("p"):
    print(p.text)

# 5. Ma’lum class yoki id bo‘yicha qidirish

html = """
<div id="content">
  <p class="text">Bir</p>
  <p class="text">Ikki</p>
  <p>Uch</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

# class bo‘yicha
texts = soup.find_all("p", class_="text")
for t in texts:
    print(t.text)

# id bo‘yicha
div = soup.find(id="content")
print(div.text.strip())

# 6. Attributlar bilan ishlash

html = """
<a href="https://example.com" title="Example">Link</a>
"""
soup = BeautifulSoup(html, "html.parser")

link = soup.find("a")
print(link["href"])      # https://example.com
print(link.get("title"))  # Example

# 7. Matnni tozalash va chiroyli chiqarish

html = """
<div>
    <h1>  Sarlavha   </h1>
    <p>
        Matn    bo'shliqlar bilan.
    </p>
</div>
"""
soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text.strip())      # Sarlavha
print(" ".join(soup.p.text.split()))  # Matn bo'shliqlar bilan.

# 8. Amaliy misol: BBC News’dan sarlavhalar


url = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h3", class_="gs-c-promo-heading__title")

for i, h in enumerate(headlines[:10], 1):
    print(f"{i}. {h.text.strip()}")

# 9. Ma’lumotlarni faylga yozish

with open("titles.txt", "w", encoding="utf-8") as f:
    for h in headlines[:10]:
        f.write(h.text.strip() + "\n")

# 10. Sahifadagi barcha havolalarni olish

links = soup.find_all("a")
for link in links[:10]:
    href = link.get("href")
    if href:
        print(href)
'''
🔗 Foydali metodlar:
Metod	                                      Ma’nosi
soup.find()	                                  Birinchi mos elementni topadi
soup.find_all()	                              Barcha mos elementlarni topadi
soup.select("selector")	                      CSS selektorlar bilan qidirish
tag.text	                                  Tag ichidagi matn
tag.attrs	                                  Tag atributlari
tag.get("attr")	                              Belgilangan atribut qiymati
'''
