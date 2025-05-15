"""
Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat 
ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
"""
films = {
  "abbos": ['shoushendan qochish', 'joker', 'titanik'],
  "tohir": ['qora ritsar', 'rambo', 'uzuklar hukmdori'],
  "shaxlo": ['qirol sher', 'simpsonlar', 'titanik'],
  "o'tkir": ['matritsa', 'yulduzlar jangi', 'gladiator'],
  "xurshid": ['forest gamp', 'parazit', 'rembo']
}

for name, kinolar in films.items():
  print(f"\n{name.title()}ning sevimli kinolari:")
  print("="*25)
  for kino in kinolar:
    print(f"-",kino.title())