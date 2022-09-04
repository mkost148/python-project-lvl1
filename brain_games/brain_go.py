#!/usr/bin/env python3


# common import
from brain_games.games.brain_calc import calc
from brain_games.games.brain_progression import progss
from brain_games.games.brain_even import even
from brain_games.games.brain_gcd import gcd
from brain_games.games.brain_prime import prime
import prompt


NUM_OF_ATTEMPTS = 3  # correct answers to win a game
DEFAULT_DIFFICULTY = 20  # maximum number to operate with


def hello():
    """Ask for user name"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def check_and_print_answer(answer, correct_answer):
    """Return (answer == correct answer) and print corresponding message"""
    if answer == correct_answer:
        print('Correct!')
    else:
        print("'", answer, "' is wrong answer ;(."
              " Correct answer was '", correct_answer, "'."
              )
    return (answer == correct_answer)


def do_func(game_func):
    user_name = hello()
    (rule_string, question_string, correct_answer) =\
        game_func(DEFAULT_DIFFICULTY)  # 1st run
    print(rule_string)  # show the rules
    scores = 0
    while scores < NUM_OF_ATTEMPTS:
        print(question_string)
        answer = prompt.string('Your answer: ')
        answer = answer.strip()
        answer = answer.lower()
        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = NUM_OF_ATTEMPTS + 1  # stop the game
        (rule_string, question_string, correct_answer) =\
            game_func(DEFAULT_DIFFICULTY)  # generate next question & answer
    if (scores == NUM_OF_ATTEMPTS):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


def do_calc():
    do_func(calc)


def do_even():
    do_func(even)


def do_gcd():
    do_func(gcd)


def do_progss():
    do_func(progss)


def do_prime():
    do_func(prime)


def main():
    hello()


if __name__ == '__main__':
    main()
