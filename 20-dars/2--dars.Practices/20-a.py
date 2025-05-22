"""
Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
"""
# variant 1

# def user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email=None, tel=None):
#     """Foydalanuvchi ma'lumotlarini lug'at ko'rinishida qaytaradi"""
#     user = {
#         'ism':ism,
#         'familiya':familiya,
#         'yosh':yosh,
#         'tugilgan_yil':tugilgan_yil,
#         'tugilgan_joy':tugilgan_joy,
#         'email':email or '',
#         'tel':tel or ''
#         }
#     if email:
#         user['email'] = email
#     if tel:
#         user['tel'] = tel
#     return user


# print("Mijoz haqida ma'lumot kiriting:\n")
# users = []
# while True:
#     ism = input("Ismingizni kiriting: ").strip()
#     familiya = input("Familiyangizni kiriting: ").strip()
#     yosh = int(input("Yoshingizni kiriting: ").strip())
#     tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: ").strip())
#     tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ").strip()
#     email = input("Emailingizni kiriting (optional): ").strip() or None
#     tel = input("Telefon raqamingizni kiriting (optionl): ").strip() or None
#     users.append(user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email, tel))
    
#     javob = input("Davom etasizmi? (yes/no): ")
#     if javob != 'yes':
#         break
# print("\nMijozlarimiz haqida ma'lumotlar: ")
# for user in users:
#     print(f"{user['ism'].title()} {user['familiya'].title()} {user['yosh']}-yoshda, \n"
#           f"Tug'ilgan yil: {user['tugilgan_yil']}. \n"
#           f"Manzil: {user['tugilgan_joy'].title()}. \n")
#     if user['email']:
#         print(f"Email: {user['email']}")
#     if user['tel']:
#         print(f"Telefon: {user['tel']}")
    
''''''
# Variant 2

# def user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email=None, tel=None):
#     """Foydalanuvchi ma'lumotlarini lug'at ko'rinishida qaytaradi"""
#     return {
#         'ism': ism,
#         'familiya': familiya,
#         'yosh': yosh,
#         'tugilgan_yil': tugilgan_yil,
#         'tugilgan_joy': tugilgan_joy,
#         'email': email or '',  # email None bo'lsa, bo'sh string qo'yamiz
#         'tel': tel or ''        # tel None bo'lsa, bo'sh string qo'yamiz
    # }

# def display_user(user):
#     """Foydalanuvchi ma'lumotlarini chiroyli chiqarish"""
#     print(f"\nFoydalanuvchi ma'lumotlari:")
#     print(f"Ism: {user['ism'].title()} {user['familiya'].title()}")
#     print(f"Yosh: {user['yosh']} (Tug'ilgan yil: {user['tugilgan_yil']})")
#     print(f"Tug'ilgan joy: {user['tugilgan_joy'].title()}")
#     if user['email']:
#         print(f"Email: {user['email']}")
#     if user['tel']:
#         print(f"Telefon: {user['tel']}")
#     print("-" * 30)

# def get_user_input():
#     """Foydalanuvchidan ma'lumotlarni qabul qilish"""
#     print("\nIltimos, ma'lumotlaringizni kiriting:")
#     ism = input("Ism: ").strip()
#     familiya = input("Familiya: ").strip()
#     yosh = int(input("Yosh: ").strip())
#     tugilgan_yil = int(input("Tug'ilgan yil: ").strip())
#     tugilgan_joy = input("Tug'ilgan joy: ").strip()
#     email = input("Email (ixtiyoriy): ").strip() or None
#     tel = input("Telefon raqam (ixtiyoriy): ").strip() or None
    
#     return user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email, tel)

# # Asosiy dastur
# if __name__ == "__main__":
#     users = []
#     print("Foydalanuvchi ma'lumotlarini kiritish dasturi")
    
#     while True:
#         users.append(get_user_input())
        
#         javob = input("\nYana foydalanuvchi qo'shasizmi? (ha/yo'q): ").lower()
#         if javob not in ('ha', 'yes', "yo'q", 'no'):
#             break
    
#     print("\nKiritilgan barcha foydalanuvchilar:")
#     for user in users:
#         display_user(user)

''''''''
# Variant 2
def user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email=None, tel=None):
    """Foydalanuvchi ma'lumotlarini lug'at ko'rinishida qaytaradi"""
    return {
        'ism': ism,
        'familiya': familiya,
        'yosh': yosh,
        'tugilgan_yil': tugilgan_yil,
        'tugilgan_joy': tugilgan_joy,
        'email': email or '',
        'tel': tel or ''
    }

def display_user(user):
    """Foydalanuvchi ma'lumotlarini chiroyli chiqarish"""
    output = [
        f"\n{user['ism'].title()} {user['familiya'].title()}, {user['yosh']}-yoshda",
        f"Tug'ilgan yil: {user['tugilgan_yil']}",
        f"Manzil: {user['tugilgan_joy'].title()}"
    ]
    
    if user['email']:
        output.append(f"Email: {user['email']}")
    if user['tel']:
        output.append(f"Telefon: {user['tel']}")
    
    print('\n'.join(output))

def main():
    """Asosiy dastur logikasi"""
    print("Mijoz haqida ma'lumot kiriting:\n")
    users = []
    
    while True:
        ism = input("Ismingizni kiriting: ").strip()
        familiya = input("Familiyangizni kiriting: ").strip()
        yosh = int(input("Yoshingizni kiriting: ").strip())
        tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: ").strip())
        tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ").strip()
        email = input("Emailingizni kiriting (optional): ").strip() or None
        tel = input("Telefon raqamingizni kiriting (optional): ").strip() or None
        
        users.append(user_info(ism, familiya, yosh, tugilgan_yil, tugilgan_joy, email, tel))
        
        javob = input("\nDavom etasizmi? (ha/yo'q): ").lower()
        if javob not in ('ha', 'yes', "yo'q", 'no'):
            break
    
    print("\nMijozlarimiz haqida ma'lumotlar:")
    for user in users:
        display_user(user)

if __name__ == "__main__":
    main()