#!/usr/bin/env python3


import prompt


ROUNDS_COUNT = 3  # correct answers to win a game
DEFAULT_DIFFICULTY = 20  # maximum number to operate with


# ------------------------------------------------
def do_func(module_func=None):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    if module_func is None:
        return
    (question_string, correct_answer) =\
        module_func.main(DEFAULT_DIFFICULTY)  # first tour of game
    print(module_func.RULE_STRING)  # show the rules

    for _ in range(ROUNDS_COUNT):
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

        # generate next question & answer
        (question_string, correct_answer) =\
            module_func.main(DEFAULT_DIFFICULTY)

    print('Congratulations, {}!'.format(user_name))
# ------------------------------------------------


if __name__ == '__main__':
    do_func()
