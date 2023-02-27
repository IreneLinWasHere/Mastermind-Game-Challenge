import pytest

if __name__ == '__main__':
    user_input = ""
    while user_input != "p" and user_input != "t":
        user_input = input('Please enter p to play or t to test => ')
    
    if user_input == "p":    
        from mastermind.mastermind import mastermind
        mastermind()
    else: 
      pytest.main()
