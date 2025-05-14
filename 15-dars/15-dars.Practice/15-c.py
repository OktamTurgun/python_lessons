"""
Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning
poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni
kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
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

davlat = input("Istalgan davlatni yozing va poytaxtini bilib oling: ").strip().title()
if davlat in countries:
  print(f"{davlat}ning poytaxti: {countries[davlat]} shahri")
else:
  print(f"Bizda {davlat} haqida ma'lumot yo'q!")