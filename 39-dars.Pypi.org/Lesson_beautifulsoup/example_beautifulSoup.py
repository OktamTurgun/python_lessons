
from bs4 import BeautifulSoup

# HTML fayl nomi
FILE_NAME = "sample.html"

# HTML faylni yuklaymiz


def load_html(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

# 1. Barcha <img> teglar va ularning src atributlari


def extract_image_sources(soup):
    print("🖼️ Rasm manzillari (img src):")
    images = soup.find_all("img")
    for img in images:
        src = img.get("src")
        if src:
            print(f"- {src}")
    print("-" * 40)

# 2. Faqat .pdf fayllarga olib boradigan <a> teglar


def extract_pdf_links(soup):
    print("📄 PDF faylga olib boruvchi linklar:")
    links = soup.find_all("a")
    for link in links:
        href = link.get("href", "")
        if href.endswith(".pdf"):
            print(f"- {href}")
    print("-" * 40)

# 3. Eng uzun <p> matnni topish


def find_longest_paragraph(soup):
    print("📌 Eng uzun <p> matn:")
    paragraphs = soup.find_all("p")
    if not paragraphs:
        print("Hech qanday <p> topilmadi.")
        return

    longest = max(paragraphs, key=lambda p: len(p.text.strip()))
    print(longest.text.strip())
    print("-" * 40)

# --- Asosiy dastur ---


def main():
    soup = load_html(FILE_NAME)
    extract_image_sources(soup)
    extract_pdf_links(soup)
    find_longest_paragraph(soup)


if __name__ == "__main__":
    main()
