from scripts.welcomemsg import welcomeMsg


def test_prints_welcome_message():
    secretWord = 'apple'
    assert welcomeMsg(
        secretWord) == 'Welcome to the game, Hangman!\nI am thinking of a word that is 5 letters long.'
