"""
04-dars: Python os kutubxonasi
Muallif: Uktam Turgunov
Sana: 2025-06-28

Ushbu darsda os kutubxonasi yordamida fayl va papkalar bilan ishlash, tizim buyruqlari va yo'llarni boshqarishni o'rganamiz:
 - current working directory (cwd)
 - papka yaratish, o'chirish
 - fayllar ro'yxatini olish
 - tizim bilan bog'lanish
"""

import os

# Joriy ishchi katalog (current working directory)
print("Joriy papka:", os.getcwd())

# Papkalar yaratish
os.makedirs("data/test", exist_ok=True)
print("data/test papkasi yaratildi")

# Fayllar ro'yxati
print("Joriy papkadagi fayllar:", os.listdir("."))

# Fayl yoki papka bormi?
print("README.md mavjudmi:", os.path.exists("README.md"))

# Faylmi yoki papkami?
print("README.md faylmi:", os.path.isfile("README.md"))
print("data papkami:", os.path.isdir("data"))

# Yo'lni birlashtirish
yol = os.path.join("data", "test", "info.txt")
print("Yangi yo'l:", yol)

# Tizim nomi va platforma
print("Tizim nomi:", os.name)  # nt (Windows), posix (Linux/Mac)

# Amaliy mashq: Fayl mavjud bo'lsa - o'qish, bo'lmasa - yaratish
def check_or_create(filename):
    if os.path.exists(filename):
        print(f"{filename} mavjud")
    else:
        with open(filename, "w") as f:
            f.write("Yangi fayl yaratildi")
        print(f"{filename} yaratildi")


check_or_create("data/test/info.txt")

# FAylni o'chirish
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} o'chirildi")
    else:
        print(f"{filename} mavjud emas")


delete_file("data/test/info.txt")

# Papkani o'chirish
def delete_directory(directory):
    if os.path.exists(directory):
        os.rmdir(directory)
        print(f"{directory} o'chirildi")
    else:
        print(f"{directory} mavjud emas")


delete_directory("data/test")

# Joriy ishchi katalogni o'zgartirish
def change(new_directory):
    try:
        os.chdir(new_directory)
        print(f"Joriy ishchi katalog {new_directory} ga o'zgartirildi")
    except FileNotFoundError:
        print(f"{new_directory} mavjud emas")
    except PermissionError:
        print(f"{new_directory} ga kirish ruxsati yo'q")


change("data")

# Joriy ishchi katalogni qayta tiklash
def reset_cwd():
    os.chdir("..")  # Joriy katalogdan bir daraja yuqoriga
    print("Joriy ishchi katalog qayta tiklandi:", os.getcwd())


reset_cwd()

# Tizim buyruqlarini bajarish
def run_command(command):
    result = os.popen(command).read()
    print(f"{command} natijasi:\n{result}")


# Windows uchun dir, Linux/Mac uchun ls
run_command("dir" if os.name == "nt" else "ls")

# Amaliy mashq: Faylga ma'lumot yozish va o'qish
def write_and_read_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"{filename} fayliga yozildi")
    with open(filename, "r") as f:
        data = f.read()
    print(f"{filename} faylidan o'qildi:\n{data}")


write_and_read_file("data/test/info.txt",
                    "Bu test fayli.\nUshbu fayl os kutubxonasi yordamida yaratildi.")
