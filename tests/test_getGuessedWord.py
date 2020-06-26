from scripts.getGuessedWord import getGuessedWord


def test_get_letters_guessed_correctly_so_far():
    secretWord = 'durian'
    lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm']
    assert getGuessedWord(secretWord, lettersGuessed) == 'd _ _ i a _'
