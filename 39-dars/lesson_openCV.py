"""
Mavzu: Python tashqi kutubxonasi. Pypi.org
Muallif: Uktam Turgunov
Sana: 2025-07-01
Mavzu: OpenCV (Computer Vision) moduli

🎯 OpenCV nima?
OpenCV (Open Source Computer Vision Library) — tasvirlar (rasmlar) va videolar bilan ishlash uchun ochiq manbali, juda kuchli kutubxona.

OpenCV yordamida quyidagilarni qilishingiz mumkin:
✅ Tasvirni ochish, ko‘rsatish va saqlash
✅ Ranglarni o‘zgartirish
✅ Filtrlar qo‘llash
✅ Ob’ekt aniqlash
✅ Kamera bilan ishlash

🔧 O‘rnatish
OpenCV’ni o‘rnatish juda oson:

bash

pip install opencv-python

"""


# 📂 Asosiy tushunchalar
# 1️⃣ Tasvirni yuklash va ko‘rsatish

import cv2

# rasmni yuklash
img = cv2.imread(
    r"C:\\Users\\User\\Documents\\GitHub\\python_lessons\\python_lessons\\39-dars.Pypi.org\\rasm.jpg")

# rasmni oynada ko‘rsatish
cv2.imshow("Mening Rasmim", img)

# klaviaturadan tugma bosilishini kutish
cv2.waitKey(0)

# barcha oynalarni yopish
cv2.destroyAllWindows()

# 2️⃣ Ranglarni o‘zgartirish


img = cv2.imread("rasm.jpg")

# rangni BGR → Gray o‘tkazish
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Kulrang Rasm", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3️⃣ Rasmni saqlash


img = cv2.imread("rasm.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_rasm.jpg", gray)

# 4️⃣ Kamera bilan ishlash


# 0 — default kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Kamera", frame)

    # ESC bosilsa chiqish
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

# 5️⃣ Rasmga matn yozish va chizish


img = cv2.imread("rasm.jpg")

# chiziq
cv2.line(img, (50, 50), (200, 200), (255, 0, 0), 3)

# doira
cv2.circle(img, (150, 150), 50, (0, 255, 0), -1)

# matn
cv2.putText(img, "Salom, OpenCV!", (10, 300), cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)

cv2.imshow("Chizilgan Rasm", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
# 🔷 Foydali funksiya va metodlar:

# Funksiya	                                          Tavsifi
# cv2.imread()	                                      Rasmni o‘qish
# cv2.imshow()	                                      Rasmni oynada ko‘rsatish
# cv2.imwrite()	                                      Rasmni faylga yozish
# cv2.cvtColor()	                                    Rangni o‘zgartirish
# cv2.VideoCapture()	                                Kamerani ishga tushirish
# cv2.line(), cv2.circle(), cv2.rectangle()	          Chizish
# cv2.putText()	                                      Rasmga matn yozish
# cv2.GaussianBlur(), cv2.Canny()	                    Filtrlar va chetlarni aniqlash
"""

'''
📋 Amaliy topshiriqlar:
✅ O‘zingizning rasmingizni yuklab, uni kulrangga o‘tkazing va saqlang.
✅ Kameradan 5 soniyalik video olishga harakat qiling.
✅ Rasmga o‘z ismingizni matn sifatida yozib chiqaring.

📚 Xulosa:
🔹 OpenCV — kompyuter ko‘rish (Computer Vision) uchun juda qulay va kuchli vosita.
🔹 Rasm va video bilan ishlashni osonlashtiradi.
🔹 Juda katta imkoniyatlarga ega: yuzni aniqlash, QR kod o‘qish, ob’ektlarni kuzatish va h.k.
'''
