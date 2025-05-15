"""
Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat
haqida ma'lumotni konsolga chiqaring
"""
countries = {
    "Uzbekistan": {
        "poytaxti": "Toshkent",
        "axoli_soni": "36 million",
        "maydoni": "448,978 km²",
        "davlat_tili": "O'zbek tili",
        "tabiati": "cho'l, tog', o'rmon, dasht",
        "davlat_tuzumi": "prezidentlik respublikasi"
    },
    "USA": {
        "poytaxti": "Vashington",
        "axoli_soni": "331 million",
        "maydoni": "9,834,000 km²",
        "davlat_tili": "Ingliz tili",
        "tabiati": "tog', cho'l, o'rmon, daryo, ko'l",
        "davlat_tuzumi": "federal respublika"
    },
    "China": {
        "poytaxti": "Pekin",
        "axoli_soni": "1.4 milliard",
        "maydoni": "9,596,961 km²",
        "davlat_tili": "Xitoy tili (Mandarin)",
        "tabiati": "tog', cho'l, daryo, o'rmon",
        "davlat_tuzumi": "kommunistik respublika"
    },
    "Russia": {
        "poytaxti": "Moskva",
        "axoli_soni": "146 million",
        "maydoni": "17,098,242 km²",
        "davlat_tili": "Rus tili",
        "tabiati": "tog', o'rmon, dasht, tundra",
        "davlat_tuzumi": "federal respublika"
    },
    "Germany": {
        "poytaxti": "Berlin",
        "axoli_soni": "83 million",
        "maydoni": "357,386 km²",
        "davlat_tili": "Nemis tili",
        "tabiati": "tog', o'rmon, daryo, tekislik",
        "davlat_tuzumi": "federal parlament respublikasi"
    },
    "Japan": {
        "poytaxti": "Tokio",
        "axoli_soni": "125 million",
        "maydoni": "377,975 km²",
        "davlat_tili": "Yapon tili",
        "tabiati": "tog', o'rmon, dengiz sohillari",
        "davlat_tuzumi": "konstitutsiyaviy monarxiya"
    },
    "Brazil": {
        "poytaxti": "Braziliya",
        "axoli_soni": "213 million",
        "maydoni": "8,515,767 km²",
        "davlat_tili": "Portugaliya tili",
        "tabiati": "o'rmon (Amazonka), tog', daryo",
        "davlat_tuzumi": "federal respublika"
    },
    "India": {
        "poytaxti": "Yangi Dehli",
        "axoli_soni": "1.4 milliard",
        "maydoni": "3,287,263 km²",
        "davlat_tili": "Hind, ingliz",
        "tabiati": "tog', cho'l, tropik o'rmon, daryo",
        "davlat_tuzumi": "federal parlament respublikasi"
    },
    "France": {
        "poytaxti": "Parij",
        "axoli_soni": "67 million",
        "maydoni": "643,801 km²",
        "davlat_tili": "Fransuz tili",
        "tabiati": "tog', o'rmon, tekislik, daryo",
        "davlat_tuzumi": "yarim-prezidentlik respublikasi"
    },
    "United Kingdom": {
        "poytaxti": "London",
        "axoli_soni": "68 million",
        "maydoni": "243,610 km²",
        "davlat_tili": "Ingliz tili",
        "tabiati": "tog', tekislik, daryo, dengiz",
        "davlat_tuzumi": "konstitutsiyaviy monarxiya"
    }
}

for key, values in countries.items():
  print(f"\n{key} haqida:")
  for value, info in values.items():
    print(f"{value.title()}: {info}")
    
# Takomillashtirilgan kod
# Davlatlar lug'atini aylanib chiqamiz (har bir davlat va uning ma'lumotlari uchun)
for davlat, info in countries.items():
    # Davlat nomini katta harflar bilan va qalin (bold) shriftda chiqaramiz
    # \033[1m - bold boshlash, \033[0m - formatlashni tugatish
    print(f"\n\033[1m{davlat.upper()}\033[0m")
    
    # Davlat nomi uzunligi + 2ga teng bo'lgan chiziq chizamiz (ko'rinish uchun)
    print("-" * (len(davlat) + 2))
    
    # Har bir davlat ma'lumotlari uchun (kalit va qiymat)
    for key, value in info.items():
        # Underscore (_) ni bo'shliq bilan almashtiramiz va har bir so'zni bosh harf bilan yozamiz
        translated_key = key.replace("_", " ").title()
        
        # Formatlangan kalit va qiymatni chiqaramiz
        print(f"{translated_key}: {value}")
    
    # Har bir davlat ma'lumotidan keyin ajratuvchi chiziq (40 ta '-')
    print("-" * 40)