import pytest

from mastermind.game import get_win_percentage, format_guess_stats

# --------------------------test get_win_percentage------------------------------------

def test_win_percentage_returns_int():
    #Arrange
    wins = 1
    plays = 15
    
    #Act
    result = get_win_percentage(wins, plays)
    
    #Assert 
    assert type(result) == int

def test_win_percentage_zero_games():
    #Arrange
    wins = 0
    plays = 0
    
    #Act
    result = get_win_percentage(wins, plays)
    
    #Assert 
    assert result == 0

def test_win_stats_no_wins():
    #Arrange
    wins = 4
    plays = 0
    
    #Act
    result = get_win_percentage(wins, plays)
    
    #Assert 
    assert result == 0

def test_win_stats_even_percentage():
    #Arrange
    wins = 3
    plays = 4
    
    #Act
    result = get_win_percentage(wins, plays)
    
    #Assert 
    assert result == 75

def test_win_stats_round_down():
    #Arrange
    wins = 1
    plays = 15
    
    #Act
    result = get_win_percentage(wins, plays)
    
    #Assert 
    assert result == 6

# --------------------------test format_guess_stats------------------------------------

def test_format_guess_stats_no_games():
    #Arrange
    guess_stats = {}
    
    #Act
    result = format_guess_stats(guess_stats)
    
    #Assert
    assert len(result) == 8
    for s in result:
        assert s == ''

def test_format_guess_stats_one_pair():
    #Arrange
    guess_stats = {1: 4}
    
    #Act
    result = format_guess_stats(guess_stats)
    
    #Assert
    assert len(result) == 8
    assert len(result[0]) == 4
    for s in result:
        assert type(s) == str
        if s:
            for char in s:
                assert char == 'X'
        else:
            assert s == ''

def test_format_guess_stats_all_pairs():
    #Arrange
    guess_stats = {
        1: 4,
        2: 3,
        3: 4,
        4: 2,
        5: 6,
        6: 1,
        7: 1,
        8: 3
    }
    
    #Act
    result = format_guess_stats(guess_stats)
    
    #Assert
    assert len(result) == 8
    assert len(result[0]) == 4
    assert len(result[1]) == 3
    assert len(result[2]) == 4
    assert len(result[3]) == 2
    assert len(result[4]) == 6
    assert len(result[5]) == 1
    assert len(result[6]) == 1
    assert len(result[7]) == 3
    for s in result:
        assert type(s) == str
        if s:
            for char in s:
                assert char == 'X'
        else:
            assert s == ''
