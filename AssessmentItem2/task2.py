import time, sys, random
import numpy as np

# I couldn't enter debug mode without referencing the folder
# with open("./AssessmentItem2/dictionary.txt", 'r') as file:
with open("dictionary.txt", 'r') as file:
    word_file = file.read()
all_words_list = word_file.split()

def clean_wordlist(word_list: list[str]) -> list[str]:
    new_word_list = []
    for word in word_list:
        # Some words contain the character ' , so lets ignore those words 
        if ('\'' not in word):
            new_word_list.append(word)
    return new_word_list

all_words_list = clean_wordlist(all_words_list)

def clear_console():
    print(chr(27) + "[2J")
    return 

class WordleGame:
    GUESSTIME = 30
    def __init__(self, lives = 5, word_length = 5):
        self.lives_left = lives
        self.word = self.choose_xletter_word(all_words_list, word_length).lower()
        self.word_length = word_length
        
    def choose_xletter_word(self, list_of_words: list[str], word_length: int) -> list[str]:
        xletter_word_list = []
        for word in list_of_words:
            if (len(word) == word_length):
                xletter_word_list.append(word)
        word = random.choice(xletter_word_list)
        return word
    
    def is_guess_valid(self, guess: str, start_time: int, end_time: int):
        if (not guess.isalpha()):
            print("Your guess may only contain letters")
            return False
        if (len(guess) != self.word_length):
            print(f"You must guess a {self.word_length} letter word")
            return False
        if (end_time - start_time > self.GUESSTIME):
            print(f"You must guess within {self.GUESSTIME} seconds")
            return False
        return True
    
    
def play_game():
    wordle_game = WordleGame(5, 5)
    print(f"Trying to guess:\n{wordle_game.word}")
    lives_left = wordle_game.lives_left
    
    while lives_left >= 0:
        start_time = time.time()
        guess = input("You have 30 seconds to guess a 5 letter word").lower()
        end_time = time.time()
        if (not wordle_game.is_guess_valid(guess, start_time, end_time)):
            lives_left = lives_left - 1
            time.sleep(5)
            clear_console()
            continue
        
        print(f"{guess}")
        time.sleep(5)
        clear_console()
        
    else:
        print(f"No lives left! You lose!")

def main():
    play_game()
    return

main()