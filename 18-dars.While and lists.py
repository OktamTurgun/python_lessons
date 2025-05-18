# -*- coding: utf-8 -*-
"""
Created on Sun May 18 09:45:36 2025

Lesson 18. While & Lists

@author: uktam
"""
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrorlash != 'ha':
        break
print("Dostlringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())

'''
Foydalanuvchi bir necha ism kiritkandan keyin so'rov chiqarish (xa/yo'q')
'''
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     ism = input(f"{n}-do'stingiz ismini kiriting: ").strip()
#     if not ism:
#         break
#     ismlar.append(ism)
#     n += 1
#     if n > 3:  # 3 ta ismdan keyin so'rov chiqarish
#         takrorlash = input("Yana qo'shasizmi? (ha/yo'q) ").lower()
#         if takrorlash != 'ha':
#             break
# print("Dostlringiz ro'yxati:")
# for ism in ismlar:
#     print('-', ism.capitalize())
    
''' while yordamida dictionary'ni to'ldirish '''
# print("Do'stingiz yoshini saqlaymiz.")
# friends = {}
# ishora = True
# while ishora:
#     name = input("Do'stingiz ismini kiriting: ").strip()
#     age = input(f"{name.title()}ning yoshini kiriting: ").strip()
#     friends[name] = int(age)
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ").lower()
#     if javob == "yo'q":
#         ishora = False
        
# for name, age in friends.items():
#     print(f"{name.title():<8}: {age}-yoshda")
    
''' while loop yordamida listdan bir necha elementlarni o'chirib tashlash '''
cars = ['bmw', 'mercedes-benz', 'volvo', 'ford', 'general motors', 'tesla', 'ferrari', 'ford']
car = 'ford'
while car in cars:
    cars.remove(car)
print(cars)

''''''
students = ['john', 'alex', 'lucy', 'micheal', 'david', 'edvard', 'ben', 'tom', 'bruce']
graded_students = {} # Baholangan talabalar
while students: # Toki students listi bo'shaguncha quyidagi codni bajar
    student = students.pop()
    grade = input(f"Enter the {student.title()}'s grade: ") # Talabaning bahosini kiriting
    print(f"The {student.title()} was evaluated!") # Talaba baholandi
    graded_students[student] = int(grade)
    
for x, y in graded_students.items():
    print(f"{x.title():<10}-was graded with a score of {y}")
    
''''''
students = ['john', 'alex', 'lucy', 'micheal', 'david', 'edvard', 'ben', 'tom', 'bruce']
graded_students = {}

def get_valid_grade(student_name):
    while True:
        grade = input(f"Enter {student_name.title()}'s grade (0-100): ")
        if grade.isdigit() and 0 <= int(grade) <= 100:
            return int(grade)
        print("Invalid input! Please enter a number between 0 and 100.")

while students:
    student = students.pop()
    grade = get_valid_grade(student)
    print(f"{student.title()} was evaluated with grade {grade}")
    graded_students[student] = grade

print("\n=== Grading Results ===")
for student in sorted(graded_students):  # Sort alphabetically
    print(f"{student.title():<10} - Grade: {graded_students[student]:>3}")

# Additional statistics
if graded_students:
    average = sum(graded_students.values()) / len(graded_students)
    print(f"\nAverage grade: {average:.2f}")
    print(f"Highest grade: {max(graded_students.values())}")
    print(f"Lowest grade: {min(graded_students.values())}")

