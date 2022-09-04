import random


def prime(difficulty):
    '''Prime game. Generate random number, Return 'rule_string',
        'question_string'
        and 'yes' or 'no' depends upon number is prime or not'''

    rule_string = 'Answer "yes" if given number is prime. '\
        'Otherwise answer "no".'
    number = random.randint(1, difficulty)
    question_string = 'Question: ' + str(number)
    if abs(number) == 1:  # '1' is not prime nor combined number
        return (rule_string, question_string, 'no')
    i = 2
    max_i = number // 2
    correct_answer = 'yes'
    while i <= max_i:
        if number % i == 0:
            # uncomment the following for test
            # print('can be divided by ', str(i))
            return (rule_string, question_string, 'no')
        i += 1
    return (rule_string, question_string, correct_answer)
