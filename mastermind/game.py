import random
from collections import Counter

colors = ["R", "Y", "G", "B", "I", "V"]

def generate_code():
    code = random.choices(colors, k=4)
    return code

def validate_guess(guess):
  if len(guess) != 4:
    return False
  for guess_letters in guess:
    if(guess_letters.upper() not in colors):
      return False 
  return True 

def color_count(guess, code):
  overlap = list((Counter(code) & Counter(guess)).elements())
  return len(overlap)

def correct_pos_and_color(guess, code):
    correct_count = 0
    for i in range(len(guess)):
      if guess[i] == code[i]:
        correct_count += 1
    return int(correct_count)

def check_guess(guess, code):
    first_num = correct_pos_and_color(guess, code)
    second_num = color_count(guess, code) - correct_pos_and_color(guess, code)
    check = (first_num, second_num)
    return check

def check_win_or_lose(guess, code, num_guesses):
    if guess == code and num_guesses <= 8:
      return True
    elif ((guess != code and num_guesses > 7) or num_guesses > 7): #num_guesses > 7 because at first try, num_guesses = 0
      return False
    else:
      return None

def get_win_percentage(wins, plays):
    if plays == 0: #to avoid error when division by 0
      return 0
    else:
      percent = int(wins / plays * 100)
      return percent

def format_guess_stats(guess_stats):
    new_guess_stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    new_guess_stats.update(guess_stats)
    new_guess_stats_values = list(new_guess_stats.values())
    Xs = []
    for values in new_guess_stats_values:
      Xs.append(values * "X")
    return Xs