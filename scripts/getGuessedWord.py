def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedSoFar = []
    for i in secretWord:
        if i in lettersGuessed:
            guessedSoFar.append(i)
        else:
            guessedSoFar.append('_')
    separator = ' '
    return separator.join(guessedSoFar)


secretWord = 'durian'
lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm']
print(getGuessedWord(secretWord, lettersGuessed))
