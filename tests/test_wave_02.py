import pytest

from mastermind.game import validate_guess, check_win_or_lose

# --------------------------test validate_guess------------------------------------

def test_guess_false_length_greater_than_four():
    #Arrange
    guess = ['R','R','R','R','R']

    #Act
    result = validate_guess(guess)

    #Assert
    assert result is False


def test_guess_true_valid_letters_rygi():
    #Arrange
    guess = ['R','Y','G','I']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_guess_true_valid_letters_bv():
    #Arrange
    guess = ['B','B','V','V']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True


def test_guess_false_invalid_letters():
    #Arrange
    guess = ['R','O','Y','I']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is False

def test_guess_true_lowercase_letters():
        #Arrange
    guess = ['B','b','v','V']

    #Act
    result = validate_guess(guess)

    #assert
    assert result is True

# --------------------------test check_win_or_lose------------------------------------

    
def test_check_win_both_conditions_true():
    #Arrange
    guess = ['R','B','B','V']
    code = ['R','B','B','V']
    num_guesses = 3

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is True

def test_check_win_exceeds_max_guesses():
    #Arrange
    guess = ['R','B','B','V']
    code = ['R','B','B','V']
    num_guesses = 9

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is False

def test_check_win_game_ongoing():
        #Arrange
    guess = ['R','B','B','V']
    code = ['R','B','B','I']
    num_guesses = 2

    #Act
    result = check_win_or_lose(guess, code, num_guesses)

    #Assert
    assert result is None
