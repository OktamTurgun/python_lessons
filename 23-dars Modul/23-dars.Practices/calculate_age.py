"""
Foydalanuvchidan tug'ilgan sanasini (YYYY-MM-DD formatida) so'rab,
uning yoshini (yil, oy, kun hisobida) hisoblang.
"""

from datetime import datetime


def calculate_age(birth_date: str) -> str:
    """
    Foydalanuvchining tug'ilgan sanasidan uning yoshini hisoblaydi.

      Args:
          birth_date: "YYYY-MM-DD" formatidagi tug'ilgan sana

      Returns:
          str: "Yil, oy, kun" formatida yosh
    """
    try:
        # Joriy sana va tug'ilgan sanani olish
        today = datetime.now()
        birth = datetime.strptime(birth_date, "%Y-%m-%d")

        if birth > today:
            return "Tug'ilgan sana kelajakda bo'lishi mumkin emas!"

        # Yoshni hisoblash
        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day

        # Agar oy yoki kun manfiy bo'lsa, hisobni tuzatish
        if days < 0:
            months -= 1
            # Oxirgi oyning kunlar soni
            last_month = today.month - 1 if today.month > 1 else 12
            last_year = today.year if today.month > 1 else today.year - 1
            days_in_last_month = (
                today.replace(day=1) - datetime(year=last_year, month=last_month, day=1)
            ).days
            days += days_in_last_month

        if months < 0:
            years -= 1
            months += 12

        return f"{years} yil, {months} oy, {days} kun"

    except ValueError:
        return "Noto'g'ri sana formati. Iltimos, 'YYYY-MM-DD' formatida kiriting."


# Foydalanuvchidan tug'ilgan sanani so'rash
if __name__ == "__main__":
    birth_date = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD): ")
    age = calculate_age(birth_date)
    print(f"Sizning yoshingiz: {age}")
