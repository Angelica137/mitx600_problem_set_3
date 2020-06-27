from getGuessedWord import getGuessedWord
from isWordGuessed import isWordGuessed


def gameRules(letterLowerCase, lettersGuessed, secretWord, attemptsLeft):
    if letterLowerCase in lettersGuessed:
        lettersGuessed.append(letterLowerCase)
        print('Oops! You\'ve already guessed that letter: ' +
              getGuessedWord(secretWord, lettersGuessed))
    elif letterLowerCase in secretWord:
        lettersGuessed.append(letterLowerCase)
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print(getGuessedWord(secretWord, lettersGuessed) + ' Good guess: ' + secretWord +
                  '\n------------\nCongratulations, you won!')
        # break
        else:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
    else:
        lettersGuessed.append(letterLowerCase)
        print('Oops! That letter is not in my word: ' +
              getGuessedWord(secretWord, lettersGuessed))
        attemptsLeft -= 1
    print('-------------')
