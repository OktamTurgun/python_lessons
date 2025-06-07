"""
Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan
ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi 
foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin 
(masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
"""
class User:
  def __init__(self,username,name,email,age,password):
    self.username = username
    self.name = name
    self.email = email
    self.age = age
    self.password = password

  def get_username(self):
    return self.username
  
  def get_name(self):
    return self.name
  
  def get_email(self):
    return self.email

  def get_age(self):
    return self.age

  def check_password(self, password):
    return self.password == password
  
  def get_info(self):
    return f"User: {self.username} Name: {self.name}, Email: {self.email}, Age: {self.age}"
  
user1 = User("1997ali","Ali Valiyev", "Example@gmail.com", 23, "ali1997valiyev")
user2 = User("olimjon1234","Olim Karinov", "Example@gmail.com", 19, "olim234790olim")
user3 = User("077ahmad","Ahmad Mirzo", "Example@gmail.com", 30, "olim77mirzo_07")

print(user1.get_info())
print(user2.get_info())
print(user3.get_info())

# Metodlarni chaqirish
print(user3.get_email()) # Example@gmail.com
print(user2.check_password("olim234790olim")) # True 
print(user2.check_password("olim23olim")) # False
print(user1.get_age()) # 23

# Obyekt xususiyatlarini o'zgartirish
user2.age = 24 # Yoshni yangilash
print(user2.get_age()) # 24

user1.email = 'ali@gmail.com'
print(user1.get_email()) # ali@gmail.com

# Exercises 2
import hashlib

class User:
    def __init__(self, username, name, email, age, password):
        self.username = username
        self.name = name
        self.email = email
        self.age = age
        self.password_hash = self._hash_password(password)
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self.password_hash == self._hash_password(password)
    
    def get_info(self):
        return f"User: {self.username}, Name: {self.name}, Email: {self.email}, Age: {self.age}"

# Foydalanish
user1 = User("1997ali", "Ali Valiyev", "ali@example.com", 23, "ali1997valiyev")
print(user1.get_info())
print(user1.check_password("notmypass"))  # False
print(user1.check_password("ali1997valiyev"))  # True

# Exercises 3
import hashlib 

class User:
    def __init__(self, username, name, email, age, password):
        self.username = username
        self.name = name
        self.email = email
        self.age = age
        self.password_hash = self._hash_password(password)  # Parol heshlangan holda saqlanadi

    def _hash_password(self, password):
        """Parolni SHA-256 yordamida heshlaydi"""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Parolni tekshiradi"""
        return self.password_hash == self._hash_password(password)

    def __str__(self):
        return f"User: {self.username}, Name: {self.name}, Email: {self.email}, Age: {self.age}"

# Test
user1 = User("1997ali", "Ali Valiyev", "ali@example.com", 23, "ali1997valiyev")
print(user1)  # __str__ metodi ishlaydi
print(user1.check_password("wrong_pass"))  # False
print(user1.check_password("ali1997valiyev"))  # True