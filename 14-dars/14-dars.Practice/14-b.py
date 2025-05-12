"""
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta
ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini 
konsolga chiqaring: Alining sevimli taomi osh
"""
taom = {
  'otam': 'Suyuq ovqatlani xammasini sevib istemol qiladilar',
  'onam': 'manti, dolma, kabob',
  'akam': 'osh, somsa, halim',
  'singlim': 'qozon-kabob, norin' 
}

# print(f"Otamning sevimli taomlari: {taom['otam']}, "
#       f"Onamning sevimli taomlari: {taom['onam']}, "
#       f"Akamning sevimli taomlari: {taom['akam']}, "
#       f"Singlimning sevimli taomlari: {taom['singlim']}")

# Huddi shu lig'atni for loop bilan chiroyli xolatda formatlash mumkin.
for relation, info in taom.items():
  if isinstance(info, list):
    print(f"{relation.title()}ning sevimli taimlari: {', '.join(info)}")
  else:
    print(f"{relation.title()}ning sevimli taomi: {info}")