"""
Created on Thu Fri 20 15:31:14 2025

33-dars. Fayllar bilan ishlash. Pickle

@author: uktam
"""
import pickle
with open('info', 'rb') as file: # 'info' faylini binar formatda o'qish
  # Fayldan talabalarni o'qib olamiz
  talaba1 = pickle.load(file)
  talaba2 = pickle.load(file)
  talaba3 = pickle.load(file)
  
# O'qilgan talabalarni chiqaramiz
print("O'qilgan talabalar:")  
print(talaba1)
print(talaba2)
print(talaba3)