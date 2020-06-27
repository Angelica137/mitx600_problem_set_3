from getGuessedWord import getGuessedWord


def gameRules(letterLowerCase, lettersGuessed, secretWord, attemptsLeft):
    if letterLowerCase in lettersGuessed:
        lettersGuessed.append(letterLowerCase)
        print('Oops! You\'ve already guessed that letter: ' +
              getGuessedWord(secretWord, lettersGuessed))
    elif letterLowerCase in secretWord:
        lettersGuessed.append(letterLowerCase)
        print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
    else:
        lettersGuessed.append(letterLowerCase)
        print('Oops! That letter is not in my word: ' +
              getGuessedWord(secretWord, lettersGuessed))

    print('-------------')
