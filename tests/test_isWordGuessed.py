from scripts.isWordGuessed import isWordGuessed


def test_word_is_guessed_correctly():
    secretWord = 'apple'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == False

    secretWord = 'prseik'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert isWordGuessed(secretWord, lettersGuessed) == True

    secretWord = 'durian'
    lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']
    assert isWordGuessed(
        'durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) == True
