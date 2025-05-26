'''
Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa
ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
'''
# Example: 1
def talaba_info(ism, familiya, **malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    talaba = {
        'ism': ism,
        'familiya': familiya,
    }
    for kalit, qiymat in malumotlar.items():
        talaba[kalit] = qiymat
    return talaba
# Misol uchun:
talaba1 = talaba_info('olim', 'hakimov', yosh=20, kurs=2, fakultet='Informatika')
talaba2 = talaba_info('davron', 'qobulov', yosh=22, kurs=3, fakultet='Matematika', shahar='Toshkent')
talaba3 = talaba_info('hasan', 'aliyev', yosh=21, fakultet='Fizika', shahar='Samarqand')
talabalar = [talaba1, talaba2, talaba3]
for talaba in talabalar:
    print(f"Talaba: {talaba['ism'].title()} {talaba['familiya'].title()}")
    for kalit, qiymat in talaba.items():
        if kalit not in ['ism', 'familiya']:
            print(f"{kalit.title()}: {qiymat}")
    print()  # Bo'sh qator chiqarish uchun
    
''''''
# Example: 2
def student_info(ism, familiya, **malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    student = {'ism': ism, 'familiya': familiya}
    student.update(malumotlar)
    return student

def print_student(student):
    """Talaba ma'lumotlarini chiroyli chiqaruvchi funksiya"""
    print(f"Talaba: {student['ism'].title()} {student['familiya'].title()}")
    for key, value in student.items():
        if key not in ['ism', 'familiya']:
            # Agar qiymat string bo'lsa title() qilamiz, aks holda o'zgartirmaymiz
            chiqarish_qiymati = str(value).capitalize() if isinstance(value, str) else value
            print(f"{key.title()}: {chiqarish_qiymati}")
    print()

# Misollar
talaba1 = student_info('olim', 'hakimov', yosh=20, kurs=2, fakultet='Informatika')
talaba2 = student_info('davron', 'qobulov', yosh=22, kurs=3, fakultet='Matematika', shahar='Toshkent')
talaba3 = student_info('hasan', 'aliyev', yosh=21, fakultet='Fizika', shahar='Samarqand', shaxsiy_reyting=4.5)
talaba4 = student_info('gulnora', 'sultonova', yosh=19, kurs=1, fakultet='Tibbiyot', millati='o\'zbek')

# Lug'atni alohida yaratib berish usuli
qoshimcha_malumotlar = {
    'yosh': 24,
    'kurs': 5,
    'fakultet': 'Jurnalistika',
    'ishlaydi': True
}

talaba5 = student_info('nozim', 'nazarov', **qoshimcha_malumotlar)
print_student(talaba5)

#
talabalar = [talaba1, talaba2, talaba3, talaba4]
for talaba in talabalar:
    print_student(talaba)
    
   
    
    
    
    
    
    
    
    
    
    
    