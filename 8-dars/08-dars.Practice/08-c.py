# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
uzbek_foods = ["osh", "norin", "somsa", "kabob", "lag'mon", "sho'rva", "qaymoq va non", "issiq non", "gurochli bo'tqa", "tuxum"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
breakfast = uzbek_foods[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
breakfast = breakfast[-4:]
breakfast.extend(["botirlar bo'tqasi", 'shirin choy va non']) # 2 ta taom qo'shildi

# Ikkala ro'yxatni ham (uzbek_foods va breakfast) konsolga chiqaring
print(breakfast)
print(uzbek_foods)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
breakfast = tuple(breakfast)

# Bu xato beradi, chunki tuple o'zgarmas 
breakfast[0] = 'uzum' # TypeError: 'tuple' object does not support item assignment
print(type(breakfast))