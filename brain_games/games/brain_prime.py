import random
import prompt
from brain_games.brain_servicelib import check_and_print_answer, hello


def is_prime(number):
    """Check if 'number' is prime. Return boolean"""
    if abs(number) == 1:  # '1' is not prime nor combined number
        return False
    i = 2
    max_i = number // 2
    while i <= max_i:
        if number % i == 0:
            # uncomment the following for test
            # print('can be divided by ', str(i))
            return False
        i += 1
    return True


def prime(num_of_attempts=3, difficulty=20):
    user_name = hello()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    scores = 0
    while scores < num_of_attempts:
        number = random.randint(2, difficulty)  # from 2

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        print('Question: ', str(number))
        answer = str.lower(prompt.string('Your answer: '))

        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = num_of_attempts + 1  # stop the game

    if (scores == num_of_attempts):  # check if win a game
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    prime()
