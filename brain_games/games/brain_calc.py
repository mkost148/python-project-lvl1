import random
import prompt
from brain_games.brain_lib import print_answer


def calc(num_of_attempts=3, difficulty=20):
    oper_sym = ('+', '-', '*')  # three operators are available
    print('What is the result of the expression?')
    scores = 0
    while scores < num_of_attempts:
        num1 = random.randint(0, difficulty)
        num2 = random.randint(0, difficulty)
        oper_type = random.randint(0, 2)  # three operators are available
        print('Question: ', str(num1), ' ', oper_sym[oper_type], ' ', str(num2))

        if oper_type == 0:  # 'plus'
            correct_answer = num1 + num2
        elif oper_type == 1:  # 'minus'
            correct_answer = num1 - num2
        else:  # 'multiply'
            correct_answer = num1 * num2

        answer = int(prompt.string('Your answer: '))

        if answer == correct_answer:
            scores += 1
            print('Correct!')
        else:
            print_answer(correct_answer, answer)
            scores = num_of_attempts + 1  # stop the game
    return (scores == num_of_attempts)


if __name__ == '__main__':
    calc()
