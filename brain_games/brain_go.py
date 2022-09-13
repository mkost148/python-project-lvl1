#!/usr/bin/env python3


import prompt


NUM_OF_ATTEMPTS = 3  # correct answers to win a game
DEFAULT_DIFFICULTY = 20  # maximum number to operate with


def do_func(game_func=''):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    if game_func == '':
        return
    (rule_string, question_string, correct_answer) =\
        game_func(DEFAULT_DIFFICULTY)  # first tour of game
    print(rule_string)  # show the rules
    scores = 0
    while scores < NUM_OF_ATTEMPTS:
        print('Question: ' + question_string)
        answer = prompt.string('Your answer: ')
        answer = answer.strip()
        answer = answer.lower()
        if answer == correct_answer:
            print('Correct!')
            scores += 1
        else:
            print("'", answer, "' is wrong answer ;(."
                  " Correct answer was '", correct_answer, "'."
                  )
            scores = NUM_OF_ATTEMPTS + 1  # stop the game
        (rule_string, question_string, correct_answer) =\
            game_func(DEFAULT_DIFFICULTY)  # generate next question & answer

    if (scores == NUM_OF_ATTEMPTS):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    do_func()
