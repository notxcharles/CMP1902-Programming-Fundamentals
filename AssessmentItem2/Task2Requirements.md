~~The script will randomly select one 5 letter word from the dictionary~~

~~during each turn the user provides a word as a guess~~

guess must be a real word. if not, the user gets a warning and skips a turn  TODO: get a warning

~~* correct letter, correct position~~
~~+ correct letter,~~
~~_ nothing correct~~

the above symbols must be seperated by a space TODO: this

Multiple  instances  of  the  same  letter  in  a  guess,  such  as  the "o"s in "robot", will be assigned a * or + only if the letter also appears multiple times in the answer TODO: check this

player should have the option to give up at any time TODO: this

if the player fails to find the answer within six turns or gives up, they lose. if the answer is found they win. an appropiate message should be printed TODO: check six turns

MUST HAVES:

code should ask the user for a name at the start and measure the time in seconds that they needed to solve the puzzle TODO: this
this should be stored in a winners.txt file which is updated only after a win. TODO: this
user should have the option to see past winners and their time before beginning a puzzle TODO: this

~~after each guess, the program should provide the clue and a list of all letters the the user has used but are not part of the right answer~~

the player is given 30 seconds to make a guess. if they provide a word after 30 seconds, the turn is lost TODO: lose a turn (add to previous guesses)

~~any erroneous input should be handled and there should be no crashing~~

ADVANCED FEATURES:

the player can select to play with four, five or six letter word
player has the option of hard mode. the hard mode required players to include letters marked as * and + in subsequent guesses TODO: all of this

the player has the option to use a hint once. this hint will provide a letter that is part of the answer but will not provide its location. the player loses one turn when using the hint TODO: all of this

the player can ask for help with the vocabulary. this will provide all the words in the dictionary that satisfy the clues TODO: all of this
