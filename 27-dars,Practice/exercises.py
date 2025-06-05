"""
Created on Wed Jun 5 16:00:46 2025

27-dars. LISTS КИРИЛЛ-LOTIN Telegram bot

@author: uktam
"""
from transliterate import to_cyrillic, to_latin
import telebot
print("Kutubxona muvaffaqiyatli yuklandi!")

# TOKEN = '7891811969:AAEBAVEECCwJYvzYrke0inFR90V4WM8wOgs'
bot = telebot.TeleBot("7891811969:AAEBAVEECCwJYvzYrke0inFR90V4WM8wOgs", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Asssalomu aleykum, Xush kelibsiz!")
 
bot.infinity_polling()
 
# text = input("Matn kiriting: ")

# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))
    
