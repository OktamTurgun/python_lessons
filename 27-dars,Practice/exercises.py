"""
Created on Wed Jun 5 16:00:46 2025

27-dars. LISTS КИРИЛЛ-LOTIN Telegram bot

@author: uktam
"""
from transliterate import to_cyrillic, to_latin
import telebot
print("Kutubxona muvaffaqiyatli yuklandi!")

TOKEN = '7891811969:AAEBAVEECCwJYvzYrke0inFR90V4WM8wOgs'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#   javob = "Asssalomu aleykum, Xush kelibsiz!"
#   javob += "\nMatn kiriting!"
#   bot.reply_to(message, javob)
  
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#   msg = message.text
#   javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg) 
  
#   bot.reply_to(message, javob(msg))
  
def convert_text(msg: str) -> str:
    """Matnni avtomatik tarjima qilish: lotin -> kirill yoki aksincha."""
    return to_cyrillic(msg) if msg.isascii() else to_latin(msg)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🖐 Assalomu alaykum!\n"
        "✍️ Matn yuboring, men uni avtomatik ravishda kirill ↔ lotin formatiga o‘giraman.\n"
        "🔁 Lotin yozuvi kirilsiz bo‘lsa – kirillga,\n"
        "🔁 Kirill yozuvi bo‘lsa – lotinga aylantiraman."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    converted = convert_text(message.text)
    bot.reply_to(message, converted)
	
 
bot.infinity_polling()
 
# text = input("Matn kiriting: ")

# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
    
