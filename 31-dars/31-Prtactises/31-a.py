"""
Loyiha: Oddiy ATM Terminali (Inkapsulyatsiya asosida)
"""
class BankHisobi:
    """BankHisobi klassi - foydalanuvchi hisobini boshqaradi (inkapsulyatsiya bilan)"""
    
    def __init__(self, ism, balans, pin):
        # Ochiq (public) xususiyat - ismni bemalol chaqirish mumkin
        self.ism = ism
        
        # Himoyalangan (protected) xususiyat - odatda tashqaridan chaqirilmaydi
        self._balans = balans
        
        # Yashirin (private) xususiyat - tashqaridan to‘g‘ridan-to‘g‘ri kira olmaysiz
        self.__pin = pin

    def balansni_korish(self, kiritilgan_pin):
        """PIN to‘g‘ri bo‘lsa balansni ko‘rsatadi"""
        if kiritilgan_pin == self.__pin:
            return f"Balansingiz: {self._balans} so‘m"
        else:
            return "Xatolik: PIN noto‘g‘ri!"

    def pul_yuklash(self, miqdor, pin_kiritilgan):
        """PIN to‘g‘ri bo‘lsa balansga pul qo‘shadi"""
        if pin_kiritilgan != self.__pin:
            return "Xatolik: PIN noto‘g‘ri!"
        if miqdor <= 0:
            return "Xatolik: Miqdor musbat bo‘lishi kerak"
        
        self._balans += miqdor
        return f"{miqdor} so‘m qo‘shildi. Yangi balans: {self._balans} so‘m"

    def pul_yechish(self, miqdor, pin_kiritilgan):
        """PIN to‘g‘ri bo‘lsa balansdan pul yechadi"""
        if pin_kiritilgan != self.__pin:
            return "Xatolik: PIN noto‘g‘ri!"
        if miqdor <= 0:
            return "Xatolik: Miqdor musbat bo‘lishi kerak"
        if miqdor > self._balans:
            return "Xatolik: Hisobda yetarli mablag‘ yo‘q"
        
        self._balans -= miqdor
        return f"{miqdor} so‘m yechildi. Qolgan balans: {self._balans} so‘m"

    def pinni_almashtirish(self, eski_pin, yangi_pin):
        """PIN parolni yangilash uchun metod"""
        if eski_pin == self.__pin:
            self.__pin = yangi_pin
            return "✅ PIN muvaffaqiyatli yangilandi"
        else:
            return "❌ Eski PIN noto‘g‘ri!"

# Test qilish: Foydalanuvchi bilan muloqotga o‘xshash sinov
hisob = BankHisobi("Uktam", 150000, "4321")

print(hisob.balansni_korish("1234"))      # ❌ noto‘g‘ri pin
print(hisob.balansni_korish("4321"))      # ✅ Balansingiz: 150000 so‘m

print(hisob.pul_yuklash(50000, "4321"))   # ✅ 50000 so‘m qo‘shildi. Yangi balans: 200000 so‘m
print(hisob.pul_yechish(300000, "4321"))  # ❌ Xatolik: Hisobda yetarli mablag‘ yo‘q
print(hisob.pul_yechish(20000, "0000"))   # ❌ Xatolik: PIN noto‘g‘ri
print(hisob.pul_yechish(20000, "4321"))   # ✅ 20000 so‘m yechildi. Qolgan balans: 180000 so‘m

print(hisob.pinni_almashtirish("4321", "1111"))  # ✅ PIN muvaffaqiyatli yangilandi
print(hisob.balansni_korish("4321"))      # ❌ Xatolik: PIN noto'g'ri!
print(hisob.balansni_korish("1111"))      # ✅ Balansingiz: 180000 so‘m (yangi pin bilan ishlaydi)

'''
O'rganiladigan muhim tushunchalar.

| Tushuncha           | Nimani anglatadi                                              |
| ------------------- | ------------------------------------------------------------- |
| `__pin`             | Private (faqat klass ichida ishlatiladi)                      |
| Getter              | `balansni_korish()` — ma’lumotni olish usuli                  |
| Setter              | `pinni_almashtirish()` — ma’lumotni yangilash usuli           |
| Nazorat             | PIN noto‘g‘ri bo‘lsa, amallar bajarilmaydi                    |
| Xatolarni qaytarish | Har bir metod noto‘g‘ri holatda foydalanuvchini ogohlantiradi |

'''