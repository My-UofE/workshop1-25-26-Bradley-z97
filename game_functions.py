import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val: int, next_val: int, user_input: str) -> bool:
    '''
    Docstring for check_higher_lower
    
    Logic for checking if the user's guess, 'h' or 'l',
    is correct or not.

    :param current_val: Current value in play
    :param next_val: Next value to be played
    :param user_input: The user's guess (either 'h' or 'l')
    '''
    return True if user_input == 'h' and current_val < next_val or user_input == 'l' and next_val < current_val else False


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    pass
