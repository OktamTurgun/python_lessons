"""
Mavzu: Practice with OOP.
Muallif: Uktam Turgunov
Sana: 2025-07-10

Vazifa: sinflar yozishni boshlash.
User klassi: ism, email va metodlari (masalan, emailni tekshiruvchi).
"""


class User:
    def __init__(self, ism, email, yosh=None, jins=None):
        self.ism = ism
        self.email = email
        self.yosh = yosh
        self.jins = jins

    def info(self):
        info_str = f"User: {self.ism} | Email: {self.email}"
        if self.yosh is not None:
            info_str += f" | Age: {self.yosh} yosh"
        if self.jins is not None:
            info_str += f" | Jinsi: {self.jins}"
        return info_str

    def email_tekshir(self):
        # Oddiy email tekshiruv
        return "@" in self.email and "." in self.email and len(self.email) > 5

    def yosh_oshir(self, n=1):
        if self.yosh is not None:
            self.yosh += n

    def email_ozgartir(self, yangi_email):
        self.email = yangi_email

    def __str__(self):
        return self.info()


# Ishlatish:
user1 = User("Uktam", "uktam@example.com", yosh=25, jins="Erkak")
print(user1)
if user1.email_tekshir():
    print("✅ Email to‘g‘ri.")
else:
    print("🚫 Email noto‘g‘ri.")

user1.yosh_oshir()
print("Yangi yosh:", user1.yosh)

user1.email_ozgartir("yangi_email@example.com")
print("Yangi email:", user1.email)
