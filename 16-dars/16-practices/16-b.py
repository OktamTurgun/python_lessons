"""
Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring
"""

navoiy = {
    "ism_sharif": "Alisher Navoiy (Nizomiddin Mir Alisher)",
    "tugilgan_yili": 1441,
    "mashxur_asarlari": ["Xamsa", "Mahbub ul-Qulub", "Majolis un-Nafois"],
    "qayerdan": "Hirot (hozirgi Afgʻoniston)",
}

buhoriy = {
    "ism_sharif": "Imom al-Buxoriy (Muhammad ibn Ismoil al-Buxoriy)",
    "tugilgan_yili": 810,
    "mashxur_asarlari": ["Sahih al-Buxoriy", "Al-Adab al-Mufrad"],
    "qayerdan": "Buxoro (hozirgi Oʻzbekiston)",
}

gazzoliy = {
    "ism_sharif": "Abu Homid al-Gʻazzoliy (Muhammad ibn Muhammad al-Gʻazzoliy)",
    "tugilgan_yili": 1058,
    "mashxur_asarlari": ["Ihyo ulum ad-din", "Kimyo-yi Saodat"],
    "qayerdan": "Tus (hozirgi Eron)",
}

imom_muslim = {
    "ism_sharif": "Muslim ibn al-Hajjoj al-Qushayriy an-Naysaburiy",
    "tugilgan_yili": 821,
    "vafot_yili": 875,
    "mashxur_asarlari": ["Sahih Muslim", "Al-Kuno va al-Asmo", "At-Tabaqot"],
    "qayerdan": "Nishopur (hozirgi Eron)",
}

popular_people = [buhoriy, navoiy, gazzoliy, imom_muslim]
for people in popular_people:
  print(f"Ism sharif: {people['ism_sharif']}\n"
        f"Mashhur asarlari:  {people['mashxur_asarlari']}\n")
  
# Example 2
popular_people = [buhoriy, navoiy, gazzoliy, imom_muslim]
for people in popular_people:
  malumot = f"""{'='*50}\nIsm Sharif: {people['ism_sharif']}\nMashhur asarlari: {people['mashxur_asarlari']}\n{'='*50}"""
  print(malumot)
