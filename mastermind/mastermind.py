from .game import generate_code, validate_guess, color_count, correct_pos_and_color, check_guess, check_win_or_lose, get_win_percentage, format_guess_stats

# These functions allow you to print a string s in the stated colors. Using them is NOT required
def print_red(s):
    return '\033[31m' + s + '\033[0m'

def print_yellow(s):
    return '\033[33m' + s + '\033[0m'

def print_green(s):
    return '\033[32m' + s + '\033[0m'

def print_blue(s):
    return '\033[36m' + s + '\033[0m'

def print_indigo(s):
    return '\033[34m' + s + '\033[0m'

def print_violet(s):
    return '\033[35m' + s + '\033[0m'

  
plays = 0
wins = 0
guess_stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
in_a_row = 0

def mastermind():
    global plays
    plays += 1
    global in_a_row
    in_a_row = 0
    game = True
    num_guesses = 0

  
    while game:
      #Beginng of game, first turn only
      if num_guesses == 0:
        print ("Welcome to Mastermind!")
        print ("Generating a new code...\n New code generated: ****\n Guess the code! \n Each character in the code is one of the following letters: \n R, Y, G, B, I, V")
        code = generate_code()
        user_input = input ("Guess the code:").upper()
        guess = list(user_input)

      while num_guesses < 8: #Not including 8, because num_guesses = 0 counted as turn 1
        
        #Invalid guess loop
        if not validate_guess(guess):
          print ("You guessed: " + str(user_input))
          user_input = input ("Guess invalid. Guess again.").upper()
          guess = list(user_input)
          
        #Valid guess loop  
        elif validate_guess(guess):
          num_guesses += 1 
          guess = list (user_input)
          global in_a_row

          #Check win/lose loop
          if check_win_or_lose(guess, code, num_guesses) == None: 
            print ("You guessed: " + str(user_input))
            print (check_guess(guess, code))
            print ("You have guessed " + str(num_guesses) + " time(s). Number of tries remaining: " + str(8 - num_guesses))
            user_input = input ("Try again (R, Y, G, B, I, V):").upper()
            guess = list (user_input)
            
          #Do stuff if win  
          elif check_win_or_lose(guess, code, num_guesses) == True:
            global wins
            wins += 1
            in_a_row += 1
            global guess_stats
            guess_stats[num_guesses] += 1 #Add num_guesses (value) to dictionary
            print ("Congratulations! You guessed the secret code!!")
            break #Break loop if win
            
          #Do stuff if lose
          elif check_win_or_lose(guess, code, num_guesses) == False:
            in_a_row = 0
            print ("You lost. Better luck next time!")

      #Get stats      
      print ("You have played " + str(plays) + " game(s) and won " + str(get_win_percentage(wins, plays)) + "%. Here are your guess stats: " + str(format_guess_stats(guess_stats)))

      #Play again prompt loop
      end_game = True
      while end_game:
        game = False
        play_again = input ("End game. Play again? Enter Y to replay, any other character to exit: ").upper()
        if play_again == "Y":
          print ("Okay, let's play again!")
          mastermind()
        else:
          print ("Thanks for playing!")
          end_game = False

      break
        
