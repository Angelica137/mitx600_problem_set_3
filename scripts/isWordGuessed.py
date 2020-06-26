# def joinLettersGuessed(lettersGuessed):


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    correct = 0
    for i in secretWord:
        if i in lettersGuessed:
            correct = 0
        else:
            correct = 1
            break
    if correct == 0:
        return True
    else:
        return False
