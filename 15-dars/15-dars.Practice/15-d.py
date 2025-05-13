"""
Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""
menu = {
  "osh":"30000",
  "lag'mon":"27000",
  "kabob":"16000",
  "halim":"35000",
  "tushonka":"37000",
  "mastava":"22000",
  "somsa":"9000",
  "sho'rva":"25000",
  "norin":"25000",
  "qozon kabob":"40000",
  "manti":"18000",
  "do'lma":"17000",
  "tabaka":"22000",
  "moxora":"28000"
}
print("3 ta taom buyurtma bering: ")
buyurtmalar = []
for n in range(3):
  buyurtmalar.append(input(f"{n+1}-taom: ").strip().lower())

for buyurtma in buyurtmalar:
  if buyurtma in menu:
    print(f"{buyurtma}: {menu[buyurtma]} so'm")
  else:
    print(f"Kechirasiz, bizda {buyurtma} qolmadi.")

''' Yuqoridagi kodni yanada optimallashgan ko'rinishga olib kelamiz '''

print("3 ta taom buyurtma bering (vergul bilan ajratib kiriting):")
buyurtmalar = input().strip().lower().split(",")[:3] # [:3] orqali faqat dastlabki 3 ta taomni saqlaymiz

# Xar bir buyurtmani loop yordamida tekshiramiz
for buyurtma in buyurtmalar:
    buyurtma = buyurtma.strip() # Har bir taomning bosh va oxiridagi bo'sh joylarini olib tashlaymiz
    narx = menu.get(buyurtma) # menu.get(buyurtma) yordamida menu lug'atidan taom narxini olamiz va xatolarni oldini oldik, 
    if narx: # Agar narx mavjud bo'lsa (taom menyuda bo'lsa)
        print(f"{buyurtma.title()}: {narx} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} qolmadi.")