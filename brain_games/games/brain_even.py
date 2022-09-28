import random


MIN_NUMBER = 0  # minimum number to generate
RULE_STRING = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):  # returns True if 'num' is even, otherwise False
    return num % 2 == 0


def question_and_answer(difficulty):
    ''''Even game'''

    num = random.randint(MIN_NUMBER, difficulty)  # generate random number
    question_string = str(num)
    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_string, correct_answer
