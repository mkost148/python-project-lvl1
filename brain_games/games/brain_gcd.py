import random
import prompt
from brain_games.brain_servicelib import check_and_print_answer


def get_gcd(num1, num2):
    """Find the greatest common divisor"""
    bigger_num = max(abs(num1), abs(num2))
    if (num1 == 0) or (num2 == 0):  # check if one of them is zero
        return bigger_num  # return maximum of them
    elif (num1 == num2):  # check if they are equal
        return num1

    # num of attempts is minimum of (half of bigger number) and (smaller number)
    gcd_max = bigger_num  # min(bigger_num // 2, smaller_num)

    result = 1
    i = 2
    while i <= gcd_max:
        if (num1 % i == 0) and (num2 % i == 0):
            result = i
        i += 1
    return result


def gcd(num_of_attempts=3, difficulty=20):
    print('Find the greatest common divisor of given numbers.')
    scores = 0
    while scores < num_of_attempts:
        num1 = random.randint(0, difficulty)
        num2 = random.randint(0, difficulty)
        print('Question: ', str(num1), ' ', str(num2))

        correct_answer = get_gcd(num1, num2)

        answer = prompt.integer('Your answer: ')

        if check_and_print_answer(answer, correct_answer):
            scores += 1
        else:
            scores = num_of_attempts + 1  # stop the game
    return (scores == num_of_attempts)


if __name__ == '__main__':
    gcd()
