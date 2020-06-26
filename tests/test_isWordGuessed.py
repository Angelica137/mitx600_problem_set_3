from scripts.isWordGuessed import isWordGuessed


def test_word_is_guessed():
    secretWord = 'apple'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == False

    secretWord = 'prseik'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == True
