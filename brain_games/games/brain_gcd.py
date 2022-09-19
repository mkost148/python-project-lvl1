import random


MIN_NUMBER = 0  # minimum number to generate


def get_gcd(num1, num2):  # returns greatest common divisor of 'num1', 'num2'
    if (num1 * num2 == 0):  # check if one of them is zero
        return num1 + num2  # non-zero element
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (num1 + num2)  # GCD + zero == GCD


def gcd(difficulty):
    '''Greatest common divisor game.\
        Return 'rule_string', 'question_string' and 'correct_answer' '''
    rule_string = 'Find the greatest common divisor of given numbers.'

    num1 = random.randint(MIN_NUMBER, difficulty)
    num2 = random.randint(MIN_NUMBER, difficulty)
    question_string = str(num1) + ' ' + str(num2)
    return (rule_string, question_string, str(get_gcd(num1, num2)))
