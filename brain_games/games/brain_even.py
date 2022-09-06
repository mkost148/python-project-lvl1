import random


def is_even(num):  # returns True if 'num' is even, otherwise False
    if (num % 2) == 0:
        return True
    else:
        return False


def even(difficulty):
    ''''Even game. Generate random number.
        Return 'yes' if number is even'''

    rule_string = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = random.randint(0, difficulty)
    question_string = str(num)
    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (rule_string, question_string, correct_answer)
