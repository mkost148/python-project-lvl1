#!/usr/bin/env python3


# common import
import prompt
import random


# ---------------------------------------------
# service functions begin

NUM_OF_ATTEMPTS = 3  # right answers to win a game


def hello():
    """Ask for user name"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def check_and_print_answer(answer, correct_answer):
    """Return (answer == correct answer) and print corresponding message"""
    if answer == correct_answer:
        print('Correct!')
    else:
        print("'", answer, "' is wrong answer ;(."
              " Correct answer was '", correct_answer, "'."
              )
    return (answer == correct_answer)

# service functions end
# ---------------------------------------------


# ---------------------------------------------
# game functions begin

# constants
MAXIMUM_STEP_OF_PROGRESSION = 10  # maximum step of arifmetical progression
MIN_LEN_OF_PROGRESSION = 5  # minimum quantity of numbers of progression
REC_LEN_OF_PROGRESSION = 10  # recommended numbers of progression to generate
DEFAULT_DIFFICULTY = 20  # maximum number to operate with


def calc(difficulty=DEFAULT_DIFFICULTY):
    '''Calculator. Returns 'question_string' (string) and\
        'correct_answer' (integer)'''
    operators = ("+", "-", "*")  # three operators are available
    num1 = random.randint(0, difficulty)
    num2 = random.randint(0, difficulty)
    oper_sym = random.choice(operators)
    if oper_sym == "+":  # 'plus'
        correct_answer = num1 + num2
    elif oper_sym == "-":  # 'minus'
        correct_answer = num1 - num2
    else:  # 'multiply'
        correct_answer = num1 * num2
    question_string = 'Question: ' + str(num1) +\
                      ' ' + oper_sym + ' ' + str(num2)
    return(question_string, correct_answer)


def progss(max_init=DEFAULT_DIFFICULTY):
    '''Progression. Generate arifmetical progression.\
        Return 'question_string' (string)\
             and 'correct_answer' (missing element, integer)'''

    # generate progression
    init = random.randrange(0, max_init)
    step = random.randrange(1, MAXIMUM_STEP_OF_PROGRESSION)
    lenght = random.randrange(MIN_LEN_OF_PROGRESSION, REC_LEN_OF_PROGRESSION)
    progression = [init]
    i = 1
    while i < lenght:
        progression.append(init + step * i)
        i += 1

    # make one element missing
    missing_element_position = random.randint(0, len(progression) - 1)
    i = 0
    question_string = 'Question: '
    while i <= len(progression) - 1:
        if i == missing_element_position:
            question_string = question_string + '.. '
        else:
            question_string = question_string + str(progression[i]) + ' '
        i += 1

    return (question_string, progression[missing_element_position])


def prime(difficulty=DEFAULT_DIFFICULTY):
    '''Prime game. Generate random number, Return 'yes' or 'no',\
        depends upon number is prime or not'''
    number = random.randint(1, difficulty)
    question_string = 'Question: ' + str(number)
    if abs(number) == 1:  # '1' is not prime nor combined number
        return (question_string, 'no')
    i = 2
    max_i = number // 2
    correct_answer = 'yes'
    while i <= max_i:
        if number % i == 0:
            # uncomment the following for test
            # print('can be divided by ', str(i))
            return (question_string, 'no')
        i += 1
    return (question_string, correct_answer)


def gcd(difficulty=DEFAULT_DIFFICULTY):
    '''Greatest common divisor game.\
        Return 'question_string' and 'correct_answer' '''
    num1 = random.randint(0, difficulty)
    num2 = random.randint(0, difficulty)
    question_string = 'Question: ' + str(num1) + ' ' + str(num2)
    bigger_num = max(abs(num1), abs(num2))
    if (num1 * num2 == 0):  # check if one of them is zero
        return (question_string, bigger_num)

    gcd_max = min(abs(num1), abs(num2))  # num of attempts. Might be optimized?!
    result = 1
    i = 2
    while i <= gcd_max:
        if (num1 % i == 0) and (num2 % i == 0):
            result = i
        i += 1
    return (question_string, result)


def even(difficulty=DEFAULT_DIFFICULTY):
    ''''Even game. Generate random number.\
        Return 'question_string' and correct answer 'yes' or 'no'\
            depends on is generated number enev or not'''
    num = random.randint(0, difficulty)
    question_string = 'Question: ' + str(num)
    if (num % 2) == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (question_string, correct_answer)

# game procedures end
# ---------------------------------------------


def main():
    hello()

#  user-friendly shell for game selection
#    while True:
#        result = False
#        game_type = prompt.character('Plase select a game:\n'
#                                     '    - <C>alculator\n'
#                                     '    - odd or <E>ven\n'
#                                     '    - greatest common <D>ivisor\n'
#                                     '    - <P>rogression\n'
#                                     '    - pr<I>me\n'
#                                     'or <Q> to quit: ')
#        game_type = game_type.upper()
#        if game_type == 'Q':
#            print("Thanks for playing, ", str.strip(user_name), "! Bye!")
#            return
#        elif game_type in 'CEDPI':
#            result = launch_game(game_type, NUM_OF_ATTEMPTS)
#            if result:  # all games won
#                print(f'Congratulations, {user_name}!')
#            else:
#                print(f"Let's try again, {user_name}!")
#        else:
#            pass


if __name__ == '__main__':
    main()
