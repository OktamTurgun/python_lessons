"""
Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan
ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
"""
class User:
  def __init__(self,username,email,age,password):
    self.username = username
    self.email = email
    self.age = age
    self.password = password

  def get_username(self):
    return self.username
  
  def get_email(self):
    return self.email

  def get_age(self):
    return self.age

  def check_password(self, password):
    return self.password == password
  
  def intro(self):
    return f"User: {self.username}, Email: {self.email}, Age: {self.age}"
  
user1 = User("Ali", "Example@gmail.com", 23, "password1")
user2 = User("Olim", "Example@gmail.com", 19, "password2")
user3 = User("Ahmad", "Example@gmail.com", 30, "password3")

print(user1.intro())
print(user2.intro())
print(user3.intro())