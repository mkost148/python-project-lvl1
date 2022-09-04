import random


def even(difficulty):
    ''''Even game. Generate random number.
        Return 'rule_string', 'question_string'
        and 'yes' or 'no' depends on is generated number enev or not'''

    rule_string = 'Answer "yes" if the number is even, otherwise answer "no".'
    num = random.randint(0, difficulty)
    question_string = 'Question: ' + str(num)
    if (num % 2) == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (rule_string, question_string, correct_answer)
