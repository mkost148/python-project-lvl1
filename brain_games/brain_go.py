import random
import prompt
from brain_games.games.brain_even import even
from brain_games.games.brain_calc import calc
from brain_games.games.brain_gcd import gcd
from brain_games.games.brain_progression import progss
from brain_games.games.brain_prime import prime


# constants
num_of_attempts = 3  # right answers to win a game
maximum_step_of_progression = 20  # maximum step of arifmetical progression
min_len_of_progression = 5  # minimum numbers of progression to generate
rec_len_of_progression = 10  # maximum numbers of progression to generate


def hello():
    """Ask for user name"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def main():
    user_name = hello()
    while True:
        game_type = prompt.character('Plase select a game:\n    - <C>alculator\n    - odd or <E>ven\n\
    - greatest common <D>ivisor\n    - <P>rogression\n    - is pr<I>me\nor <any other key> to quit: ')
        game_type = game_type.upper()

        if game_type == 'C':
            difficulty = prompt.integer('Please enter maximum number to operate with: ')
            calc(user_name, num_of_attempts, difficulty)
        elif game_type == 'E':
            difficulty = prompt.integer('Please enter maximum number to operate with: ')
            even(user_name, num_of_attempts, difficulty)
        elif game_type == 'D':
            difficulty = prompt.integer('Please enter maximum number to operate with: ')
            gcd(user_name, num_of_attempts, difficulty)
        elif game_type == 'P':
            len_of_progression = random.randrange(min_len_of_progression, rec_len_of_progression)
            difficulty = prompt.integer('Please enter maximum initial number of progression: ')
            progss(user_name, num_of_attempts, difficulty, maximum_step_of_progression, len_of_progression)
        elif game_type == 'I':
            difficulty = prompt.integer('Please enter maximum number to operate with: ')
            prime(user_name, num_of_attempts, difficulty)
        else:
            print(f'Thanks for playing, {user_name}! Bye!')
            return


if __name__ == '__main__':
    main()
