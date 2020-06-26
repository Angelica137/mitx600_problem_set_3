import string


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
