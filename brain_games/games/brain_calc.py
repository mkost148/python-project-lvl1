import random
import prompt
from brain_games.brain_servicelib import check_and_print_answer, hello


def calc(num_of_attempts=3, difficulty=20):
    user_name = hello()

    operators = ("+", "-", "*")  # three operators are available
    print('What is the result of the expression?')
    scores = 0
    while scores < num_of_attempts:
        num1 = random.randint(0, difficulty)
        num2 = random.randint(0, difficulty)
        oper_sym = random.choice(operators)

        print('Question:', str(num1), oper_sym, str(num2))

        if oper_sym == "+":  # 'plus'
            correct_answer = num1 + num2
        elif oper_sym == "-":  # 'minus'
            correct_answer = num1 - num2
        else:  # 'multiply'
            correct_answer = num1 * num2

        answer = int(prompt.string('Your answer: '))

        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = num_of_attempts + 1  # stop the game

    if (scores == num_of_attempts):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    calc()
