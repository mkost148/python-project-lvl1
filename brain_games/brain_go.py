#!/usr/bin/env python3


import prompt


ROUNDS_COUNT = 3  # correct answers to win a game
DEFAULT_DIFFICULTY = 20  # maximum number to operate with


def game(module_func=None):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    if module_func is None:
        return

    print(module_func.RULE_STRING)  # show the rules
    for _ in range(ROUNDS_COUNT):
        question_string, correct_answer =\
            module_func.question_and_answer(DEFAULT_DIFFICULTY)
        print('Question: ' + question_string)
        answer = prompt.string('Your answer: ')
        answer = answer.strip()
        answer = answer.lower()
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'", answer, "' is wrong answer ;(."
                  " Correct answer was '", correct_answer, "'."
                  )
            print(f"Let's try again, {user_name}!")
            return

    print('Congratulations, {}!'.format(user_name))
