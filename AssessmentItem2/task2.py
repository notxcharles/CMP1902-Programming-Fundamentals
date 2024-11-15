import time, sys, random
import numpy as np

with open("dictionary.txt", 'r') as file:
    word_file = file.read()
all_words_list = word_file.split()

def get_xletter_words(list_of_words: list[str], word_length: int) -> list[str]:
    xletter_word_list = []
    for word in list_of_words:
        if (len(word) == word_length):
            xletter_word_list.append(word)
    return xletter_word_list
    
five_letter_words = get_xletter_words(all_words_list, 5)
word = random.choice(five_letter_words)
print(word)