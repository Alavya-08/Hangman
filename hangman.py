# required libraries for this game to play 
import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)   # <<---this will choose a random word for us from the list 
    
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in word

    alphabet = set(string.ascii_uppercase)

    used_letters = set() #what the user has guessed
    
    lives = 6  #total lives a user will get

    # storing/getting  user input 
    while len(word_letters)> 0 and lives> 0:

        # letters used
        print(f"You have {lives} left and You have used:"," ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        print("Current Word is :"," ".join(word_list))
        user_letter = input("Guess a Word:").upper() 
        
        #  main ---logic 
        if (user_letter in alphabet - used_letters):
            used_letters.add(user_letter)
            if (user_letter in word_letters):
                word_letters.remove(user_letter)
            else:
                lives -= 1 # substract from 6 if the word is wrong
                print("Letter is not in the Word.")
        elif (user_letter in used_letters):
            print("You have already used that character.Please try again!!")
        else:
            print("Invalid Character.Please try Again")       
    
    # get here when len(words_letters) == 0  or lives == 0
    if (lives == 0):
        print(f"Sorry, You Died. The word was {word}")
    else:
        print(f"You have guessed the {word}!!")

# taking input/guess from the user 
user_input = input("Guess a Word:")

# run the code 
hangman()

    
        