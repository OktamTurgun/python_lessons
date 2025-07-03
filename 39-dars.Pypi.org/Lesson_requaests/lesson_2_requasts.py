"""
📌 Mavzu: Python tashqi kutubxonasi. pypi.org
📦 Modul: requests
✍️ Muallif: Uktam Turgunov
📅 Sana: 2025-07-03

requests — bu HTTP so‘rovlarni yuborish, API'lar bilan ishlash va
veb sahifalardan ma’lumot olish uchun eng mashhur Python kutubxonasi.
Rasmiy hujjat: https://docs.python-requests.org
"""

import requests
from pprint import pprint  # JSON ma’lumotlarni chiroyli ko‘rsatish uchun
# 🌐 1. Web sahifani olish (GET metodi)

url = "https://kun.uz/news/main"
response = requests.get(url)
print("✅ Sahifa kodi:", response.status_code)
# print(response.text[:500])  # Sahifaning birinchi 500 belgisi

# 🌍 2. API bilan ishlash — restcountries API

country = "Uzbekistan"
url = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(url)
r_json = r.json()[0]  # Faqat birinchi natija
print("🇺🇿 Davlat:", r_json['name']['common'])
print("🏙 Poytaxt:", r_json['capital'][0])
print("📍 Hudud:", r_json['region'])
print("👥 Aholi:", r_json['population'])

# ⚙️ 3. Asosiy requests funksiyalari
# ✅ 3.1. Oddiy GET so‘rovi

response = requests.get('https://api.github.com')
print("GitHub API status:", response.status_code)
pprint(response.json())

# ✅ 3.2. POST so‘rovi yuborish

data = {'name': 'Ahmad', 'job': 'developer'}
post_response = requests.post('https://httpbin.org/post', data=data)
print("POST javobi:")
pprint(post_response.json())

# ✅ 3.3. So‘rovga headers qo‘shish

headers = {'User-Agent': 'my-app/0.0.1'}
header_response = requests.get('https://httpbin.org/headers', headers=headers)
print("Custom headers:")
pprint(header_response.json())

# ✅ 3.4. params — URL parametrlar yuborish

params = {'q': 'python'}
param_response = requests.get('https://httpbin.org/get', params=params)
print("Parametr bilan URL:", param_response.url)

# ✅ 3.5. Fayl yuklab olish (rasm)

file_url = 'https://httpbin.org/image/png'
file_response = requests.get(file_url)
with open('downloaded_image.png', 'wb') as f:
    f.write(file_response.content)
print("📥 Fayl yuklab olindi: downloaded_image.png")

# ✅ 3.6. JSON formatida ma’lumot yuborish

json_data = {'username': 'user', 'password': 'pass'}
json_response = requests.post('https://httpbin.org/post', json=json_data)
print("JSON yuborildi:")
pprint(json_response.json())

# ✅ 3.7. Xatoliklarni ushlash (try-except)

try:
    bad_response = requests.get('https://thisurldoesnotexist.tld')
    bad_response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("🚫 Xatolik yuz berdi:", e)

# ✅ 3.8. Cookies bilan ishlash

cookie_response = requests.get(
    'https://httpbin.org/cookies/set/sessioncookie/123456789')
cookies = cookie_response.cookies
print("🍪 Cookies:", cookies.get_dict())

# ✅ 3.9. Session — ketma-ket so‘rovlar

with requests.Session() as session:
    session.get('https://httpbin.org/cookies/set/sessioncookie/abcdef')
    session_response = session.get('https://httpbin.org/cookies')
    print("🔁 Session cookies:")
    pprint(session_response.json())
'''
📌 Xulosa:
requests moduli bilan siz:

oddiy GET/POST so‘rovlar yubora olasiz,

API'lar bilan ishlay olasiz,

fayl yuklab olishingiz mumkin,

headers, params, cookies, JSON bilan ishlashingiz mumkin,

xatoliklarni tutishingiz mumkin.
'''
