import string
from getAvailableLetters import getAvailableLetters
from getGuessedWord import getGuessedWord
from welcomeMsg import welcomeMsg
from isWordGuessed import isWordGuessed


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
    guess = getGuessedWord(secretWord, lettersGuessed)
    attemptsLeft = 8
    while attemptsLeft > 0:
        print('you have ' + str(attemptsLeft) +
              ' guesses left\nAvailable letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letterLowerCase = letter.lower()
        if letterLowerCase in lettersGuessed:
            lettersGuessed.append(letterLowerCase)
            print('Oops! You\'ve already guessed that letter: ' + guess)
        elif letterLowerCase in secretWord:
            lettersGuessed.append(letterLowerCase)
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print(getGuessedWord(secretWord, lettersGuessed) + ' Good guess: ' + secretWord +
                      '\n------------\nCongratulations, you won!')
                break
            else:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letterLowerCase)
            print('Oops! That letter is not in my word: ' +
                  getGuessedWord(secretWord, lettersGuessed))
            attemptsLeft -= 1
        print('-------------')


# count no of attempts
# return available letters - get avail letters
# ask them to guess a letter
# reply
secretWord = 'apple'
lettersGuessed = []
hangman(secretWord)
