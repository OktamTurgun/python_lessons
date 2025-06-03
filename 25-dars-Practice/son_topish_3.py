import random


def son_top(x=10):
    """Foydalanuvchi kompyuter o'ylagan sonni topuvchi funksiya
    args:
        x (int): Foydalanuvchi o'ylagan sonning maksimal qiymati
    return:
        taxminlar (int): Foydalanuvchining sonni topish uchun sarflagan taxminlari soni
    """
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi?")
    taxminlar = 0

    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if taxmin < tasodifiy_son:
            print(f"Xato! Men o'ylagan son {taxmin} dan kattaroq. Yana urinib ko'ring.")

        elif taxmin > tasodifiy_son:
            print(
                f"Xato! Men o'ylagan son {taxmin} dan kichikroq. Yana urinib ko'ring."
            )

        else:
            break
    print(f"Tabriklayman! Siz {taxmin} sonini {taxminlar} urunishda topdingiz!")
    return taxminlar


def son_top_pc(x=10):
    """Kompyuter foydalanuvchi o'ylagan sonni topuvchi funksiya
    args:
        x (int): Foydalanuvchi o'ylagan sonning maksimal qiymati
    return:
        taxminlar (int): Kompyuterning sonni topish uchun sarflagan taxminlari soni
    """
    input(f"\nEndi siz 1 dan {x} gacha son o'ylang va Enter ni bosing...")
    low, high = 1, x
    taxminlar = 0

    while True:
        taxminlar += 1
        if low != high:
            taxmin = random.randint(low, high)
        else:
            taxmin = low
        javob = input(
            f"Siz {taxmin} soninio'yladingiz, to'g'rimi? (To'g'ri (t), kattaroq (k), kichik (kich)): "
        ).lower()
        if javob == "kich":
            high = taxmin - 1
        elif javob == "k":
            low = taxmin + 1
        else:
            break
    print(f"Kompyuter {taxmin} sonini {taxminlar} urunishda topdi!")
    return taxminlar


def play_game(x=10):
    """Foydalanuvchi va kompyuter o'rtasida son topish o'yini"""
    print("=== SON TOPISH O'YINI ===")
    yana_oynaymizmi = True
    user_wins = 0
    comp_wins = 0
    tie = 0
    while yana_oynaymizmi:
        print("\n=== Game started! ===")
        user_attampt = son_top(x)
        pc_attempt = son_top_pc(x)
        if user_attampt > pc_attempt:
            print(f"Yutdim! {pc_attempt}- urunishda")
            comp_wins += 1
        elif user_attampt < pc_attempt:
            print(f"Siz Yutdingiz! {user_attampt}-urunishda!")
            user_wins += 1
        else:
            print(f"Durrang: {user_attampt} = {pc_attempt} urunish")
            tie += 1
        # Natijalarni chiqarish
        print(
            f"\nHozirgi hisob: Foydalanuvchi {user_wins} - Kompyuter {comp_wins} durrang {tie}"
        )
        yana_oynaymizmi = input("Yana o'ynaymizmi? (ha/yo'q): ").lower()
        if yana_oynaymizmi != "ha":
            print("O'yin tugadi. Rahmat!")
            yana_oynaymizmi = False
            print(
                f"Final hisob: Foydalanuvchi {user_wins} - Kompyuter {comp_wins} durrang {tie}"
            )


if __name__ == "__main__":
    play_game(10)
