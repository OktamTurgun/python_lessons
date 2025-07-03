"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-01
Mavzu: worldcloud moduli

"""

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, "html.parser")

# YANGI class nomi
news = soup.find_all(class_="small-cards__default-text")

matn = ""
for n in news:
    matn += n.get_text(strip=True) + " "

if not matn.strip():
    raise ValueError("Matn bo‘sh chiqdi! Sahifa class nomini tekshiring.")

stopwords = set([
    "uchun", "bo'yicha", "lekin", "bilan",
    "va", "bor", "ham", "xil", "yil"
])

wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=stopwords,
    min_font_size=20
).generate(matn)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
