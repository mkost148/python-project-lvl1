import random


MIN_NUMBER = 0  # minimum number to generate


def calc(difficulty):
    '''Calculator. Returns 'rule_string', 'question_string' and
        'correct_answer' (string)'''

    rule_string = 'What is the result of the expression?'
    operators = ("+", "-", "*")  # three operators are available
    num1 = random.randint(MIN_NUMBER, difficulty)
    num2 = random.randint(MIN_NUMBER, difficulty)
    oper_sym = random.choice(operators)
    if oper_sym == "+":  # 'plus'
        correct_answer = num1 + num2
    elif oper_sym == "-":  # 'minus'
        correct_answer = num1 - num2
    else:  # 'multiply'
        correct_answer = num1 * num2
    question_string = str(num1) + ' ' + oper_sym + ' ' + str(num2)
    return (rule_string, question_string, str(correct_answer))
