def welcomeMsg(secretWord):
    return ('Welcome to the game, Hangman!\nI am thinking of a word that is ' +
            str(len(secretWord)) + ' letters long.')


secretWord = 'apple'
lettersGuessed = []
welcomeMsg(secretWord)
print('Welcome to the game, Hangman!')
print('I am thinking of a word that is ' +
      str(len(secretWord)) + ' letters long.')
