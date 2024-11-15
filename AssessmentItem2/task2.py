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
    
    