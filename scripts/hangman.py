import string
from getAvailableLetters import getAvailableLetters
from getGuessedWord import getGuessedWord
from welcomeMsg import welcomeMsg
from gameRules import gameRules


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
    print(welcomeMsg(secretWord))
    attemptsLeft = 8
    while attemptsLeft > 0:
        print('you have ' + str(attemptsLeft) +
              ' gesses left\nAvailable letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letterLowerCase = letter.lower()
        getGuessedWord(secretWord, lettersGuessed)
        gameRules(letterLowerCase, lettersGuessed, secretWord, attemptsLeft)
        attemptsLeft -= 1
# print(getGuessedWord(secretWord, lettersGuessed))
# is letterLowerCase in secret word
# congrats message leave counter unchanged
# if letter is not in secret word
# sad message
# change counter
# if letter had already been changed
# sad message


# count no of attempts
# return available letters - get avail letters
# ask them to guess a letter
# reply


secretWord = 'apple'
lettersGuessed = []
hangman(secretWord)
