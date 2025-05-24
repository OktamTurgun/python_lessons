'''

Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan
foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat
lug'at qaytaradigan qilib yozing.
'''
def bahola(ismlar):
    # Talabalar ro'yxatini qabul qilib, baholarni so'raydi
    # va natijani lug'at ko'rinishida qaytaradi
    baholar = {}
    for ism in ismlar:
        baho = input((f"Talaba {ism.title()}ning bahosini kiriting: "))
        baholar[ism] = int(baho)
    return baholar
  
talabalar = ['ali', 'vali', 'olim', 'hasan', 'husan']
baholar = bahola(talabalar)   
print("Talabalarning baholari:")
for ism, baho in baholar.items():
    print(f"{ism.title()}ning bahosi: {baho}")