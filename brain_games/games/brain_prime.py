import random


MIN_NUMBER = 1  # minimum number to generate
RULE_STRING = 'Answer "yes" if given number is prime. '\
              'Otherwise answer "no".'


def is_prime(number):  # returns True if 'number' is prime, otherwise False
    if abs(number) == 1:  # '1' is not prime nor combined number
        return False
    i = 2
    max_i = number // 2  # num of iterations
    while i <= max_i:
        if number % i == 0:
            # uncomment the following for test
            # print('can be divided by ', str(i))
            return False
        i += 1
    return True


def question_and_answer(difficulty):
    '''Prime game'''

    number = random.randint(MIN_NUMBER, difficulty)  # generate random number
    question_string = str(number)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_string, correct_answer
