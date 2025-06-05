"""
Created on Wed Jun 5 16:00:46 2025

27-dars. LISTS КИРИЛЛ-LOTIN Telegram bot

@author: uktam
"""
from transliterate import to_cyrillic, to_latin

text = input("Matn kiriting: ")

if text.isascii():
    print(to_cyrillic(text))
else:
    print(to_latin(text))
    
