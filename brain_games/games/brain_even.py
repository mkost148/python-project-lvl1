import random
import prompt
from brain_games.brain_servicelib import check_and_print_answer


def is_even(num):
    """Check if 'num' is even or odd"""
    return (num % 2) == 0


def even(num_of_attempts=3, difficulty=20):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    scores = 0
    while scores < num_of_attempts:
        num = random.randint(0, difficulty)
        print('Question: ', str(num))

        if is_even(num):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = str.lower(prompt.string('Your answer: '))

        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = num_of_attempts + 1  # stop the game
    return (scores == num_of_attempts)


if __name__ == '__main__':
    even()
