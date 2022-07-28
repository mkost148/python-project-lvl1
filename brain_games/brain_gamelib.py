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


def launch_game(game_type, attempts=NUM_OF_ATTEMPTS):
    if game_type == 'C':  # Calculator
        difficulty = prompt.integer('Please enter maximum number: ')
        return calc(attempts, difficulty)

    elif game_type == 'E':  # odd or Even
        difficulty = prompt.integer('Please enter maximum number: ')
        return even(attempts, difficulty)

    elif game_type == 'D':  # Greatest common divisor
        difficulty = prompt.integer('Please enter maximum number: ')
        return gcd(attempts, difficulty)

    elif game_type == 'P':  # Progression
        max_initial_num = prompt.integer(
            'Please enter maximum initial number: ')
        return progss(attempts,
                      max_initial_num,
                      MAXIMUM_STEP_OF_PROGRESSION,
                      MIN_LEN_OF_PROGRESSION,
                      REC_LEN_OF_PROGRESSION)

    elif game_type == 'I':  # Prime or not
        difficulty = prompt.integer('Please enter maximum number: ')
        return prime(attempts, difficulty)


def main():
    return


if __name__ == '__main__':
    main()
