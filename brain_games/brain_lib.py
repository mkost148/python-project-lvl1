import prompt
from brain_games.games.brain_even import even
from brain_games.games.brain_calc import calc
from brain_games.games.brain_gcd import gcd
from brain_games.games.brain_progression import progss
from brain_games.games.brain_prime import prime


# constants
NUM_OF_ATTEMPTS = 3  # right answers to win a game
MAXIMUM_STEP_OF_PROGRESSION = 10  # maximum step of arifmetical progression
MIN_LEN_OF_PROGRESSION = 5  # minimum quantity of numbers of progression
REC_LEN_OF_PROGRESSION = 10  # recommended numbers of progression to generate


def hello():
    """Ask for user name"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def print_answer(correct_answer, answer):
    print("'", answer, "' is wrong answer ;(."
          " Correct answer was '", correct_answer, "'."
          )


def launch_game(game_type):
    if game_type == 'C':  # Calculator
        difficulty = prompt.integer('Please enter maximum number: ')
        return calc(NUM_OF_ATTEMPTS, difficulty)

    elif game_type == 'E':  # odd or Even
        difficulty = prompt.integer('Please enter maximum number: ')
        return even(NUM_OF_ATTEMPTS, difficulty)

    elif game_type == 'D':  # Greatest common divisor
        difficulty = prompt.integer('Please enter maximum number: ')
        return gcd(NUM_OF_ATTEMPTS, difficulty)

    elif game_type == 'P':  # Progression
        max_initial_num = prompt.integer(
            'Please enter maximum initial number: ')
        return progss(NUM_OF_ATTEMPTS,
                      max_initial_num,
                      MAXIMUM_STEP_OF_PROGRESSION,
                      MIN_LEN_OF_PROGRESSION,
                      REC_LEN_OF_PROGRESSION)

    elif game_type == 'I':  # Prime or not
        difficulty = prompt.integer('Please enter maximum number: ')
        return prime(NUM_OF_ATTEMPTS, difficulty)


def main():
    return


if __name__ == '__main__':
    main()
