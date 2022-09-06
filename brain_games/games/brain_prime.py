import random


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


def prime(difficulty):
    '''Prime game. Returns 'yes' if number is prime'''

    rule_string = 'Answer "yes" if given number is prime. '\
                  'Otherwise answer "no".'
    number = random.randint(1, difficulty)  # generate random number
    question_string = str(number)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (rule_string, question_string, correct_answer)
