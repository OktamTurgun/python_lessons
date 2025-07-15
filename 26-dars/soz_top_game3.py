import random
from uzwords import words

# def get_word():
#   word = random.choice(words)
#   while "-" in word or " " in word:
#       word = random.choice(words)
#   return word.upper()

# def display_word(word, guessed_letters):
#   display = ""
#   for letter in word:
#       if letter in guessed_letters:
#           display += letter + " "
#       else:
#           display += "_ "
#   return display.strip()

# def play():
#   word = get_word()
#   guessed_letters = set()
#   attempts = 6

#   print("So'z topish o'yiniga xush kelibsiz!")
#   print("So'z:", display_word(word, guessed_letters))

#   while attempts > 0 and set(word) != guessed_letters:
#       guess = input("Harf kiriting: ").upper()
#       if guess in guessed_letters:
#           print("Bu harfni avval kiritgansiz.")
#       elif guess in word:
#           guessed_letters.add(guess)
#           print("To'g'ri!")
#       else:
#           attempts -= 1
#           print(f"Noto'g'ri! Qolgan urinishlar: {attempts}")
#       print("So'z:", display_word(word, guessed_letters))

#   if set(word) == guessed_letters:
#       print(f"Tabriklaymiz! So'z topildi: {word}")
#   else:
#       print(f"Afsus, urinishlar tugadi. So'z: {word}")

# if __name__ == "__main__":
#   play()
  
def get_words():
  word = random.choice(words)
  while "_" in word or " " in word:
    word = random.choice(words)
  return word.upper()

def display(user_letters, word):
  display_letter = ""
  for letter in word:
    if letter in user_letters.upper():
      display_letter += letter
    else:
      display_letter += "_"
  return display_letter

def play_game():
    word = get_words()
    word_letters = set(word)
    user_letters = ''
    print(f"Men {len(word)} xonali so'z o'yladim topa olasizmi?: ")

    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print("Siz kiritgan harflar", ", ".join(sorted(user_letters)))
            
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print(f"Xato! '{letter}' harfini oldin kiritgansiz.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"Juda to'gri! '{letter}' harfi so'zda bor")
        else:
            print(f"Noto'g'ri kiritsh! '{letter}' harfi so'zda yo'q.")
        user_letters += letter
    print(f"{word} so'zini {len(user_letters)} urunishda topdingiz!")
    
    play_again = input("Yana o'ynaysizmi? (yes/no): ")
    if play_again == 'yes':
        play_game()
    else:
        print("O'yin uchun raxmat")
        
if __name__ =="__main__":
    play_game()
    
            
            
            
            
            
            
            



