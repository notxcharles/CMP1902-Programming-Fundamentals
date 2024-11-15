import time, sys, random
import numpy as np

with open("dictionary.txt", 'r') as file:
    word_file = file.read()
all_words_list = word_file.split()

def clean_wordlist(word_list: list[str]) -> list[str]:
    new_word_list = []
    for word in word_list:
        if ('\'' not in word):
            new_word_list.append(word)
    
    return new_word_list
all_words_list = clean_wordlist(all_words_list)

class WordleGame:
    GUESSTIME = 30
    def __init__(self, lives = 5, word_length = 5):
        self.lives_left = lives
        self.word = self.choose_xletter_word(all_words_list, word_length)
        
    def choose_xletter_word(self, list_of_words: list[str], word_length: int) -> list[str]:
        xletter_word_list = []
        for word in list_of_words:
            if (len(word) == word_length):
                xletter_word_list.append(word)
        word = random.choice(xletter_word_list)
        return word
    
    
def play_game():
    wordle_game = WordleGame(5, 5)
    print(f"Trying to guess:\n{wordle_game.word}")
    lives_left = wordle_game.lives_left
    
    while lives_left >= 0:
        start_time = time.time()
        guess = input("You have 30 seconds to guess a 5 letter word")
        end_time = time.time()
        print(f"{start_time} | {end_time} | {end_time-start_time}")
        if (end_time-start_time > wordle_game.GUESSTIME):       
            lives_left = lives_left - 1
            print(f"Guess took too long & you've lost a life - {lives_left} remain")
            continue
        print(f"{guess}")
    else:
        print(f"No lives left! You lose!")

def main():
    play_game()
    return

main()