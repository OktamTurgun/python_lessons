"""
Created on Wed Jun 25 12:43:14 2025

36-dars. Fynksiyalarni kekshirish. Unittest moduli 

@author: uktam
"""


def get_full_name(ism, familiya, otasi_ism=''):
    if otasi_ism:
        return f"{ism} {otasi_ism} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()
# print(get_full_name("alijon", "valiyev"))
