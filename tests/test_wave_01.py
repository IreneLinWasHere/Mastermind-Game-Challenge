import pytest

from mastermind.game import generate_code

# --------------------------test generate_code------------------------------------

def test_generate_code_length_four():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert len(result) == 4

def test_generate_code_is_list():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert type(result) == list

def test_generate_code_uses_valid_letters():
    #Arrange
    valid_letters = ['R', 'Y', 'G', 'B', 'I', 'V']

    #Act
    result = generate_code()

    #Assert
    for letter in result:
        assert letter in valid_letters
    
