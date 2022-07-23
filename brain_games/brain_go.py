import random
import prompt
from brain_games.games.brain_even import even
from brain_games.games.brain_calc import calc
from brain_games.games.brain_gcd import gcd
from brain_games.games.brain_progression import progss


num_of_attempts = 3  # right answers to win a game
maximum_step_of_progression = 20  # maximum step of progression
min_len_of_progression = 5  # minimum numbers of progreeion to generate
rec_len_of_progression = 10  # maximum numbers of progreeion to generate


def hello():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def main():
    user_name = hello()
    while True:
        game_type = prompt.character('Plase select a game:\n    - <C>alculator\n    - odd or <E>ven\n\
    - greatest common <D>ivisor\n    - <P>rogression\nor <any other key> to quit: ')
        game_type = game_type.upper()

        if game_type == 'C':
            difficulty = prompt.integer('Please choose difficulty (maximum number to operate with): ')
            calc(user_name, num_of_attempts, difficulty)
        elif game_type == 'E':
            difficulty = prompt.integer('Please choose difficulty (maximum number to operate with): ')
            even(user_name, num_of_attempts, difficulty)
        elif game_type == 'D':
            difficulty = prompt.integer('Please choose difficulty (maximum number to operate with): ')
            gcd(user_name, num_of_attempts, difficulty)
        elif game_type == 'P':
            len_of_progression = random.randrange(min_len_of_progression, rec_len_of_progression)
            difficulty = prompt.integer('Please enter maximum initial number of progression: ')
            progss(user_name, num_of_attempts, difficulty, maximum_step_of_progression, len_of_progression)
        else:
            print(f'Thanks for playing, {user_name}! Bye!')
            return


if __name__ == '__main__':
    main()
