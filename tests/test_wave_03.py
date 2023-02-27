import pytest

from mastermind.game import color_count, correct_pos_and_color, check_guess

# --------------------------test color_count------------------------------------

def test_returns_int():
    #Arrange
    guess = ['R','R','G','B']
    code = ['R','G','B','V']

    #Act
    result = color_count(guess, code)

    #Assert
    assert type(result) == int

def test_two_matching():
    #Arrange
    guess = ['R','I','G','B']
    code = ['R','I','V','V']

    #Act
    result = color_count(guess, code)

    #Assert
    assert result == 2

def test_order_does_not_matter():
    #Arrange
    guess = ['R','I','G','B']
    code = ['V','V','R','I']

    #Act
    result = color_count(guess, code)

    #Assert
    assert result == 2

def test_letter_not_double_counted():
    #Arrange
    guess = ['R','R','G','B']
    code = ['R','V','V','V']

    #Act
    result = color_count(guess, code)

    assert result == 1

def test_duplicates_counted_if_echoed():
    #Arrange
    guess = ['R','R','G','V']
    code = ['R','R','I','B']

    #Act
    result = color_count(guess, code)

    assert result == 2


def test_no_match_returns_zero():
    #Arrange
    guess = ['R','B','V','V']
    code = ['I','I','I','I']

    #Act
    result = color_count(guess, code)

    #Assert
    assert result == 0

#--------------------------test correct_pos_and_color------------------------------------

def test_correct_pos_and_color_returns_int():
    #Arrange
    guess = ['R','B','B','B']
    code = ['I','I','I','I']

    #Act
    result = correct_pos_and_color(guess, code)

    #Assert
    assert type(result) == int

def test_correct_pos_and_color_two_match():
    #Arrange
    guess = ['R','B','I','V']
    code = ['R','B','G','G']

    #Act
    result = correct_pos_and_color(guess, code)

    #Assert
    assert result == 2

def test_correct_color_but_not_pos_returns_zero():
    #Arrange
    guess = ['R','B','I','V']
    code = ['I','V','R','B']

    #Act
    result = correct_pos_and_color(guess, code)

    #Assert
    assert result == 0

def test_correct_color_and_pos_dups_not_double_counted():
    #Arrange
    guess = ['R','B','I','R']
    code = ['R','V','V','V']

    #Act
    result = correct_pos_and_color(guess, code)
    
    #Assert
    assert result == 1


def test_correct_pos_and_color_no_match_returns_zero():
    #Arrange
    guess = ['R','B','V','V']
    code = ['I','I','I','I']

    #Act
    result = correct_pos_and_color(guess, code)

    #Assert
    assert result == 0

#--------------------test check_guess()-------------------------------------
def test_correct_guess():
    #Arrange
    guess = ['R','B','V','V']
    code = ['R','B','V','V']
    #Act
    result = check_guess(guess, code)

    #Assert
    assert result == (4, 0)


def test_mixed_guess():
    #Arrange
    guess = ['R','B','I','V']
    code = ['R','Y','B','V']

    #Act
    result = check_guess(guess, code)

    #Assert
    assert result == (2, 1)

def test_completely_incorrect():
    #Arrange
    guess = ['V','V','V','V']
    code = ['R','R','R','R']

    #Act
    result = check_guess(guess, code)

    #Assert
    assert result == (0, 0)