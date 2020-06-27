import string
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/Angelica/Documents/Coding/ComputerScience/MIT_600/wk_3/mitx600_problem_set_3/scripts/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


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


def welcomeMsg(secretWord):
    return ('Welcome to the game, Hangman!\nI am thinking of a word that is ' +
            str(len(secretWord)) + ' letters long\n-------------')


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


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    for i in lettersGuessed:
        if i in alphabet_list:
            alphabet_list.remove(i)
    separator = ''
    return separator.join(alphabet_list)


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
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    print(welcomeMsg(secretWord))
    attemptsLeft = 8
    while attemptsLeft > 0:
        print('you have ' + str(attemptsLeft) +
              ' guesses left\nAvailable letters: ' + getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        letterLowerCase = letter.lower()
        if letterLowerCase in lettersGuessed:
            lettersGuessed.append(letterLowerCase)
            print('Oops! You\'ve already guessed that letter: ' +
                  getGuessedWord(secretWord, lettersGuessed))
        elif letterLowerCase in secretWord:
            lettersGuessed.append(letterLowerCase)
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Good guess: ' + secretWord +
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

    if attemptsLeft == 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
