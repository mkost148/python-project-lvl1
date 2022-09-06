import random


def get_gcd(num1, num2):  # returns greatest common divisor of 'num1', 'num2'
    bigger_num = max(abs(num1), abs(num2))
    if (num1 * num2 == 0):  # check if one of them is zero
        return bigger_num
    gcd_max = min(abs(num1), abs(num2))  # num of attempts. Might be optimized?!
    result = 1
    i = 2
    while i <= gcd_max:
        if (num1 % i == 0) and (num2 % i == 0):
            result = i
        i += 1
    return result


def gcd(difficulty):
    '''Greatest common divisor game.\
        Return 'rule_string', 'question_string' and 'correct_answer' '''
    rule_string = 'Find the greatest common divisor of given numbers.'

    num1 = random.randint(0, difficulty)
    num2 = random.randint(0, difficulty)
    question_string = str(num1) + ' ' + str(num2)
    return (rule_string, question_string, str(get_gcd(num1, num2)))
