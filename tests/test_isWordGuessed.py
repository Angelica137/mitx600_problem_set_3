from scripts.isWordGuessed import isWordGuessed


def test_word_is_guessed_False():
    secretWord = 'apple'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == False


def test_word_is_guessed_True():
    secretWord = 'eikprs'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == True
