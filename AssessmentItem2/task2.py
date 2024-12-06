import time, sys, random
import numpy as np


def clear_console() -> None:
    print(chr(27) + "[2J")
    return 

class WordleGame:
    GUESSTIME = 30
    def __init__(self, lives: int = 5, word_length: int = 5):
        self.lives_left = lives
        self.attempts = lives
        self.word_list = self.get_word_list()
        self.word = self.choose_xletter_word(self.word_list, word_length).lower()
        self.word_length = word_length
        self.previous_guesses = [] # list of the previous guessed words
        self.previous_clues = [] # list of all the previously generated clues
        # set with all the incorrect letters that the user has used. set because we want all elements to be unique
        self.incorrect_letters = set() 
    
    def clean_word_list(self, word_list: list[str]) -> list[str]:
        # Some words contain the character ' , so lets ignore those words 
        # TODO: remove all characters from string (not just ')
        new_word_list = []
        for word in word_list:
            if ('\'' not in word):
                new_word_list.append(word)
        return new_word_list

    def get_word_list(self) -> list[str]:
        # I couldn't enter debug mode without referencing the folder
        # with open("./AssessmentItem2/dictionary.txt", 'r') as file:
        with open("dictionary.txt", 'r') as file:
            word_file = file.read()
            all_words_list = word_file.split()
        all_words_list = self.clean_word_list(all_words_list)
        return all_words_list

    def choose_xletter_word(self, word_list: list[str], word_length: int) -> list[str]:
        xletter_word_list = []
        for word in word_list:
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
        # TODO: need to check if it is a valid word (check in word list)
        return True
    
    def process_guess(self, guess: str) -> int:
        self.previous_guesses.append(guess)
        if (guess not in self.word_list):
            return 2
        
        if (guess == self.word):
            # print(f"Correct! The word was {guess}!")
            return 1
        
        feedback = [None] * self.word_length
        for i, character in enumerate(guess):
            # print(f"looking at {character=}, pos {i}")
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
        
        self.previous_clues.append(feedback)
        return 0
    
    def create_display(self):
        # Called after each time console is cleared
        print(f"Lives Left: {self.lives_left}")
        print(f"Incorrect letters: {self.incorrect_letters}\n")
        print(f"word to guess: {self.word}") # TODO: REMOVE THIS LATER
        for i, clue in enumerate(self.previous_clues):
            print(f"Turn {i+1}/{self.attempts}: {clue}   {self.previous_guesses[i]}")
        return
            
    def show_game_end_screen(self, game_won: bool):
        if (game_won):
            print(f"Congratulations, you've guessed the correct answer - {self.word}")
            print(f"It took {len(self.previous_guesses)} turns!")
        else:
            print(f"You've run out of lives! The word was {self.word}")
        print("")
        for i, clue in enumerate(self.previous_clues):
            print(f"Turn {i+1}/{self.attempts}: {clue}   {self.previous_guesses[i]}")
        return
        
    
    
def play_game():
    wordle_game = WordleGame(5, 5)
    print(f"Trying to guess:\n{wordle_game.word}")
    
    while wordle_game.lives_left > 0:
        start_time = time.time()
        guess = input("You have 30 seconds to guess a 5 letter word:\n").lower()
        end_time = time.time()
        
        if (not wordle_game.is_guess_valid(guess, start_time, end_time)):
            lives_left = lives_left - 1
            time.sleep(5)
            clear_console()
            continue
        
        outcome = wordle_game.process_guess(guess)
        if (outcome == 1):
            # player has guessed the correct answer
            clear_console()
            wordle_game.show_game_end_screen(game_won = True)
            # TODO: After solving first time, show_game_end_screen shows "it took 0 turns!"
            return
        elif (outcome == 0):
            # player has made an incorrect guess
            print("Incorrect guess! You lose a life")
            wordle_game.lives_left = wordle_game.lives_left - 1
        elif (outcome == 2):
            print("Guess is not a word! You lose a life")
            wordle_game.lives_left = wordle_game.lives_left - 1
        time.sleep(5)
        clear_console()
        wordle_game.create_display()
    
    # Out of lives
    wordle_game.show_game_end_screen(game_won = False)

def main():
    play_game()
    return

main()

# Potential errors:
# 1. word to guess was "boats"
#       guessing the word "boots" returned **+**
#       instead, the intended behaviour should have been **_**, with the second 'o' not belonging
#       I need to check if this should have been in the incorrect letters set

# 2. after guessing the correct word, the "congratulations, you've guessed the correct answer" line should be proceeded with a clear_console()

