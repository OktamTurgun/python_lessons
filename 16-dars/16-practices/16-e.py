""" 
16-d.py dagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
"""
countries = {
    "Uzbekistan": {
        "poytaxti": "Toshkent",
        "axoli_soni": "36 million",
        "maydoni": "448,978 km²",
        "davlat_tili": "O'zbek tili",
        "tabiati": "cho'l, tog', o'rmon, dasht",
        "davlat_tuzumi": "prezidentlik respublikasi",
        "pul_birligi":"so'm"
    },
    "USA": {
        "poytaxti": "Vashington",
        "axoli_soni": "331 million",
        "maydoni": "9,834,000 km²",
        "davlat_tili": "Ingliz tili",
        "tabiati": "tog', cho'l, o'rmon, daryo, ko'l",
        "davlat_tuzumi": "federal respublika",
        "pul_birligi":"AQSH dollari"
    },
    "China": {
        "poytaxti": "Pekin",
        "axoli_soni": "1.4 milliard",
        "maydoni": "9,596,961 km²",
        "davlat_tili": "Xitoy tili (Mandarin)",
        "tabiati": "tog', cho'l, daryo, o'rmon",
        "davlat_tuzumi": "kommunistik respublika",
        "pul_birligi":"yuan"
    },
    "Russia": {
        "poytaxti": "Moskva",
        "axoli_soni": "146 million",
        "maydoni": "17,098,242 km²",
        "davlat_tili": "Rus tili",
        "tabiati": "tog', o'rmon, dasht, tundra",
        "davlat_tuzumi": "federal respublika",
        "pul_birligi":"rubl"
    },
    "Germany": {
        "poytaxti": "Berlin",
        "axoli_soni": "83 million",
        "maydoni": "357,386 km²",
        "davlat_tili": "Nemis tili",
        "tabiati": "tog', o'rmon, daryo, tekislik",
        "davlat_tuzumi": "federal parlament respublikasi",
        "pul_birligi":"yevro"
    },
    "Japan": {
        "poytaxti": "Tokio",
        "axoli_soni": "125 million",
        "maydoni": "377,975 km²",
        "davlat_tili": "Yapon tili",
        "tabiati": "tog', o'rmon, dengiz sohillari",
        "davlat_tuzumi": "konstitutsiyaviy monarxiya",
        "pul_birligi":"yena"
    },
    "Brazil": {
        "poytaxti": "Braziliya",
        "axoli_soni": "213 million",
        "maydoni": "8,515,767 km²",
        "davlat_tili": "Portugaliya tili",
        "tabiati": "o'rmon (Amazonka), tog', daryo",
        "davlat_tuzumi": "federal respublika",
        "pul_birligi":"brazil reali"
    },
    "India": {
        "poytaxti": "Yangi Dehli",
        "axoli_soni": "1.4 milliard",
        "maydoni": "3,287,263 km²",
        "davlat_tili": "Hind, ingliz",
        "tabiati": "tog', cho'l, tropik o'rmon, daryo",
        "davlat_tuzumi": "federal parlament respublikasi",
        "pul_birligi":"hind rupiyasi"
    },
    "France": {
        "poytaxti": "Parij",
        "axoli_soni": "67 million",
        "maydoni": "643,801 km²",
        "davlat_tili": "Fransuz tili",
        "tabiati": "tog', o'rmon, tekislik, daryo",
        "davlat_tuzumi": "yarim-prezidentlik respublikasi",
        "pul_birligi":"yevro"
    },
    "United Kingdom": {
        "poytaxti": "London",
        "axoli_soni": "68 million",
        "maydoni": "243,610 km²",
        "davlat_tili": "Ingliz tili",
        "tabiati": "tog', tekislik, daryo, dengiz",
        "davlat_tuzumi": "konstitutsiyaviy monarxiya",
        "pul_birligi":"fult sterling"
    }
}
'''
"To'liq ma'lumotlar formati" yoki "Batafsil format":
Barcha kalit-qiymat juftliklarini avtomatik ravishda chiqaradi
Lug'atdagi barcha ma'lumotlarni standart formatda ko'rsatadi
Kod qisqa va universal (har qanday yangi maydon qo'shilsa, o'zgarishsiz ishlaydi)
'''
davlat = input("Dalat nomini kiriting: ").strip().title()
if davlat in countries:
  print(f"\n{davlat} haqida ma'lumot: ")
  print("_" * (len(davlat) + 16))
  for key, value in countries[davlat].items():
    # Underscore (_) ni bo'shliq bilan almashtiramiz va har bir so'zni bosh harf bilan yozamiz
    translated_key = key.replace("_", " ").title()
    # Formatlangan kalit va qiymatni chiqaramiz
    print(f"{translated_key:<15}: {value}")
  # Har bir davlat ma'lumotidan keyin ajratuvchi chiziq (40 ta '-') 
  print("_" * 40)
else:
  print(f"Kechirasiz, bizda {davlat} haqida ma'lumot yo'q!")
  
'''
"Maxsus ko'rinish formati" yoki "Tanlangan format":
Faqat kerakli maydonlarni aniq ko'rsatib chiqaradi
Chiqarish formati aniq nazorat qilinadi (masalan, "poytaxti" emas "poytaxt" deb chiqarish)
Har bir maydon uchun alohida formatlash talab qilinadi
'''  
davlat = input('Davlat nomini kiriting: ').strip().title()
if davlat in countries:
    info = countries[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxti'].title()}"
          f"\nHududi: {info['maydoni']} kv.km"
          f"\nAholisi: {info['axoli_soni']}"
          f"\nDavlat tili: {info['davlat_tili']}"
          f"\nDavlat tuzumi: {info['davlat_tuzumi'].title()}"
          f"\nPul birligi: {info['pul_birligi'].title()}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
        