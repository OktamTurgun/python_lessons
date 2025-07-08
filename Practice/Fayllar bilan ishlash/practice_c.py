"""
Mavzu: Practice. Matndan statistik analiz
Muallif: Uktam Turgunov
Sana: 2025-07-08

Vazifa 1: 
Berilgan matnli fayldan:
- nechta satr (qator)
- nechta so‘z
- nechta belgi (harf)
borligini hisoblaydigan dastur yozing

"""


def text_analysis(matn):
    with open("matn.txt", 'r', encoding='utf-8') as file:
        matn = file.read()

        satrlar = matn.splitlines()
        words = matn.split()
        characters = matn.replace("\n", '')

        print("Statistika:")
        print(f"Satrlar soni: {len(satrlar)}")
        print(f"So'zlar soni: {len(words)}")
        print(f"Belgilar soni: {len(characters)}")


if __name__ == "__main__":
    text_analysis("matn.txt")
