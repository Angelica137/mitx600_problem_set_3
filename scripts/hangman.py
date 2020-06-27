import string
from getAvailableLetters import getAvailableLetters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +
          str(len(secretWord)) + 'letters long.')
    counter = 0
    while counter < 8:
        print('_ _ _ _ _ _ _ _')
        counter += 1
        print('Available letters:' + getAvailableLetters(lettersGuessed))
    print(counter)
# count no of attempts
# return available letters - get avail letters
# ask them to guess a letter
# reply


secretWord = 'apple'
lettersGuessed = []
hangman(secretWord)
