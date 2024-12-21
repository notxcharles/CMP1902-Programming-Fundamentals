import time
import sys
import random
import numpy as np


def clear_console() -> None:
    print(chr(27) + "[2J")
    return

class WordleGame:
    GUESSTIME = 30
    def __init__(self, word_length: int = 5):
        self.lives_left = 6
        self.attempts = self.lives_left
        self.word_list = self.get_word_list()
        self.word_length = word_length
        self.word = self.choose_xletter_word(self.word_list).lower()
        self.character_frequency = self.get_character_frequency(self.word)
        self.previous_guesses = [] # list of the previous guessed words
        self.previous_clues = [] # list of all the previously generated clues
        # set with all the incorrect letters that the user has used. set because we want all elements to be unique
        self.incorrect_letters = set()
        self.play_game()
    
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
        with open("./AssessmentItem2/dictionary.txt", 'r') as file:
        # with open("dictionary.txt", 'r') as file:
            word_file = file.read()
            all_words_list = word_file.split()
        all_words_list = self.clean_word_list(all_words_list)
        return all_words_list

    def get_character_frequency(self, word: str) -> dict[str, int]:
        frequency = dict()
        for character in self.word:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency

    def choose_xletter_word(self, word_list: list[str]) -> str:
        xletter_word_list = []
        for word in word_list:
            if (len(word) == self.word_length):
                xletter_word_list.append(word)
        word = random.choice(xletter_word_list)
        return word

    def is_guess_valid(self, guess: str, start_time: float, end_time: float):
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

    def create_guess_feedback(self, guess: str, invalid_guess: bool = False) -> list[str]:
        feedback = ['_'] * self.word_length
        if (invalid_guess == True):
            return feedback

        character_frequency_guess = self.get_character_frequency(guess)
        for i, character in enumerate(guess):
            if character in self.word and guess[i] == self.word[i]:
                feedback[i] = '*'
                self.character_frequency[character] -= 1
                character_frequency_guess[character] -= 1
        for i, character in enumerate(guess):
            if character not in self.word:
                feedback[i] = '_'
                self.incorrect_letters.add(character)
                continue
            if character in self.word and self.character_frequency[character] != 0:
                feedback[i] = '+'
                self.character_frequency[character] -= 1
                continue
        return feedback

    def process_guess(self, guess: str) -> int:
        self.previous_guesses.append(guess)
        if (guess not in self.word_list):
            print(f"Incorrect! Must guess a valid word!")
            feedback = self.create_guess_feedback(guess, invalid_guess = True)
            self.previous_clues.append(feedback)
            return 2
        
        if (guess == self.word):
            print(f"Correct! The word was {guess}!")
            return 1

        feedback = self.create_guess_feedback(guess)
        self.previous_clues.append(feedback)
        return 0

    def clue_to_string(self, clue: list[str]) -> str:
        string = ""
        for i, character in enumerate(clue):
            string += character
            if (i != len(clue) - 1):
                string += " "
        return string

    def print_previous_clues(self):
        for i, clue in enumerate(self.previous_clues):
            clue_string = self.clue_to_string(clue)
            if self.previous_guesses[i] in self.word_list:
                print(f"Turn {i + 1}/{self.attempts}: {clue_string}   {self.previous_guesses[i]}")
            else:
                print(f"Turn {i + 1}/{self.attempts}: {clue_string}   invalid word: {self.previous_guesses[i]}")
        return

    def create_round_display(self):
        # Called after each time console is cleared
        print(f"Lives Left: {self.lives_left}")
        print(f"Incorrect letters: {self.incorrect_letters}")
        print(f"word to guess: {self.word}") # TODO: REMOVE THIS LATER
        self.print_previous_clues()
        return
            
    def show_game_end_screen(self, game_won: bool):
        if (game_won):
            print(f"Congratulations, you've guessed the correct answer - {self.word}")
            print(f"It took {self.attempts} attempts, {self.lives_left} lives remaining")
            if (len(self.previous_guesses)) == 1:
                print(f"It took {self.attempts - self.lives_left + 1} turn!")
            else:
                print(f"It took {self.attempts - self.lives_left + 1} turns!")
        else:
            print(f"You've run out of lives! The word was {self.word}")
        self.print_previous_clues()
        return

    def play_game(self):
        print(f"lives left: {self.lives_left}")
        print(f"Trying to guess:\n{self.word}")
        while self.lives_left > 0:
            start_time = time.time()
            guess = input(f"You have 30 seconds to guess a {len(self.word)} letter word:\n").lower()
            end_time = time.time()

            if (not self.is_guess_valid(guess, start_time, end_time)):
                self.lives_left = self.lives_left - 1
                print(f"Lives left: {self.lives_left}")
                time.sleep(2)
                clear_console()
                self.create_round_display()
                continue

            outcome = self.process_guess(guess)
            if (outcome == 1):
                # player has guessed the correct answer
                clear_console()
                self.show_game_end_screen(game_won=True)
                return
            elif (outcome == 0):
                # player has made an incorrect guess
                self.lives_left = self.lives_left - 1
            elif (outcome == 2):
                # must guess a word
                self.lives_left = self.lives_left - 1
            time.sleep(2)
            clear_console()
            self.create_round_display()

        # Out of lives
        clear_console()
        self.show_game_end_screen(game_won=False)
        
    
    
def play_game():
    wordle_game = WordleGame(5)


def main():
    play_game()
    return

main()
