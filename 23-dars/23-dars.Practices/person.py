"""
person.py modulida:
- Shaxs ma'lumotlari moduli (funksiyalar asosida)

main.py da foydalanish misolini ko'rsating
"""


def create_person(name, age, gender, city, accupation=None):
    """
    Yangi shaxs ma'lumotlari lug'atini yaratadi

    Args:
        name (str): Shaxs ismi
        age (int): Yosh
        gender (str): Jinsi (male/female)

    Returns:
        dict: Shaxs ma'lumotlari lug'ati
    """
    person = {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city,
        "accupation": accupation,
    }
    return person


def person_to_dict(person):
    """
    Shaxs ma'lumotlarini lug'at ko'rinishida qaytaradi
      (Aslida bu funksiya kerak emas, chunki ma'lumotlar lug'atda,
      lekin metod sifatida ko'rsatish uchun qo'shildi)

      Args:
          person (dict): Shaxs ma'lumotlari lug'ati

      Returns:
          dict: Shaxs ma'lumotlari lug'ati
    """
    return person


def dict_to_person(data):
    """
    Lug'atdan shaxs ma'lumotlarini yaratadi

    Args:
        data (dict): Shaxs ma'lumotlari lug'ati

    Returns:
        dict: Yangi shaxs lug'ati
    """
    return create_person(
        data["name"], data["age"], data["gender"], data["city"], data.get("accupation")
    )


def display_person(person):
    """
    Shaxs ma'lumotlarini chiroyli shaklda konsolga chiqaradi

    Args:
        person (dict): Shaxs ma'lumotlari lug'ati
    """
    print("\nShaxs ma'lumotlari:")
    print("=" * 20, sep="\n")
    print(f"Ism: {person['name']}")
    print(f"Yosh: {person['age']}")
    print(f"Jins: {person['gender']}")
    print(f"Shahar: {person['city']}")
    if person["accupation"]:
        print(f"Kasb: {person['accupation']}")
    else:
        print("kasb: Noma'lum")
    print("-" * 20, sep="\n")


def update_person(person, **kwargs):
    """
    Shaxs ma'lumotlarini yangilaydi

    Args:
        person (dict): Shaxs ma'lumotlari lug'ati
        **kwargs: Yangilanishlar (kalit=qiymat)

    Returns:
        dict: Yangilangan shaxs ma'lumotlari lug'ati
    """
    for key, value in kwargs.items():
        if key in person:
            person[key] = value
    return person
