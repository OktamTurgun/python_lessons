"""
Karra jadvalidan tasodifiy savollar beradigan va foydalanuvchi to'g'ri javob bergunicha yoki dastur to'xtaguncha davom etadigan dastur yozing:
"""
import random
def karra_jadvali_oyini():
    print('Assalomu aleykum!')
    print("Karra jadvali o'yiniga xush kelibsiz!")
    print("Dasturni to'xtatish uchun 'stop' deb yozing.")
    
    while True:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        savol = f"{a}x{b} nechiga teng?>>> "
        
        javob = input(savol)
        
        if javob.lower() == 'stop':
            print("O'yin tugadi. Rahmat!")
            break
            
        try:
            javob_float = float(javob)
            if javob_float == a * b:
                print("Barakalla! Javob to'g'ri.")
            else:
                print(f"Javob xato! To'g'ri javob: {a*b}. Yana urunib ko'ring.")
        except ValueError:
            print("Iltimos, faqat raqam yoki 'stop' kiriting!")

# Dasturni boshlash
karra_jadvali_oyini()

import random

def karra_jadvali_oyini():
    print("Assalomu aleykum! Karra jadvaliga xush kelibsiz!")
    
    # Foydalanuvchi ismini so'raymiz
    ism = input("Ismingizni kiriting: >>> ").strip().title()
    
    # O'yin boshlashga tayyorligini tekshiramiz
    tayyor = input(f"{ism}, tayyormisiz? (ha/yo'q): >>> ").lower()
    
    if tayyor != 'ha':
        print("Yaxshi, keyinroq urinib ko'ring!")
        return
    
    print(f"\nAjoyib {ism}! O'yin boshlanmoqda...")
    print("Har bir to'g'ri javob uchun 1 ball olasiz.")
    print("Sizda 3 ta xato javob berish imkoniyati bor.\n")
    
    ballar = 0
    xato_chegara = 5
    xato_soni = 0
    
    while xato_soni < xato_chegara:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        to_gri_javob = a * b
        
        savol = f"{a} x {b} = ? (Javobingizni kiriting yoki 'stop' deb yozing): >>> "
        javob = input(savol)
        
        if javob.lower() == 'stop':
            print(f"\nO'yin tugadi {ism}! Sizning ballaringiz: {ballar}")
            return
            
        try:
            javob_int = int(javob)
            if javob_int == to_gri_javob:
                ballar += 1
                print(f"Barakalla {ism}! ✅ To'g'ri javob! Sizning ballaringiz: {ballar}")
            else:
                xato_soni += 1
                print(f"Xato ❌! To'g'ri javob: {to_gri_javob}. Sizda {xato_chegara - xato_soni} imkoniyat qoldi.")
        except ValueError:
            print("Iltimos, faqat raqam kiriting yoki 'stop' deb yozing!")
    
    print(f"\n{ism}, siz {xato_chegara} marta xato javob berdingiz. O'yin tugadi.")
    print(f"Yakuniy ballaringiz: {ballar}")

# Dasturni boshlash
karra_jadvali_oyini()