#!/usr/bin/env python3

import prompt

from brain_games.brain_global import (
    hello,
    launch_game,
)


def main():
    user_name = hello()

    while True:
        result = False
        game_type = prompt.character('Plase select a game:\n'
                                     '    - <C>alculator\n'
                                     '    - odd or <E>ven\n'
                                     '    - greatest common <D>ivisor\n'
                                     '    - <P>rogression\n'
                                     '    - pr<I>me\n'
                                     'or <Q> to quit: ')
        game_type = game_type.upper()
        if game_type == 'Q':
            print("Thanks for playing, ", str.strip(user_name), "! Bye!")
            return
        elif game_type in 'CEDPI':
            result = launch_game(game_type)
            if result is True:
                print(f'Congratulations, {user_name}!')
            else:
                print(f"Let's try again, {user_name}!")
        else:
            pass


if __name__ == '__main__':
    main()
