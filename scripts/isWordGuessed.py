# def joinLettersGuessed(lettersGuessed):


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    separator = ','
    joinLettersGuessed = separator.join(lettersGuessed)
    return joinLettersGuessed is secretWord