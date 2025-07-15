# # friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga 
# chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida
# mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, 
# mehmonlar ro'yxatiga qo'shing.

friends = []
friends.append("Ahmad")
friends.append("Abdurahmon")
friends.append("Alisher")
friends.append("Adham")
friends.append("Sohibjon")
friends.append("Sardor")

friends.remove("Alisher")
friends.remove("Ahmad")

friends.insert(0, "Sobir")
friends.insert(-1, "Tohir")
friends.insert(2, "Qobil")

guests = []

guests.append(friends.pop(2))
guests.append(friends.pop())
guests.append(friends.pop(-2))

print(f"Bugun keladigan o'rtoqlarim: {friends}, ammo kelgan do'stlarim: {guests}")