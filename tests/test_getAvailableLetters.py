from scripts.getAvailableLetters import getAvailableLetters


def test_returns_alphabet_letters_remaining_after_guess():
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    assert getAvailableLetters(lettersGuessed) == 'abcdfghjlmnoqtuvwxyz'
