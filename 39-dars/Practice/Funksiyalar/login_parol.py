"""
Mavzu: Login-parol tekshirishning turli usullari
Muallif: Uktam Turgunov
Sana: 2025-07-07
"""


# 1. ASOSIY FUNKSIYA
def check_credentials_basic():
    """Foydalanuvchidan login va parol so'rab, to'g'riligini tekshiradi"""
    correct_login = "admin"
    correct_password = "1234"

    login = input("Login kiriting: ")
    password = input("Parol kiriting: ")

    if login == correct_login and password == correct_password:
        print(f"Xush kelibsiz, {login.title()}!")
    else:
        print("Login yoki parol noto'g'ri!")


# 2. EXCEPTION BILAN TEKSHIRISH
class LoginError(Exception):
    """Login/parol xatosi uchun maxsus exception"""
    pass


def check_with_exception(login: str, password: str) -> str:
    """Xatoliklarni exception orqali qaytaradi"""
    if login == "admin" and password == "1234":
        return f"Xush kelibsiz, {login.title()}!"
    raise LoginError("Login yoki parol noto'g'ri!")


# 3. LUG'AT BILAN TEKSHIRISH
def check_with_dict(login: str, password: str, users: dict = None) -> bool:
    """Lug'atda login-parol mavjudligini tekshiradi"""
    users = users or {"admin": "1234"}
    return users.get(login) == password


# 4. LAMBDA FUNKSIYASI
def check_with_lambda(
    login, password): return login == "admin" and password == "1234"


# 5. FAYLDAN O'QIB TEKSHIRISH
def check_from_file(login: str, password: str, filename: str = "users.txt") -> bool:
    """Fayldan login-parollarni o'qib tekshiradi"""
    try:
        with open(filename) as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if user == login and pwd == password:
                    return True
    except FileNotFoundError:
        print("Fayl topilmadi!")
    return False


# 6. KLASS ORQALI TEKSHIRISH
class Authenticator:
    """Login-parol tekshirish uchun klass"""

    def __init__(self, login: str = "admin", password: str = "1234"):
        self.correct_login = login
        self.correct_password = password

    def verify(self, login: str, password: str) -> bool:
        """Login-parolni tekshiradi"""
        return login == self.correct_login and password == self.correct_password

    def authenticate(self) -> bool:
        """Foydalanuvchidan ma'lumot olib tekshiradi"""
        login = input("Login: ")
        password = input("Parol: ")

        if self.verify(login, password):
            print(f"Xush kelibsiz, {login}!")
            return True

        print("Noto'g'ri login yoki parol!")
        return False


# Test qilish
if __name__ == "__main__":
    print("1. Asosiy funksiya:")
    check_credentials_basic()

    print("\n2. Exception bilan:")
    try:
        print(check_with_exception("admin", "1234"))
    except LoginError as e:
        print(e)

    print("\n3. Lug'at bilan:")
    print(check_with_dict("admin", "1234"))

    print("\n4. Lambda bilan:")
    print(check_with_lambda("admin", "1234"))

    print("\n5. Fayldan o'qib:")
    print(check_from_file("admin", "1234"))

    print("\n6. Klass orqali:")
    auth = Authenticator()
    auth.authenticate()
