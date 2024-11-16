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
    character_frequency = dict()
    def __init__(self, lives = 5, word_length = 5):
        self.lives_left = lives
        self.attempts = lives
        self.word = self.choose_xletter_word(all_words_list, word_length).lower()
        self.word_length = word_length
        self.previous_guesses = [] # list of the previous guessed words
        self.previous_clues = [] # list of all the previously generated clues
        # set with all the incorrect letters that the user has used. set because we want all letters to be unique
        self.incorrect_letters = set() 
        
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
    
    def process_guess(self, guess: str) -> int:
        if (guess == self.word):
            print(f"Correct! The word was {guess}!")
            return 1
        
        feedback = [None] * self.word_length
        for i, character in enumerate(guess):
            print(f"looking at {character=}, pos {i}")
            if character not in self.word:
                feedback[i] = '_'
                self.incorrect_letters.add(character)
                continue
            if character in self.word and character == self.word[i]:
                feedback[i] = '*'
                continue
            if character in self.word:
                feedback[i] = '+'
                continue
        
        self.previous_guesses.append(guess)
        self.previous_clues.append(feedback)
        print(feedback)
        return 0
    
    def create_display(self):
        # Called after each time console is cleared
        print(f"Lives Left: {self.lives_left}")
        print(f"Incorrect letters: {self.incorrect_letters}\n")
        print(self.word)
        for i, clue in enumerate(self.previous_clues):
            print(f"Turn {i+1}/{self.attempts}: {clue}   {self.previous_guesses[i]}")
        
    
    
def play_game():
    wordle_game = WordleGame(5, 5)
    print(f"Trying to guess:\n{wordle_game.word}")
    
    while wordle_game.lives_left > 0:
        start_time = time.time()
        guess = input("You have 30 seconds to guess a 5 letter word").lower()
        end_time = time.time()
        
        if (not wordle_game.is_guess_valid(guess, start_time, end_time)):
            lives_left = lives_left - 1
            time.sleep(5)
            clear_console()
            continue
        
        outcome = wordle_game.process_guess(guess)
        if (outcome == 1):
            # player has guessed the correct answer
            print("Congratulations!")
        elif (outcome == 0):
            # player has made an incorrect guess
            print("Incorrect guess")
            wordle_game.lives_left = wordle_game.lives_left - 1
        # print(f"{guess}")
        time.sleep(5)
        clear_console()
        wordle_game.create_display()
    
    print("Out of the loop")

def main():
    play_game()
    return

main()