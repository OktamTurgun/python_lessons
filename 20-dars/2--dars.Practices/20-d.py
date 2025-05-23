'''
Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi,
1 dan katta musbat sonlar)
'''
# Variant 1 Eng samarali yechim  
def tub_sonlar(min, max):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya."""
    tub_sonlar = []
    for num in range(min, max + 1):
        if num > 1:  # 1 dan katta sonlarni tekshiramiz
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                tub_sonlar.append(num)
    return tub_sonlar
print(tub_sonlar(10, 50)) 

''''''
# Variant 2 biroz optimallashtirilgan
# def tub_sonlar_top(min_num, max_num):
#     """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya."""
#     # Agar minimal son 2 dan kichik bo'lsa, uni 2 ga tenglaymiz 
#     tub_sonlar = []   
    
#     for n in range(max(min_num,2), max_num + 1): # 1 dan kichuk sonlarni otkazib yuboramiz
#         for x in range(2, int(n**0.5) + 1): # faqat kvadrat ildizigacha tekshiramiz
#             if n % x == 0:
#                 break
#         else:
#             tub_sonlar.append(n)
#     return tub_sonlar
    
# print(tub_sonlar_top(0, 10))
# print(tub_sonlar_top(1, 100))

''''''
# variant 3
def tub_sonlar_top(min, max):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya."""
    tub_sonlar = []
    # Agar minimal son 2 dan kichik bo'lsa, uni 2 ga tenglaymiz
    for n in range(min, max + 1): # 1 dan kichik sonlarni o'tkazib yuboramiz
        tub = True 
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n): # 2 dan n-1 gacha bo'lgan sonlarni tekshiramiz
                if n % x == 0: # Agar n x ga qoldiqsiz bo'linadigan bo'lsa, tub emas
                    tub = False # tub emas
        if tub: # Agar tub bo'lsa, ro'yxatga qo'shamiz
            tub_sonlar.append(n)

    return tub_sonlar # tub sonlar ro'yxatini qaytaradi
print(tub_sonlar_top(0, 10)) # [2, 3, 5, 7] 
print(tub_sonlar_top(1, 100))
 