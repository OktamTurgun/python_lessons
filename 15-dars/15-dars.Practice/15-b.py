"""
Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
"""
countries = {
  "Uzbekistan":"Tashkent",
  "Canada": "Ottawa",
  "Russia": "Moscow",
  "Denmark": "Copenhagen",
  "Egypt": "Cairo",
  "Qatar": "Doha",
  "Spain": "Madrid",
  "Turkey": "Ankara",
  "France": "Paris",
  "Germany": "Berlin",
  "Hungary": "Budapest",
  "India": "New Delhi",
  "Argentina": "Buenos Aires",
  "Japan": "Tokyo",
  "Kenya": "Nairobi",
  "Luxembourg": "Luxembourg",
  "Mexico": "Mexico City",
  "Nigeria": "Abuja",
  "Oman": "Muscat",
  "Peru": "Lima",
  "Brazil": "Brasilia"
}
print("Dunyo davlatlari:")
for country in sorted(countries.keys()):
  print(country)

print("\nDavlatlar poytaxtlari:")
for capital in sorted(countries.values()):
  print(capital)

print("Dunyo davlat va poytaxtlari:\n"+'_'*28) # (\n", '_'*28. sep='') Bu xam xuddu shu natijani chiqaradi
for country, capital in sorted(countries.items()):
  print("{:<12}: {}".format(country, capital))