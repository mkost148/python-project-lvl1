import prompt
from brain_games.games.brain_even import even
from brain_games.games.brain_calc import calc


num_of_attempts = 3


def hello():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def main():
    user_name = hello()
    while True:
        game_type = prompt.character('Plase select a game: <C>alculator, <E>ven, or <any other key> to quit: ')
        game_type = game_type.upper()
        if game_type == 'C':
            difficulty = prompt.integer('Please choose difficulty (maximum number to operate with): ')
            calc(user_name, num_of_attempts, difficulty)
        elif game_type == 'E':
            difficulty = prompt.integer('Please choose difficulty (maximum number to operate with): ')
            even(user_name, num_of_attempts, difficulty)
        else:
            print(f'Thanks for playing, {user_name}! Bye!')
            return


if __name__ == '__main__':
    main()
