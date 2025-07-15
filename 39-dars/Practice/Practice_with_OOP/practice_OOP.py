"""
Mavzu: Practice. OOP boʻlimi uchun amaliy topshiriq
Muallif: Uktam Turgunov
Sana: 2025-07-05
Vazifa:
Siz bir kishining hayot yo’li qanday ekanligini numeralogiya orqali psixologik jihatdan aniqlab beruvchi dastur tuzishingiz kerak.

Quyidagi yo’l-yo’riq orqali amalga oshiring:

Person nomli klass yarating

Bu klassga 5 ta attribute bering:
 1. first_name(str): Kishining ismi
 2. last_name(str): Kishining familiyasi
 3. age(int): Kishining yoshi
 4. email(str): Kishining elektron pochtasi
 5. birth_day: Kishining tug’ilgan kuni # bu attribute property bo’lsin 3 ta integer qaytaradigan

Person klassida quyidag funksiyalar amalga oshiriladi:

Obyektning boshlang’ich barcha qiymatlarini o’rnatish uchun constructor yaratin

get_info() deb nomlangan metod yarating, kishining barcha ma’lumotlarini qaytaradigan

get_life_path_number() deb nomlangan metod yarating, kishining tug’ilgan sanasi orqali hisob kitob qilingan raqamni qaytaruvchi metod.
Bu raqam(life_path_number) qanday hisob kitob qilinadi ? 
Misol uchun bizda 14-iyul 2002-yil da tug’ilgan inson bor ismi Jamshid.
1-qadam: Kun: 14 → 1 + 4 = 5
2-qadam: Oy: 07 → 0 + 7 = 7
3-qadam: Yil: 2002 → 2+0+0+2 = 4
4-qadam: Yig’indisi: 5 + 7 + 4 = 16
5-qadam: Yig’indisi: 16 → 1+6 = 7
Natija: 7 ✅
Javob: Jamshidni life_path_number i bu 7 ekan.

      👆🏻bu algoritm dinamik ishlashi kerak. faqat kursatilgan bir holat uchun ishlaydigan bo'lmasligi kerak !!!

Raqamga mos xabar ya’ni ta’rif oladigan metod yarating.
get_info_by_number() deb nomlangan va number nomli parametr qabul qilsin.
Raqamga mos ma’lumotni fayldan o’qib olishingiz kerak. Faylni yuklab olish
Fayl bir marta o'qib olinadi va number parametri orqali ma'lumot fayl ichidan qidirladi !

O’qib olish oson bo’lishi uchun # belgisi quyilgan raqam oldiga.

Shuningdek, qo’shimcha shu ishlar bajarilishi kerak:

Dastur ishga tushirilgandan so'ng ma'lumotlarni(first_name, last_name, ...) konsole orqali foydalanuvchidan so'rash.

Person klassining ob'ektini yaratib ungga so'ralgan ma'lumotlar berilsin.

get_info() metodini chaqiring va kishi haqida ma'lumotlarni ko'rsating.

get_life_path_number() metodini chaqiring va hisoblangan raqamni biron o’zgaruvchiga saqlab oling va konsolga chiqaring

get_info_by_number() metodini chaqiring va foydalanuvchiga chiqgan raqami bo’yicha berilgan psixologik maslahat(fayldagi ta’rif) ni qaytaring.

Kodni yuborishda formatini "Code" ga o'zgartirib yuboring,
"""

import datetime


class Person:
    """
      Person klassi konstruktori.
    """

    def __init__(self, first_name: str, last_name: str, age: int, email: str, birth_day: tuple[int, int, int]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.birth_day = birth_day

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._birth_day = value

    def get_info(self):
        return (
            f"First name: {self.first_name.title()} \n"
            f"Last name: {self.last_name.title()} \n"
            f"Age: {self.age} \n"
            f"Email: {self.email} \n"
            f"Birth day: {self.birth_day[2]:02d}-{self.birth_day[1]:02d}-{self.birth_day[0]}"
        )

    def get_life_path_number(self):
        """
          Hayot yo‘li raqamini hisoblash
        """
        def sum_digits(n):
            while n > 9:
                n = sum(int(digit) for digit in str(n))
            return n

        day, month, year = self.birth_day
        day_sum = sum_digits(day)
        month_sum = sum_digits(month)
        year_sum = sum_digits(year)

        total = day_sum + month_sum + year_sum
        life_path_number = sum_digits(total)
        return life_path_number

    def get_info_by_number(self, number):
        """Fayldan raqamga mos ma'lumotni o'qib qaytaradi"""
        with open("life_path_info.txt", encoding="utf-8") as file:
            content = file.read()
        sections = content.split("#")
        for section in sections:
            section = section.strip()
            if section and section.startswith(str(number)):
                # Raqamdan keyingi birinchi satrdan boshlab ta'rifni olish
                return section[len(str(number)):].lstrip(":-. \n\r\t")

        return "Bu raqam uchun ma'lumot topilmadi!"


if __name__ == "__main__":
    print("Ma'limotlaringizni kiriting:")
    first_name = input("Ismingiz: ")
    last_name = input("Familiyangiz: ")
    age = int(input("Yoshingiz: "))
    email = input("email: ")
    birth_date_str = input("Tug'ilgan sana: (yyyy-mm-dd): ")
    y, m, d = map(int, birth_date_str.split("-"))

    person1 = Person(first_name, last_name, age, email, (d, m, y))

    print("\nShaxsiy ma'lumotlar:")
    print(person1.get_info())

    life_path_number = person1.get_life_path_number()
    print(f"\nHayot yo'li raqamingiz: {life_path_number}")

    advice = person1.get_info_by_number(life_path_number)
    print(f"\nSiz uchun maxsus tavsiya:\n{advice}")
