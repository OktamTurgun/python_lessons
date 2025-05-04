# # sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang 
# (musbat, manfiy, butun, o'nlik). 
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

sonlar = [12, 76.5, -23.2, 34.9, 50, 99, -500]

sonlar.append(41)
sonlar.append(120)
sonlar.append(19.0)

sonlar.insert(0, 0.7)
sonlar.remove(50)

sonlar[4] = sonlar[4] + 2222
sonlar = sonlar[:-2] # oxirgi 2ta elementni o'chiradi
son = sonlar.pop(1)
sonlar.insert(3, 54)

sonlar.extend([5.5, -40, 130])

sonlar.sort()
sonlar.reverse()
sonlar.sort(reverse=True)
print(sonlar)