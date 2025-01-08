# task2.py - Charles Frederick Harrison 25320877
# Variant of the Wordle game
# This script will:
# > Randomly select one 5-letter word from dictionary.txt
# > During each turn the player provides a guess. Check if it is a real word, if not, lose a life (turn)
# > After each guess, provide a clue.
#   clue: * - letter and correct position, + - letter correct, _ letter not in answer
# > Multiple instances of the same letter will e assigned with either * or + only if the letter
#   appears multiple times
# > Player has the option to give up at any time
# > Player has 6 turns/lives. If the correct answer is found they win, otherwise they lose
# Desired Features:
# > Asks for an alias, lets users see past fasted times. Users time is also saved to file
# > After each turn, the code provides a list of all invalid characters that the user has used
# > Player is given 30 seconds to guess a word
# > Erroneous input is handled correctly
# Advanced Features:
# > Player has the option to use a hint once
# > Player can ask for help with the vocabulary
import time
import random

class WordleGame:
    GUESSTIME = 30
    def __init__(self) -> None:
        self.lives_left = 6
        self.max_attempts = self.lives_left
        self.word_list = self.get_word_list()
        self.word_length = 5
        self.valid_word_list = self.get_xletter_words(self.word_list, self.word_length)
        self.word = self.choose_xletter_word(self.valid_word_list).lower()
        self.characters = set()
        self.character_frequency = dict()
        self.player_name = ""
        self.previous_guesses = [] # list of the previous guessed words
        self.previous_clues= [] # list of all the previously generated clues
        # set with all the incorrect letters that the user has used. set because we want all elements to be unique
        self.incorrect_letters = set()
        self.correctly_guessed_letters = set()
        # correctly_positioned_letters will keep track of any letters that the
        # user has guessed that are in the correct positions
        # this is needed for vocab()
        self.correctly_positioned_letters = [None] * self.word_length
        self.valid_words = []
        self.hint_used = False
        self.hint = None
        self.hard_mode = False
        self. play_game()

    @staticmethod
    def clear_console() -> None:
        """Clears the console/terminal"""
        print(chr(27) + "[2J")
        return

    @staticmethod
    def clean_word_list(word_list: list[str]) -> list[str]:
        """Removes words that contain non-alphabet characters"""
        new_word_list = []
        for word in word_list:
            for char in word:
                if (not char.isalpha()):
                    break
            else:
                new_word_list.append(word)
        return new_word_list

    def get_word_list(self) -> list[str]:
        """Returns a list of all words in the dictionary"""
        with open("dictionary.txt", 'r') as file:
            word_file = file.read()
            all_words_list = word_file.split()
        all_words_list = self.clean_word_list(all_words_list)
        return all_words_list

    @staticmethod
    def get_character_frequency(word: str) -> dict[str, int]:
        """Returns a dictionary of the frequency of each character in a word"""
        # TODO: This could be further optimised to a list of length 26
        frequency = dict()
        for character in word:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency

    @staticmethod
    def get_xletter_words(word_list: list[str], word_length: int):
        """Returns a list of words that contain x number of letters"""
        xletter_word_list = []
        for word in word_list:
            if (len(word) == word_length):
                xletter_word_list.append(word)
        return xletter_word_list

    @staticmethod
    def choose_xletter_word(word_list: list[str]) -> str:
        """Returns a random word from a list of words that contain x number of letters"""
        word = random.choice(word_list)
        return word

    def player_chose_word_length(self, word_length: int) -> None:
        """Set the word length and generate a new word for the player to guess"""
        self.word_length = word_length
        self.valid_word_list = self.get_xletter_words(self.word_list, self.word_length)
        self.word = self.choose_xletter_word(self.valid_word_list).lower()
        self.word = "ogre" # DEBUGGING
        self.character_frequency = self.get_character_frequency(self.word)
        self.characters = set(self.word)
        self.correctly_positioned_letters = [None] * self.word_length
        return

    def get_valid_words(self) -> list[str]:
        """Returns a list of words that are valid for the current word length"""
        all_valid_words = []
        for word in self.valid_word_list:
            if (len(word) != self.word_length):
                continue

            # Word should not contain characters that are in self.incorrect_letters()
            skip_loop = False
            for i, character in enumerate(self.correctly_positioned_letters):
                if (character is None):
                    continue
                elif (character != word[i]):
                    # we can eliminate that word from the word list
                    skip_loop = True
                    break
            if (skip_loop):
                continue

            for character in self.correctly_guessed_letters:
                if character not in word:
                    skip_loop = True
                    break
            if (skip_loop):
                continue

            all_valid_words.append(word)
        return all_valid_words

    def generate_hint(self) -> None:
        """Generates a hint for the player.The hint is a
        single character that has not already been guessed"""
        if (self.hint_used):
            return
        unguessed_characters = self.characters - self.correctly_guessed_letters
        character = random.choice(list(unguessed_characters))
        self.hint = character
        self.hint_used = True
        self.lives_left -= 1
        self.previous_clues.append([])
        self.correctly_guessed_letters.add(character)
        return
    
    def is_hard_mode_guess_valid(self, guess: str):
        """Returns true if the guess is valid with hard_mode rules"""
        if (len(self.correctly_guessed_letters) == 0):
            return True
        for character in self.correctly_guessed_letters:
            if (character not in guess):
                return False
        # Check that the guessed character is in a previously guessed correct position
        # "The hard mode requires players to include letters marked as 
        # * and + in subsequent guesses" does not mean that previously guessed characters
        # must be in the correct position
        # for i, character in enumerate(guess):
        #     if (self.correctly_positioned_letters[i] == None):
        #         continue
        #     if (character != self.correctly_positioned_letters[i]):
        #         return False
        
        return True

    def is_guess_valid(self, guess: str, start_time: float, end_time: float) -> bool:
        """Returns True if the guess is valid. Checks for
        alphabetic characters, length, and guess time"""
        if (not guess.isalpha()):
            print("Your guess may only contain letters")
            return False
        if (len(guess) != self.word_length):
            print(f"You must guess a {self.word_length} letter word")
            return False
        if (end_time - start_time > self.GUESSTIME):
            print(f"You must guess within {self.GUESSTIME} seconds")
            return False
        if (self.hard_mode):
            if (not self.is_hard_mode_guess_valid(guess)):
                print("Hard mode is enabled! You must include letters marked as * and + in")
                return False
        return True

    def create_guess_feedback(self, guess: str, invalid_guess: bool = False) -> list[str]:
        """Returns a list of feedback for a given guess"""
        feedback = ['_'] * self.word_length
        if (invalid_guess == True):
            return feedback

        character_frequency_guess = self.get_character_frequency(guess)
        for i, character in enumerate(guess):
            if (character not in self.word):
                feedback[i] = '_'
                self.incorrect_letters.add(character)
            elif (guess[i] == self.word[i]):
                feedback[i] = '*'
                self.correctly_positioned_letters[i] = guess[i]
                self.character_frequency[character] -= 1
                self.correctly_guessed_letters.add(character)
            elif (feedback[i] != '*' and character in self.word and self.character_frequency[character] > 0):
                # TODO: i dont think i need character in word anymore now that i use continue
                # TODO: this should probably be an if elif else loop for readability
                feedback[i] = '+'
                self.character_frequency[character] -= 1
                self.correctly_guessed_letters.add(character)
            if (character in self.word):
                # c_g_l keeps a set of characters that have been correctly guessed
                self.correctly_guessed_letters.add(character)
        return feedback

    def process_guess(self, guess: str) -> int:
        """Processes a guess and returns the outcome of the guess.
        0- incorrect guess
        1- correct guess
        2- error: must guess a valid word"""
        self.previous_guesses.append(guess)
        if (guess not in self.word_list):
            print(f"Incorrect! Must guess a valid word!")
            feedback = self.create_guess_feedback(guess, invalid_guess = True)
            self.previous_clues.append(feedback)
            return 2

        feedback = self.create_guess_feedback(guess)
        self.previous_clues.append(feedback)

        if (guess == self.word):
            print(f"Correct! The word was {guess}!")
            return 1
        return 0

    @staticmethod
    def clue_to_string(clue: list[str]) -> str:
        """Returns a string representation of a clue"""
        string = ""
        for i, character in enumerate(clue):
            string += character
            if (i != len(clue) - 1):
                string += " "
        return string

    def print_previous_clues(self) -> None:
        """Prints all previous clues"""
        for i, guess in enumerate(self.previous_guesses):
            clue = self.previous_clues[i]
            clue_string = self.clue_to_string(clue)
            if (guess in self.word_list):
                print(f"Turn {i + 1}/{self.max_attempts}: {clue_string}   {guess}")
            elif (guess.split(" ")[0] == ">>>hint:"):
                print(f"Turn {i + 1}/{self.max_attempts}: Hint-  {guess.split(" ")[1]}")
            elif (guess.split(" ")[0] == ">>>invalidguess:"):
                if (self.hard_mode):
                    print(f"Turn {i + 1}/{self.max_attempts}: invalid guess: {guess.split(" ")[1]} - Hard mode is enabled! You must include letters marked as * and + in")
                else:
                    print(f"Turn {i + 1}/{self.max_attempts}: invalid guess: {guess.split(" ")[1]}")
            else:
                print(f"Turn {i + 1}/{self.max_attempts}: {clue_string}   invalid word: {guess}")
        return

    def create_round_display(self) -> None:
        """Creates a display of the current round"""
        print(f"Lives Left: {self.lives_left}")
        print(f"Incorrect letters: {self.incorrect_letters}")
        # print(f"word to guess: {self.word}") # for debugging use
        self.print_previous_clues()
        return
            
    def show_game_end_screen(self, game_won: bool, game_time: float = None) -> None:
        """Creates the end screen of the game"""
        if (game_won):
            print(f"Congratulations, you've guessed the correct answer - {self.word} in {game_time:.2f} seconds!")
            if (len(self.previous_guesses) == 1):
                print(f"It took {self.max_attempts - self.lives_left + 1} turn!")
            else:
                print(f"It took {self.max_attempts - self.lives_left + 1} turns!")
        else:
            print(f"You've run out of lives! The word was {self.word}")
        self.print_previous_clues()
        return

    @staticmethod
    def read_winners_file() -> list[str]:
        """Returns a list of all winners from the winners.txt file"""
        with open("winners.txt", 'r') as file:
            winners_file = file.read()
            winners_list = winners_file.split("\n")
        return winners_list

    def update_winners_file(self, game_time: float) -> None:
        """Adds the current player to the winners.txt file"""
        with open("winners.txt", 'a') as file:
            file.write(f"{self.player_name} - {game_time:.2f}\n")
        return

    def exit_game(self) -> None:
        """Exits the game"""
        self.clear_console()
        print("Thanks for playing!")
        return exit()

    def play_game(self) -> None:
        """Main game loop"""
        self.clear_console()

        print("Welcome to Wordle!")
        name = input("What is your name? ")
        self.player_name = name
        show_past_winners = input("Would you like to see past winners? (y/n) ")
        if (show_past_winners.lower() == "y"):
            previous_winners = self.read_winners_file()
            for winner in previous_winners:
                print(winner)
        print("")

        # user must specify a word length
        word_length_selected = False
        while (not word_length_selected):
            word_length = input("Enter the word length you would like to play (4, 5, 6): ")
            if (word_length.isdigit() and int(word_length) in [4, 5, 6]):
                self.player_chose_word_length(int(word_length))
                word_length_selected = True
            else:
                print("Invalid word length. Please enter a valid word length.")

        # user must specify whether they wish to play hard mode
        hard_mode_input = input("Do you want to play hard mode? (y/n) ")
        if (hard_mode_input.isalpha() and hard_mode_input == "y"):
            print("Playing in hard mode")
            self.hard_mode = True
        else:
            print("Playing in easy mode")
        game_start_time = time.time()
        print("")

        # user gets WordleGame.lives_left amount of guesses
        while self.lives_left > 0:
            guess_start_time = time.time()
            if (len(self.valid_words) > 0):
                print(f"Valid words: {self.valid_words}")
            self.valid_words = []
            print("Input \"exit()\" to quit the game")
            print("Input \"vocab()\" to see a list of all valid words")
            if (not self.hint_used):
                print("Input \"hint()\" to reveal a letter. You can only use one hint and will lose a life.")
            guess = input(f"You have 30 seconds to guess a {len(self.word)} letter word: ").lower()
            guess_end_time = time.time()

            if guess.lower() == "exit()":
                self.exit_game()
            elif guess.lower() == "hint()":
                self.generate_hint()
                self.clear_console()
                self.create_round_display()
                continue
            elif guess.lower() == "vocab()":
                self.valid_words = self.get_valid_words()
                self.clear_console()
                continue

            if (not self.is_guess_valid(guess, guess_start_time, guess_end_time)):
                # User has made an invalid guess
                self.lives_left = self.lives_left - 1
                self.clear_console()
                self.create_round_display()
                self.previous_guesses.append(f">>>invalidguess: {guess}")
                self.previous_clues.append([])
                self.clear_console()
                self.show_game_end_screen(game_won=False)
                continue

            outcome = self.process_guess(guess)
            if (outcome == 1):
                # Player has guessed the correct answer
                self.clear_console()
                game_end_time = time.time()
                game_time = (game_end_time - game_start_time)
                self.show_game_end_screen(game_won=True, game_time=game_time)
                self.update_winners_file(game_time)
                return
            elif (outcome == 0):
                # Player has made an incorrect guess
                self.lives_left = self.lives_left - 1
            elif (outcome == 2):
                # Must guess a valid word
                self.lives_left = self.lives_left - 1
            self.clear_console()
            self.create_round_display()

        # Out of lives

        self.clear_console()
        self.show_game_end_screen(game_won=False)
        return


def main():
    WordleGame()
    return

main()