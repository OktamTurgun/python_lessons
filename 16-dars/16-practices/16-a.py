"""
Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi
ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
va har bir shaxs haqidagi ma'lumotni konsolga chiqaring
"""

Elon = {
        "fullname": "Elon Musk",
        "yosh": 52,
        "activity": "SpaceX, Tesla, Neuralink va Twitter kompaniyalari asoschisi va rahbari",
        "kasb": "Tadbirkor, muhandis, ixtirochi",
        "millat": "Amerikalik (Janubiy Afrika kelib chiqishi)",
        "place": "AQSh"
        }
Ronaldo = {
          "fullname": "Cristiano Ronaldo",
          "yosh": 38,
          "activity": "Professional futbolchi, Saudiya Arabistonining Al-Nassr klubida o'ynaydi",
          "kasb": "Sportchi (futbolchi)",
          "millat": "Portugal",
          "place": "Saudiya Arabistoni"
          }
Rowling = {
          "fullname": "J.K. Rowling",
          "yosh": 59,
          "activity": "Garri Potter kitoblari muallifi",
          "kasb": "Yozuvchi",
          "millat": "Britan",
          "place": "Buyuk Britaniya"
          }
Sundar = {
          "fullname": "Sundar Pichai",
          "yosh": 52,
          "activity": "Google va Alphabet kompaniyalari bosh direktori",
          "kasb": "Tadbirkor, texnologiya mutaxassisi",
          "millat": "Hind",
          "place": "AQSh"
          }
popular_peoples = [Elon, Ronaldo, Rowling, Sundar]

# for person in popular_peoples:
#   fullname = person["fullname"]
#   age = person["yosh"]
#   activity = person["activity"]
#   profession = person["kasb"]
#   nationality = person["millat"]
#   residence = person["place"]
#   print(f"\nFullnmae: {fullname}, Age: {age},\n"
#         f"Career: {activity.title()}, \n"
#         f"Profession: {profession}, \n"
#         f"Nationality: {nationality}, Residence: {residence}")
  
# Yana bir chiroyli usul (f-string formatlash):
for person in popular_peoples:
    info = f"""
{'='*50}
Full Name: {person['fullname']}
Age: {person['yosh']}
Career: {person['activity']}
Profession: {person['kasb']}
Nationality: {person['millat']}
Residence: {person['place']}
{'='*50}
"""
    print(info)
    
# Takomillashtirilgan versiya (.items() va chiroyli formatlash):
for person in popular_peoples:
    print("\n" + "="*50)  # Ajratish uchun chiziq
    for key, value in person.items():
        # Kalitlarni chiroyli nomlarga o'zgartirish
        display_key = {
            "fullname": "Full Name",
            "yosh": "Age",
            "activity": "Career",
            "kasb": "Profession",
            "millat": "Nationality",
            "place": "Residence"
        }.get(key, key)
        
        print(f"{display_key}: {value}")
