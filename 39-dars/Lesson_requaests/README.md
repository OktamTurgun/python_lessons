
# 🧰 Python Requests moduli

![Python](https://img.shields.io/badge/Python-requests-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/lesson-complete-brightgreen)
![Author](https://img.shields.io/badge/author-Uktam%20Turgunov-lightgrey)

## 📌 Mavzu: Python tashqi kutubxonasi - `requests`

### 🗓 Sana: 2025-07-03

---

## 🧠 Maqsad

Ushbu darsda siz Python dasturlash tilida mashhur `requests` modulidan foydalanishni o‘rganasiz. Bu modul veb sahifalar yoki API'lar bilan HTTP orqali bog‘lanish imkonini beradi.

---

## 📦 `requests` kutubxonasi haqida

`requests` — HTTP so‘rovlar yuborish va javoblarni olish uchun juda qulay tashqi kutubxona. U orqali:

- GET/POST kabi HTTP so‘rovlar yuboriladi  
- JSON bilan ishlash mumkin  
- Fayllar yuklab olinadi  
- So‘rovga header, params, cookie va boshqa parametrlar qo‘shish mumkin  

📚 Rasmiy sayt: [https://docs.python-requests.org](https://docs.python-requests.org)

---

## ⚙️ O‘rnatish

```bash
pip install requests
```

---

## 🧪 Asosiy ishlatish usullari

### ✅ 1. `GET` so‘rovi

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

---

### ✅ 2. `POST` so‘rovi

```python
data = {'name': 'Ahmad', 'job': 'developer'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())
```

---

### ✅ 3. Parametrlar bilan so‘rov

```python
params = {'q': 'python'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)
```

---

### ✅ 4. Header yuborish

```python
headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.json())
```

---

### ✅ 5. JSON yuborish

```python
json_data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://httpbin.org/post', json=json_data)
print(response.json())
```

---

### ✅ 6. Fayl yuklab olish

```python
url = 'https://httpbin.org/image/png'
r = requests.get(url)
with open('downloaded_image.png', 'wb') as f:
    f.write(r.content)
```

---

### ✅ 7. Cookies bilan ishlash

```python
r = requests.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(r.cookies.get_dict())
```

---

### ✅ 8. Session orqali ko‘p so‘rovlar yuborish

```python
with requests.Session() as session:
    session.get('https://httpbin.org/cookies/set/sessioncookie/abcdef')
    r = session.get('https://httpbin.org/cookies')
    print(r.json())
```

---

### ✅ 9. Xatoliklarni tutish

```python
try:
    r = requests.get('https://notfound.tld')
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Xatolik:", e)
```

---

## 🌍 Amaliy API misoli: `restcountries.com`

```python
country = "Uzbekistan"
url = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(url)
data = r.json()[0]
print(data['capital'], data['region'], data['population'])
```

---

## ✅ Yakuniy natija

- Siz endi `requests` moduli yordamida API'lar bilan ishlash, fayllar yuklash, parametr va header yuborish, cookie va sessionlar bilan ishlashni bilasiz.
- Amaliy loyihalarda (masalan: valyuta kursi, ob-havo, davlat ma'lumotlari) API'lar bilan bog‘lanishda keng qo‘llaniladi.

---

## 📁 Fayl tarkibi

```bash
requests_lesson/
│
├── requests_demo.py       # Asosiy kod fayli
├── downloaded_image.png   # Yuklab olingan fayl (rasm)
└── README.md              # Darsga izoh hujjati
```

---

## 📚 Qo‘shimcha manbalar

- [Requests documentation](https://docs.python-requests.org/en/latest/)
- [HTTPBIN test sayti](https://httpbin.org)
- [REST Countries API](https://restcountries.com)

---

> Dars muallifi: **Uktam Turgunov**  
> GitHub: [github.com/your-profile](https://github.com/your-profile)
